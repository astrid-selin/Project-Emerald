<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { journal } from '$lib/stores/journal';
	import { getCurrentMoonPhase } from '$lib/utils/moonPhase';
	import type { MoonPhase } from '$lib/types';
	import Card from '$lib/components/Card.svelte';
	import Button from '$lib/components/Button.svelte';
	import CardSelector from '$lib/components/CardSelector.svelte';

	// Form state
	let title = $state('');
	let entryType = $state<'reading' | 'dream' | 'practice' | 'reflection'>('reading');
	let spreadType = $state('');
	let selectedCards = $state<number[]>([]);
	let notes = $state('');
	let tags = $state('');
	let date = $state('');
	let moonPhase = $state<MoonPhase | null>(null);
	let errors = $state<Record<string, string>>({});
	let submitting = $state(false);

	onMount(() => {
		// Set default date to today
		date = new Date().toISOString().split('T')[0];

		// Get current moon phase
		moonPhase = getCurrentMoonPhase();
	});

	// Validate form
	function validateForm(): boolean {
		errors = {};

		if (!title.trim()) {
			errors.title = 'Title is required';
		}

		if (!notes.trim()) {
			errors.notes = 'Notes are required';
		}

		if (!date) {
			errors.date = 'Date is required';
		}

		return Object.keys(errors).length === 0;
	}

	// Handle form submission
	async function handleSubmit() {
		if (!validateForm()) {
			return;
		}

		submitting = true;

		try {
			// Parse tags
			const tagArray = tags
				.split(',')
				.map((t) => t.trim())
				.filter((t) => t.length > 0);

			// Create entry
			const entryId = journal.addEntry({
				date,
				title: title.trim(),
				entry_type: entryType,
				spread_type: spreadType.trim() || undefined,
				cards_drawn: selectedCards.length > 0 ? selectedCards : undefined,
				notes: notes.trim(),
				moon_phase: moonPhase ? `${moonPhase.emoji} ${moonPhase.phase}` : undefined,
				tags: tagArray.length > 0 ? tagArray : undefined
			});

			// Navigate to journal list
			goto('/journal');
		} catch (error) {
			console.error('Error creating entry:', error);
			errors.submit = 'Failed to create entry. Please try again.';
		} finally {
			submitting = false;
		}
	}

	// Handle cancel
	function handleCancel() {
		goto('/journal');
	}

	// Handle card selection
	function handleCardSelect(cardIds: number[]) {
		selectedCards = cardIds;
	}
</script>

<div class="max-w-3xl mx-auto">
	<!-- Page Header -->
	<div class="mb-8">
		<h2 class="text-4xl font-bold text-charcoal mb-2">New Journal Entry</h2>
		<p class="text-lg text-charcoal/70">Record your reading, dream, or practice</p>
	</div>

	<!-- Form -->
	<Card padding="lg">
		<form onsubmit={(e) => { e.preventDefault(); handleSubmit(); }}>
			<!-- Moon Phase Display -->
			{#if moonPhase}
				<div class="mb-6 p-4 bg-cream rounded-lg border-2 border-gold/30">
					<div class="flex items-center gap-3">
						<span class="text-4xl">{moonPhase.emoji}</span>
						<div>
							<p class="font-bold text-charcoal">{moonPhase.phase}</p>
							<p class="text-sm text-charcoal/70">{moonPhase.illumination}% illuminated</p>
						</div>
					</div>
				</div>
			{/if}

			<!-- Title -->
			<div class="mb-6">
				<label for="title" class="block text-sm font-medium text-gold mb-2">
					Title <span class="text-red-500">*</span>
				</label>
				<input
					id="title"
					type="text"
					bind:value={title}
					placeholder="e.g., Morning Three-Card Spread"
					class="w-full px-4 py-2 border border-charcoal/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald focus:border-transparent {errors.title
						? 'border-red-500'
						: ''}"
				/>
				{#if errors.title}
					<p class="text-red-500 text-sm mt-1">{errors.title}</p>
				{/if}
			</div>

			<!-- Date -->
			<div class="mb-6">
				<label for="date" class="block text-sm font-medium text-gold mb-2">
					Date <span class="text-red-500">*</span>
				</label>
				<input
					id="date"
					type="date"
					bind:value={date}
					class="w-full px-4 py-2 border border-charcoal/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald focus:border-transparent {errors.date
						? 'border-red-500'
						: ''}"
				/>
				{#if errors.date}
					<p class="text-red-500 text-sm mt-1">{errors.date}</p>
				{/if}
			</div>

			<!-- Entry Type -->
			<div class="mb-6">
				<label for="entry-type" class="block text-sm font-medium text-gold mb-2">
					Entry Type <span class="text-red-500">*</span>
				</label>
				<select
					id="entry-type"
					bind:value={entryType}
					class="w-full px-4 py-2 border border-charcoal/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald focus:border-transparent"
				>
					<option value="reading">Reading</option>
					<option value="dream">Dream</option>
					<option value="practice">Practice</option>
					<option value="reflection">Reflection</option>
				</select>
			</div>

			<!-- Spread Type (only for readings) -->
			{#if entryType === 'reading'}
				<div class="mb-6">
					<label for="spread-type" class="block text-sm font-medium text-gold mb-2">
						Spread Type
					</label>
					<input
						id="spread-type"
						type="text"
						bind:value={spreadType}
						placeholder="e.g., Three Card, Celtic Cross, Single Card"
						class="w-full px-4 py-2 border border-charcoal/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald focus:border-transparent"
					/>
				</div>
			{/if}

			<!-- Cards Drawn -->
			{#if entryType === 'reading'}
				<div class="mb-6">
					<CardSelector bind:selectedCards onSelect={handleCardSelect} />
				</div>
			{/if}

			<!-- Notes -->
			<div class="mb-6">
				<label for="notes" class="block text-sm font-medium text-gold mb-2">
					Notes <span class="text-red-500">*</span>
				</label>
				<textarea
					id="notes"
					bind:value={notes}
					rows="8"
					placeholder="Write your thoughts, interpretations, and reflections..."
					class="w-full px-4 py-2 border border-charcoal/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald focus:border-transparent resize-y {errors.notes
						? 'border-red-500'
						: ''}"
				></textarea>
				{#if errors.notes}
					<p class="text-red-500 text-sm mt-1">{errors.notes}</p>
				{/if}
			</div>

			<!-- Tags -->
			<div class="mb-6">
				<label for="tags" class="block text-sm font-medium text-gold mb-2">Tags</label>
				<input
					id="tags"
					type="text"
					bind:value={tags}
					placeholder="e.g., love, career, spiritual-growth (comma-separated)"
					class="w-full px-4 py-2 border border-charcoal/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald focus:border-transparent"
				/>
				<p class="text-xs text-charcoal/60 mt-1">Separate tags with commas</p>
			</div>

			<!-- Submit Error -->
			{#if errors.submit}
				<div class="mb-6 bg-red-50 border border-red-200 text-red-800 px-4 py-3 rounded-lg">
					<p class="text-sm">{errors.submit}</p>
				</div>
			{/if}

			<!-- Buttons -->
			<div class="flex flex-col sm:flex-row gap-3">
				<Button type="submit" variant="primary" size="lg" fullWidth={true} disabled={submitting}>
					{submitting ? 'Saving...' : 'Save Entry'}
				</Button>
				<button
					type="button"
					onclick={handleCancel}
					disabled={submitting}
					class="px-6 py-3 text-lg font-semibold text-charcoal border-2 border-charcoal/20 rounded-lg hover:bg-charcoal/5 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
				>
					Cancel
				</button>
			</div>
		</form>
	</Card>
</div>

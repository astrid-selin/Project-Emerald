<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import { journal } from '$lib/stores/journal';
	import { getCard } from '$lib/api';
	import type { JournalEntry, Card as CardType } from '$lib/types';
	import Card from '$lib/components/Card.svelte';
	import Badge from '$lib/components/Badge.svelte';
	import Button from '$lib/components/Button.svelte';
	import LoadingSpinner from '$lib/components/LoadingSpinner.svelte';

	let entryId = $state('');
	let entry = $state<JournalEntry | null>(null);
	let cards = $state<CardType[]>([]);
	let loading = $state(true);
	let loadingCards = $state(false);
	let showDeleteConfirm = $state(false);

	// Get entry type color
	function getEntryTypeColor(
		type: 'reading' | 'dream' | 'practice' | 'reflection'
	): 'emerald' | 'gray' | 'gold' {
		switch (type) {
			case 'reading':
				return 'emerald';
			case 'dream':
				return 'gray';
			case 'practice':
				return 'gold';
			case 'reflection':
				return 'gray';
			default:
				return 'gray';
		}
	}

	// Format date
	function formatDate(dateStr: string): string {
		const date = new Date(dateStr);
		return date.toLocaleDateString('en-US', {
			weekday: 'long',
			month: 'long',
			day: 'numeric',
			year: 'numeric'
		});
	}

	// Load entry and cards
	onMount(async () => {
		// Get entry ID from URL
		const unsubscribe = page.subscribe((p) => {
			entryId = p.params.id || '';
		});

		// Load entry
		const entries = await new Promise<JournalEntry[]>((resolve) => {
			const unsubJournal = journal.subscribe((value) => {
				resolve(value);
			});
			unsubJournal();
		});

		entry = entries.find((e) => e.id === entryId) || null;

		if (!entry) {
			loading = false;
			unsubscribe();
			return;
		}

		// Load cards if present
		if (entry.cards_drawn && entry.cards_drawn.length > 0) {
			loadingCards = true;
			try {
				const cardPromises = entry.cards_drawn.map((id) => getCard(id));
				cards = await Promise.all(cardPromises);
			} catch (error) {
				console.error('Error loading cards:', error);
			} finally {
				loadingCards = false;
			}
		}

		loading = false;
		unsubscribe();
	});

	// Handle delete
	function handleDelete() {
		if (!entry) return;

		journal.deleteEntry(entry.id);
		goto('/journal');
	}

	// Toggle delete confirmation
	function toggleDeleteConfirm() {
		showDeleteConfirm = !showDeleteConfirm;
	}
</script>

<div class="max-w-4xl mx-auto">
	<!-- Loading State -->
	{#if loading}
		<div class="flex flex-col items-center justify-center py-20">
			<LoadingSpinner size="lg" />
			<p class="text-charcoal/70 mt-4">Loading entry...</p>
		</div>
	{:else if !entry}
		<!-- Entry Not Found -->
		<div class="text-center py-20">
			<h2 class="text-3xl font-bold text-charcoal mb-4">Entry Not Found</h2>
			<p class="text-lg text-charcoal/70 mb-6">
				The journal entry you're looking for doesn't exist.
			</p>
			<Button href="/journal" variant="primary" size="lg">Back to Journal</Button>
		</div>
	{:else}
		<!-- Back Button -->
		<div class="mb-6">
			<Button href="/journal" variant="tertiary">← Back to Journal</Button>
		</div>

		<!-- Entry Content -->
		<Card padding="lg">
			<!-- Date and Moon Phase -->
			<div class="flex items-center justify-between mb-6 pb-6 border-b border-charcoal/10">
				<div>
					<p class="text-sm text-charcoal/60 mb-1">Entry Date</p>
					<p class="text-lg font-medium text-charcoal">{formatDate(entry.date)}</p>
				</div>
				{#if entry.moon_phase}
					<div class="text-right">
						<p class="text-4xl mb-1">{entry.moon_phase.split(' ')[0]}</p>
						<p class="text-sm text-charcoal/70">{entry.moon_phase.split(' ').slice(1).join(' ')}</p>
					</div>
				{/if}
			</div>

			<!-- Title -->
			<h1 class="text-3xl font-bold text-charcoal mb-4">{entry.title}</h1>

			<!-- Entry Type Badge -->
			<div class="mb-6">
				<Badge
					text={entry.entry_type.charAt(0).toUpperCase() + entry.entry_type.slice(1)}
					color={getEntryTypeColor(entry.entry_type)}
					size="md"
				/>
			</div>

			<!-- Spread Type -->
			{#if entry.spread_type}
				<div class="mb-6">
					<p class="text-sm font-medium text-gold mb-1">Spread Type</p>
					<p class="text-base text-charcoal">{entry.spread_type}</p>
				</div>
			{/if}

			<!-- Cards Drawn -->
			{#if entry.cards_drawn && entry.cards_drawn.length > 0}
				<div class="mb-6">
					<p class="text-sm font-medium text-gold mb-3">Cards Drawn</p>
					{#if loadingCards}
						<div class="flex items-center gap-2">
							<LoadingSpinner size="sm" />
							<span class="text-sm text-charcoal/70">Loading cards...</span>
						</div>
					{:else if cards.length > 0}
						<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3">
							{#each cards as card}
								<a
									href="/cards/{card.number}"
									class="block p-3 border border-charcoal/20 rounded-lg hover:border-emerald transition-colors"
								>
									<p class="font-medium text-charcoal mb-1">{card.name}</p>
									<p class="text-xs text-charcoal/60">
										{card.arcana}
										{#if card.suit}• {card.suit}{/if}
									</p>
									{#if card.keywords && card.keywords.length > 0}
										<div class="mt-2 flex flex-wrap gap-1">
											{#each card.keywords.slice(0, 2) as keyword}
												<span class="text-xs bg-emerald/10 text-emerald px-2 py-0.5 rounded">
													{keyword}
												</span>
											{/each}
										</div>
									{/if}
								</a>
							{/each}
						</div>
					{/if}
				</div>
			{/if}

			<!-- Notes -->
			<div class="mb-6">
				<p class="text-sm font-medium text-gold mb-3">Notes</p>
				<div class="prose prose-charcoal max-w-none">
					<p class="text-base text-charcoal whitespace-pre-wrap leading-relaxed">{entry.notes}</p>
				</div>
			</div>

			<!-- Tags -->
			{#if entry.tags && entry.tags.length > 0}
				<div class="mb-6">
					<p class="text-sm font-medium text-gold mb-3">Tags</p>
					<div class="flex flex-wrap gap-2">
						{#each entry.tags as tag}
							<Badge text={tag} color="gray" size="md" />
						{/each}
					</div>
				</div>
			{/if}

			<!-- Metadata -->
			<div class="mt-8 pt-6 border-t border-charcoal/10">
				<p class="text-xs text-charcoal/50">
					Created on {new Date(entry.created_at).toLocaleString('en-US', {
						month: 'long',
						day: 'numeric',
						year: 'numeric',
						hour: 'numeric',
						minute: '2-digit'
					})}
				</p>
			</div>
		</Card>

		<!-- Actions -->
		<div class="mt-6 flex flex-col sm:flex-row gap-3">
			<Button variant="secondary" size="md" disabled={true}>Edit (Coming Soon)</Button>

			{#if showDeleteConfirm}
				<div class="flex flex-col sm:flex-row gap-3 flex-1">
					<button
						onclick={handleDelete}
						class="px-6 py-2 text-base font-semibold bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors"
					>
						Confirm Delete
					</button>
					<button
						onclick={toggleDeleteConfirm}
						class="px-6 py-2 text-base font-semibold text-charcoal border-2 border-charcoal/20 rounded-lg hover:bg-charcoal/5 transition-colors"
					>
						Cancel
					</button>
				</div>
			{:else}
				<button
					onclick={toggleDeleteConfirm}
					class="px-6 py-2 text-base font-semibold text-red-600 border-2 border-red-600 rounded-lg hover:bg-red-50 transition-colors"
				>
					Delete Entry
				</button>
			{/if}
		</div>
	{/if}
</div>

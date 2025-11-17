<script lang="ts">
	import { onMount } from 'svelte';
	import { journal } from '$lib/stores/journal';
	import { getCard } from '$lib/api';
	import type { JournalEntry, Card as CardType } from '$lib/types';
	import Card from '$lib/components/Card.svelte';
	import Badge from '$lib/components/Badge.svelte';
	import Button from '$lib/components/Button.svelte';
	import ProtectedRoute from '$lib/components/ProtectedRoute.svelte';

	let entries = $state<JournalEntry[]>([]);
	let filter = $state<string>('all');
	let cardCache = $state<Map<number, CardType>>(new Map());

	// Subscribe to journal store
	journal.subscribe((value) => {
		entries = value;
	});

	// Fetch card names for entries that have cards
	async function loadCardNames(entry: JournalEntry) {
		if (!entry.cards_drawn || entry.cards_drawn.length === 0) return [];

		const cardNames: string[] = [];
		for (const cardId of entry.cards_drawn) {
			if (cardCache.has(cardId)) {
				cardNames.push(cardCache.get(cardId)!.name);
			} else {
				try {
					const card = await getCard(cardId);
					cardCache.set(cardId, card);
					cardNames.push(card.name);
				} catch (e) {
					cardNames.push(`Card #${cardId}`);
				}
			}
		}
		return cardNames;
	}

	// Get entry type color
	function getEntryTypeColor(
		type: 'reading' | 'dream' | 'practice' | 'reflection'
	): 'emerald' | 'gray' | 'gold' {
		switch (type) {
			case 'reading':
				return 'emerald';
			case 'dream':
				return 'gray'; // Using gray since we don't have purple
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
			month: 'short',
			day: 'numeric',
			year: 'numeric'
		});
	}

	// Get filtered entries
	let filteredEntries = $derived(filter === 'all' ? entries : entries.filter((e) => e.entry_type === filter));
</script>

<ProtectedRoute>
<div class="max-w-7xl mx-auto">
	<!-- Page Header -->
	<div class="mb-8 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
		<div>
			<h2 class="text-4xl font-bold text-charcoal mb-2">Your Journal</h2>
			<p class="text-lg text-charcoal/70">Track your readings, dreams, and magical practice</p>
		</div>
		<Button href="/journal/new" variant="primary" size="lg">+ New Entry</Button>
	</div>

	<!-- Filter Tabs -->
	<div class="mb-6 flex flex-wrap gap-2">
		<button
			onclick={() => (filter = 'all')}
			class="px-4 py-2 rounded-lg transition-colors {filter === 'all'
				? 'bg-emerald text-white'
				: 'bg-gray-100 text-charcoal hover:bg-gray-200'}"
		>
			All Entries
		</button>
		<button
			onclick={() => (filter = 'reading')}
			class="px-4 py-2 rounded-lg transition-colors {filter === 'reading'
				? 'bg-emerald text-white'
				: 'bg-gray-100 text-charcoal hover:bg-gray-200'}"
		>
			Readings
		</button>
		<button
			onclick={() => (filter = 'dream')}
			class="px-4 py-2 rounded-lg transition-colors {filter === 'dream'
				? 'bg-emerald text-white'
				: 'bg-gray-100 text-charcoal hover:bg-gray-200'}"
		>
			Dreams
		</button>
		<button
			onclick={() => (filter = 'practice')}
			class="px-4 py-2 rounded-lg transition-colors {filter === 'practice'
				? 'bg-emerald text-white'
				: 'bg-gray-100 text-charcoal hover:bg-gray-200'}"
		>
			Practice
		</button>
		<button
			onclick={() => (filter = 'reflection')}
			class="px-4 py-2 rounded-lg transition-colors {filter === 'reflection'
				? 'bg-emerald text-white'
				: 'bg-gray-100 text-charcoal hover:bg-gray-200'}"
		>
			Reflections
		</button>
	</div>

	<!-- Empty State -->
	{#if filteredEntries.length === 0 && filter === 'all'}
		<div class="text-center py-20">
			<p class="text-2xl text-charcoal/70 mb-4">No entries yet. Start your first reading!</p>
			<Button href="/journal/new" variant="primary" size="lg">Create Your First Entry</Button>
		</div>
	{:else if filteredEntries.length === 0}
		<div class="text-center py-20">
			<p class="text-xl text-charcoal/70">No {filter} entries found</p>
		</div>
	{:else}
		<!-- Entries Grid -->
		<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
			{#each filteredEntries as entry (entry.id)}
				<a href="/journal/{entry.id}" class="block group">
					<Card hover={true} padding="md">
						<!-- Date and Moon Phase -->
						<div class="flex items-center justify-between mb-3">
							<span class="text-sm text-charcoal/70">{formatDate(entry.date)}</span>
							{#if entry.moon_phase}
								<span class="text-xl">{entry.moon_phase.split(' ')[0]}</span>
							{/if}
						</div>

						<!-- Title -->
						<h3 class="text-xl font-bold text-charcoal mb-2 group-hover:text-emerald transition-colors">
							{entry.title}
						</h3>

						<!-- Entry Type Badge -->
						<div class="mb-3">
							<Badge
								text={entry.entry_type.charAt(0).toUpperCase() + entry.entry_type.slice(1)}
								color={getEntryTypeColor(entry.entry_type)}
								size="sm"
							/>
						</div>

						<!-- Cards Drawn -->
						{#if entry.cards_drawn && entry.cards_drawn.length > 0}
							{#await loadCardNames(entry)}
								<p class="text-sm text-charcoal/70 mb-3">
									Cards: {entry.cards_drawn.length} drawn
								</p>
							{:then cardNames}
								<p class="text-sm text-charcoal/70 mb-3">
									Cards: {cardNames.join(', ')}
								</p>
							{/await}
						{/if}

						<!-- Notes Preview -->
						<p class="text-sm text-charcoal/70 line-clamp-3 mb-3">
							{entry.notes.slice(0, 100)}{entry.notes.length > 100 ? '...' : ''}
						</p>

						<!-- Tags -->
						{#if entry.tags && entry.tags.length > 0}
							<div class="flex flex-wrap gap-1 mb-3">
								{#each entry.tags.slice(0, 3) as tag}
									<span class="text-xs bg-charcoal/10 text-charcoal px-2 py-1 rounded">
										{tag}
									</span>
								{/each}
								{#if entry.tags.length > 3}
									<span class="text-xs text-charcoal/50">+{entry.tags.length - 3} more</span>
								{/if}
							</div>
						{/if}

						<!-- View Details -->
						<div class="mt-4 pt-3 border-t border-emerald/10">
							<span class="text-sm text-emerald font-medium group-hover:underline">
								Read Entry →
							</span>
						</div>
					</Card>
				</a>
			{/each}
		</div>

		<!-- Entry Count -->
		<div class="mt-8 text-center text-charcoal/70">
			<p>
				Showing {filteredEntries.length}
				{filteredEntries.length === 1 ? 'entry' : 'entries'}
			</p>
		</div>
	{/if}
</div>
</ProtectedRoute>

<script lang="ts">
	import { onMount } from 'svelte';
	import { getCards } from '$lib/api';
	import type { Card as CardType } from '$lib/types';
	import Badge from './Badge.svelte';
	import LoadingSpinner from './LoadingSpinner.svelte';

	interface Props {
		selectedCards: number[];
		onSelect: (cardIds: number[]) => void;
	}

	let { selectedCards = $bindable(), onSelect }: Props = $props();

	let cards = $state<CardType[]>([]);
	let loading = $state(true);
	let searchQuery = $state('');
	let error = $state<string | null>(null);

	onMount(async () => {
		try {
			loading = true;
			error = null;
			cards = await getCards();
		} catch (err) {
			error = err instanceof Error ? err.message : 'Failed to load cards';
			console.error('Error loading cards:', err);
		} finally {
			loading = false;
		}
	});

	// Toggle card selection
	function toggleCard(cardId: number) {
		if (selectedCards.includes(cardId)) {
			const newSelection = selectedCards.filter((id) => id !== cardId);
			selectedCards = newSelection;
			onSelect(newSelection);
		} else {
			const newSelection = [...selectedCards, cardId];
			selectedCards = newSelection;
			onSelect(newSelection);
		}
	}

	// Filter cards based on search query
	let filteredCards = $derived(searchQuery
		? cards.filter(
				(card) =>
					card.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
					card.keywords.some((k) => k.toLowerCase().includes(searchQuery.toLowerCase()))
			)
		: cards);
</script>

<div class="card-selector">
	<!-- Header -->
	<div class="mb-4">
		<div class="flex items-center justify-between mb-2">
			<label class="block text-sm font-medium text-gold">Cards Drawn</label>
			{#if selectedCards.length > 0}
				<span class="text-sm text-charcoal/70">{selectedCards.length} selected</span>
			{/if}
		</div>

		<!-- Search Input -->
		<input
			type="text"
			bind:value={searchQuery}
			placeholder="Search cards by name or keyword..."
			class="w-full px-4 py-2 border border-charcoal/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald focus:border-transparent"
		/>
	</div>

	<!-- Loading State -->
	{#if loading}
		<div class="flex items-center justify-center py-8">
			<LoadingSpinner size="md" />
		</div>
	{/if}

	<!-- Error State -->
	{#if error}
		<div class="bg-red-50 border border-red-200 text-red-800 px-4 py-3 rounded-lg mb-4">
			<p class="text-sm">{error}</p>
		</div>
	{/if}

	<!-- Cards Grid -->
	{#if !loading && !error}
		<div class="max-h-96 overflow-y-auto border border-charcoal/20 rounded-lg p-4">
			{#if filteredCards.length === 0}
				<p class="text-center text-charcoal/70 py-8">No cards found</p>
			{:else}
				<div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
					{#each filteredCards as card (card.number)}
						<button
							type="button"
							onclick={() => toggleCard(card.number)}
							class="text-left px-3 py-2 rounded-lg border transition-all {selectedCards.includes(
								card.number
							)
								? 'border-emerald bg-emerald/10'
								: 'border-charcoal/20 hover:border-emerald/50'}"
						>
							<div class="flex items-center justify-between">
								<div class="flex-1 min-w-0">
									<p class="font-medium text-charcoal truncate">{card.name}</p>
									<p class="text-xs text-charcoal/60">
										{card.arcana}
										{#if card.suit}• {card.suit}{/if}
									</p>
								</div>
								{#if selectedCards.includes(card.number)}
									<span class="ml-2 text-emerald">✓</span>
								{/if}
							</div>
						</button>
					{/each}
				</div>
			{/if}
		</div>
	{/if}

	<!-- Selected Cards Display -->
	{#if selectedCards.length > 0 && !loading}
		<div class="mt-4">
			<p class="text-sm font-medium text-charcoal/70 mb-2">Selected Cards:</p>
			<div class="flex flex-wrap gap-2">
				{#each selectedCards as cardId}
					{@const card = cards.find((c) => c.number === cardId)}
					{#if card}
						<Badge text={card.name} color="emerald" size="sm" />
					{/if}
				{/each}
			</div>
		</div>
	{/if}
</div>

<style>
	.card-selector {
		width: 100%;
	}
</style>

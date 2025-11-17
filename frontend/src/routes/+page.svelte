<script lang="ts">
	import { onMount } from 'svelte';
	import { getCards } from '$lib/api';
	import type { Card as CardType } from '$lib/types';
	import Card from '$lib/components/Card.svelte';
	import Badge from '$lib/components/Badge.svelte';
	import LoadingSpinner from '$lib/components/LoadingSpinner.svelte';

	let cards = $state<CardType[]>([]);
	let loading = $state(true);
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
</script>

<div class="max-w-7xl mx-auto">
	<!-- Page Header -->
	<div class="mb-8">
		<h2 class="text-4xl font-bold text-charcoal mb-2">Tarot Card Library</h2>
		<p class="text-lg text-charcoal/70">
			Explore the complete deck of 78 tarot cards with their esoteric correspondences
		</p>
	</div>

	<!-- Loading State -->
	{#if loading}
		<div class="flex flex-col items-center justify-center py-20">
			<LoadingSpinner size="lg" />
			<p class="text-charcoal/70 mt-4">Loading cards...</p>
		</div>
	{/if}

	<!-- Error State -->
	{#if error}
		<div class="bg-red-50 border border-red-200 text-red-800 px-6 py-4 rounded-lg">
			<h3 class="font-bold mb-2">Error Loading Cards</h3>
			<p>{error}</p>
			<p class="text-sm mt-2 text-red-600">
				Make sure the backend API is running on http://localhost:5000
			</p>
		</div>
	{/if}

	<!-- Cards Grid -->
	{#if !loading && !error && cards.length > 0}
		<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
			{#each cards as card}
				<a href="/cards/{card.number}" class="block group">
					<Card hover={true} padding="md" border="none">
						<!-- Card Number Badge -->
						<div class="flex items-center justify-between mb-3">
							<Badge
								text={card.arcana === 'Major Arcana' ? 'Major' : card.suit || 'Minor'}
								color="gray"
								size="sm"
							/>
							<span class="text-xs text-charcoal/50 font-mono">#{card.number}</span>
						</div>

						<!-- Card Name -->
						<h3
							class="text-xl font-bold text-charcoal mb-2 group-hover:text-emerald transition-colors"
						>
							{card.name}
						</h3>

						<!-- Arcana Type -->
						<p class="text-sm text-charcoal/70 mb-3">
							{card.arcana}
							{#if card.element}
								<span class="text-gold">• {card.element}</span>
							{/if}
						</p>

						<!-- Keywords -->
						{#if card.keywords && card.keywords.length > 0}
							<div class="flex flex-wrap gap-2">
								{#each card.keywords.slice(0, 3) as keyword}
									<Badge text={keyword} color="emerald" size="sm" />
								{/each}
							</div>
						{/if}

						<!-- View Details -->
						<div class="mt-4 pt-3 border-t border-emerald/10">
							<span class="text-sm text-emerald font-medium group-hover:underline">
								View Details →
							</span>
						</div>
					</Card>
				</a>
			{/each}
		</div>

		<!-- Cards Count -->
		<div class="mt-8 text-center text-charcoal/70">
			<p>Showing {cards.length} cards</p>
		</div>
	{/if}

	<!-- Empty State -->
	{#if !loading && !error && cards.length === 0}
		<div class="text-center py-20">
			<p class="text-xl text-charcoal/70">No cards found</p>
		</div>
	{/if}
</div>

<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { getTreeOfLife } from '$lib/api';
	import type { Sephirah, Path } from '$lib/types';

	// Props
	interface Props {
		width?: number;
		height?: number;
		interactive?: boolean;
	}

	let { width = 600, height = 800, interactive = true }: Props = $props();

	// State
	let sephiroth: Sephirah[] = $state([]);
	let paths: Path[] = $state([]);
	let loading = $state(true);
	let error = $state<string | null>(null);
	let hoveredNode = $state<number | null>(null);

	// Sephiroth positions (x, y coordinates)
	const positions: Record<number, { x: number; y: number }> = {
		1: { x: 300, y: 50 },   // Kether (top center)
		2: { x: 450, y: 150 },  // Chokmah (upper right)
		3: { x: 150, y: 150 },  // Binah (upper left)
		4: { x: 450, y: 300 },  // Chesed (right)
		5: { x: 150, y: 300 },  // Geburah (left)
		6: { x: 300, y: 350 },  // Tiphareth (center)
		7: { x: 450, y: 500 },  // Netzach (lower right)
		8: { x: 150, y: 500 },  // Hod (lower left)
		9: { x: 300, y: 600 },  // Yesod (lower center)
		10: { x: 300, y: 750 }  // Malkuth (bottom)
	};

	// Load tree data
	onMount(async () => {
		try {
			const data = await getTreeOfLife();
			sephiroth = data.sephiroth.spheres;
			paths = data.paths.connections;
			loading = false;
		} catch (err) {
			error = err instanceof Error ? err.message : 'Failed to load Tree of Life';
			loading = false;
		}
	});

	// Get position for a sephirah by number
	function getSephirahPosition(number: number): { x: number; y: number } {
		return positions[number] || { x: 0, y: 0 };
	}

	// Handle node click
	function handleNodeClick(number: number) {
		if (interactive) {
			goto(`/qabalah/sephiroth/${number}`);
		}
	}
</script>

{#if loading}
	<div class="flex items-center justify-center" style="height: {height}px;">
		<div class="text-center">
			<div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-emerald-600"></div>
			<p class="mt-4 text-gray-600">Loading Tree of Life...</p>
		</div>
	</div>
{:else if error}
	<div class="flex items-center justify-center" style="height: {height}px;">
		<div class="text-center text-red-600">
			<p class="text-lg font-semibold">Error Loading Tree</p>
			<p class="mt-2">{error}</p>
		</div>
	</div>
{:else}
	<div class="tree-of-life-container flex justify-center">
		<svg viewBox="0 0 600 800" class="w-full h-auto max-w-full" style="max-height: {height}px;">
			<!-- Draw paths first (behind nodes) -->
			{#each paths as path}
				{@const fromPos = getSephirahPosition(path.connects_from)}
				{@const toPos = getSephirahPosition(path.connects_to)}
				<line
					x1={fromPos.x}
					y1={fromPos.y}
					x2={toPos.x}
					y2={toPos.y}
					stroke="#2B2B2B"
					stroke-width="2"
					opacity="0.3"
					class="transition-opacity duration-200"
				/>
			{/each}

			<!-- Draw nodes (on top of paths) -->
			{#each sephiroth as seph}
				{@const pos = getSephirahPosition(seph.number)}
				{@const isHovered = hoveredNode === seph.number}
				<g
					class={interactive ? 'cursor-pointer transition-all duration-200' : ''}
					onclick={() => handleNodeClick(seph.number)}
					onmouseenter={() => (hoveredNode = seph.number)}
					onmouseleave={() => (hoveredNode = null)}
					role={interactive ? 'button' : 'img'}
					tabindex={interactive ? 0 : -1}
					aria-label={`${seph.name} - Sephirah ${seph.number}`}
				>
					<!-- Circle -->
					<circle
						cx={pos.x}
						cy={pos.y}
						r="40"
						fill={isHovered ? '#50C878' : '#D4AF37'}
						stroke="#2B2B2B"
						stroke-width={isHovered ? 3 : 2}
						class="transition-all duration-200"
					/>

					<!-- Sephirah number (small, top of circle) -->
					<text
						x={pos.x}
						y={pos.y - 15}
						text-anchor="middle"
						font-size="12"
						font-weight="600"
						fill="#2B2B2B"
						class="pointer-events-none select-none"
					>
						{seph.number}
					</text>

					<!-- Sephirah name (center of circle) -->
					<text
						x={pos.x}
						y={pos.y + 5}
						text-anchor="middle"
						font-size="14"
						font-weight="700"
						fill="#2B2B2B"
						class="pointer-events-none select-none"
					>
						{seph.name}
					</text>

					<!-- Hebrew name (smaller, below English name) -->
					<text
						x={pos.x}
						y={pos.y + 20}
						text-anchor="middle"
						font-size="10"
						fill="#2B2B2B"
						opacity="0.8"
						class="pointer-events-none select-none"
					>
						{seph.hebrew_name}
					</text>
				</g>
			{/each}
		</svg>
	</div>
{/if}

<style>
	.tree-of-life-container {
		width: 100%;
		padding: 1rem;
	}

	/* Responsive adjustments */
	@media (max-width: 640px) {
		.tree-of-life-container {
			padding: 0.5rem;
		}
	}

	/* Ensure text is crisp */
	svg text {
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
	}
</style>

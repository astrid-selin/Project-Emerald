<script lang="ts">
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();
	const { cardData } = data;
	const { card, qabalah_path, connected_sephiroth, astrology } = cardData;

	// Helper function to get element color
	function getElementColor(element: string | null | undefined, suit: string | null | undefined): string {
		if (element === 'Fire' || suit === 'Wands') return '#FF6B35';
		if (element === 'Water' || suit === 'Cups') return '#4A90E2';
		if (element === 'Air' || suit === 'Swords') return '#F7DC6F';
		if (element === 'Earth' || suit === 'Pentacles') return '#52C41A';
		return '#9B59B6'; // Spirit/Major Arcana
	}

	const cardColor = getElementColor(card.element, card.suit);
</script>

<svelte:head>
	<title>{card.name} - Tarot Card Library</title>
</svelte:head>

<div class="max-w-5xl mx-auto">
	<!-- Header Section -->
	<div class="mb-8">
		<a
			href="/"
			class="inline-flex items-center text-emerald hover:text-emerald/80 font-medium mb-4 transition-colors"
		>
			<svg
				class="w-5 h-5 mr-2"
				fill="none"
				stroke="currentColor"
				viewBox="0 0 24 24"
			>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M10 19l-7-7m0 0l7-7m-7 7h18"
				/>
			</svg>
			Back to Cards
		</a>

		<h1 class="text-5xl font-bold text-charcoal mb-2">
			{card.number}. {card.name}
		</h1>
		<p class="text-2xl text-charcoal/70">{card.arcana}</p>
	</div>

	<!-- Main Content Grid -->
	<div class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-8">
		<!-- Left Column: Card Image Placeholder -->
		<div class="lg:col-span-1">
			<div
				class="rounded-lg shadow-lg overflow-hidden sticky top-8"
				style="background-color: {cardColor};"
			>
				<div class="aspect-[2/3] flex items-center justify-center p-8">
					<h2 class="text-3xl font-bold text-white text-center drop-shadow-lg">
						{card.name}
					</h2>
				</div>
			</div>
		</div>

		<!-- Right Column: Card Information -->
		<div class="lg:col-span-2 space-y-6">
			<!-- Basic Info Card -->
			<div class="bg-white rounded-lg shadow-md p-6 border border-charcoal/10">
				<h2 class="text-2xl font-bold text-gold mb-4">Basic Information</h2>
				<dl class="grid grid-cols-1 sm:grid-cols-2 gap-4">
					<div>
						<dt class="text-sm font-semibold text-charcoal/70 mb-1">Arcana</dt>
						<dd class="text-lg text-charcoal">{card.arcana}</dd>
					</div>
					{#if card.suit}
						<div>
							<dt class="text-sm font-semibold text-charcoal/70 mb-1">Suit</dt>
							<dd class="text-lg text-charcoal">{card.suit}</dd>
						</div>
					{/if}
					{#if card.element}
						<div>
							<dt class="text-sm font-semibold text-charcoal/70 mb-1">Element</dt>
							<dd class="text-lg text-charcoal">{card.element}</dd>
						</div>
					{/if}
					{#if astrology.planet || astrology.sign}
						<div>
							<dt class="text-sm font-semibold text-charcoal/70 mb-1">Astrology</dt>
							<dd class="text-lg text-charcoal">
								{#if astrology.planet}{astrology.planet}{/if}
								{#if astrology.planet && astrology.sign} in {/if}
								{#if astrology.sign}{astrology.sign}{/if}
							</dd>
						</div>
					{/if}
				</dl>
			</div>

			<!-- Keywords Section -->
			{#if card.keywords && card.keywords.length > 0}
				<div class="bg-white rounded-lg shadow-md p-6 border border-charcoal/10">
					<h2 class="text-2xl font-bold text-gold mb-4">Keywords</h2>
					<div class="flex flex-wrap gap-2">
						{#each card.keywords as keyword}
							<span class="bg-emerald text-white px-4 py-2 rounded-full text-sm font-medium">
								{keyword}
							</span>
						{/each}
					</div>
				</div>
			{/if}

			<!-- Meanings Section -->
			<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
				<!-- Upright Meaning -->
				<div class="bg-emerald/5 rounded-lg shadow-md p-6 border border-emerald/20">
					<h3 class="text-xl font-bold text-emerald mb-3">Upright Meaning</h3>
					<p class="text-charcoal leading-relaxed">{card.upright_meaning}</p>
				</div>

				<!-- Reversed Meaning -->
				<div class="bg-gold/5 rounded-lg shadow-md p-6 border border-gold/20">
					<h3 class="text-xl font-bold text-gold mb-3">Reversed Meaning</h3>
					<p class="text-charcoal leading-relaxed">{card.reversed_meaning}</p>
				</div>
			</div>

			<!-- Qabalah Correspondences Section -->
			{#if qabalah_path}
				<div class="bg-white rounded-lg shadow-md p-6 border-2 border-emerald">
					<h2 class="text-2xl font-bold text-emerald mb-4">
						Qabalistic Correspondences
					</h2>
					<dl class="space-y-3">
						<div>
							<dt class="text-sm font-semibold text-charcoal/70 mb-1">Hebrew Letter</dt>
							<dd class="text-lg text-charcoal">
								{qabalah_path.hebrew_letter} ({qabalah_path.letter_meaning})
							</dd>
						</div>
						<div>
							<dt class="text-sm font-semibold text-charcoal/70 mb-1">Tree of Life Path</dt>
							<dd class="text-lg text-charcoal">Path {qabalah_path.number}</dd>
						</div>
						<div>
							<dt class="text-sm font-semibold text-charcoal/70 mb-1">Connects</dt>
							<dd class="text-lg text-charcoal">
								{#if connected_sephiroth}
									<a
										href="/qabalah/sephiroth/{connected_sephiroth.from.number}"
										class="text-emerald hover:underline"
									>
										{qabalah_path.from_sephirah_name}
									</a>
									to
									<a
										href="/qabalah/sephiroth/{connected_sephiroth.to.number}"
										class="text-emerald hover:underline"
									>
										{qabalah_path.to_sephirah_name}
									</a>
								{:else}
									{qabalah_path.from_sephirah_name} to {qabalah_path.to_sephirah_name}
								{/if}
							</dd>
						</div>
						<div>
							<dt class="text-sm font-semibold text-charcoal/70 mb-1">Intelligence</dt>
							<dd class="text-lg text-charcoal italic">{qabalah_path.intelligence}</dd>
						</div>
					</dl>
				</div>
			{/if}

			<!-- Astrology Correspondences Section -->
			{#if astrology && (astrology.planet || astrology.sign || astrology.element)}
				<div class="bg-white rounded-lg shadow-md p-6 border-2 border-gold">
					<h2 class="text-2xl font-bold text-gold mb-4">Astrological Correspondences</h2>
					<dl class="space-y-3">
						{#if astrology.planet}
							<div>
								<dt class="text-sm font-semibold text-charcoal/70 mb-1">Planet</dt>
								<dd class="text-lg text-charcoal">{astrology.planet}</dd>
							</div>
						{/if}
						{#if astrology.sign}
							<div>
								<dt class="text-sm font-semibold text-charcoal/70 mb-1">Zodiac Sign</dt>
								<dd class="text-lg text-charcoal">{astrology.sign}</dd>
							</div>
						{/if}
						{#if astrology.element}
							<div>
								<dt class="text-sm font-semibold text-charcoal/70 mb-1">Element</dt>
								<dd class="text-lg text-charcoal">{astrology.element}</dd>
							</div>
						{/if}
					</dl>
				</div>
			{/if}
		</div>
	</div>

	<!-- Bottom Navigation -->
	<div class="flex justify-between items-center py-8 border-t border-charcoal/10">
		{#if card.number > 0}
			<a
				href="/cards/{card.number - 1}"
				class="inline-flex items-center text-emerald hover:text-emerald/80 font-medium transition-colors"
			>
				<svg
					class="w-5 h-5 mr-2"
					fill="none"
					stroke="currentColor"
					viewBox="0 0 24 24"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M15 19l-7-7 7-7"
					/>
				</svg>
				Previous Card
			</a>
		{:else}
			<div></div>
		{/if}

		{#if card.number < 77}
			<a
				href="/cards/{card.number + 1}"
				class="inline-flex items-center text-emerald hover:text-emerald/80 font-medium transition-colors"
			>
				Next Card
				<svg
					class="w-5 h-5 ml-2"
					fill="none"
					stroke="currentColor"
					viewBox="0 0 24 24"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M9 5l7 7-7 7"
					/>
				</svg>
			</a>
		{:else}
			<div></div>
		{/if}
	</div>
</div>

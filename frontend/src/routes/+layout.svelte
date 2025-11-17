<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<title>Emerald - Esoteric Education</title>
</svelte:head>

<div class="min-h-screen flex flex-col">
	<!-- Header -->
	<header class="bg-charcoal text-cream shadow-lg">
		<div class="container mx-auto px-4 py-6">
			<div class="flex items-center justify-between">
				<h1 class="text-3xl font-bold text-emerald">Emerald</h1>
				<nav class="flex gap-6">
					<a href="/" class="text-cream hover:text-emerald transition-colors">Cards</a>
					<a href="/about" class="text-cream hover:text-emerald transition-colors">About</a>
					<a href="/learn" class="text-cream hover:text-emerald transition-colors">Learn</a>
				</nav>
			</div>
		</div>
	</header>

	<!-- Main Content -->
	<main class="flex-1 container mx-auto px-4 py-8">
		{@render children()}
	</main>

	<!-- Footer -->
	<footer class="bg-charcoal text-cream mt-auto">
		<div class="container mx-auto px-4 py-6">
			<div class="text-center">
				<p class="text-sm">
					© {new Date().getFullYear()} Emerald. Esoteric education through Tarot, Qabalah, and
					Astrology.
				</p>
			</div>
		</div>
	</footer>
</div>

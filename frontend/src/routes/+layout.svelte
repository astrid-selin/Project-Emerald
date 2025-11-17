<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';
	import Header from '$lib/components/Header.svelte';
	import Footer from '$lib/components/Footer.svelte';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<title>Emerald - Esoteric Education</title>
</svelte:head>

<div class="flex flex-col min-h-screen">
	<Header />
	<main class="flex-grow container mx-auto px-4 py-8">
		{@render children()}
	</main>
	<Footer />
</div>

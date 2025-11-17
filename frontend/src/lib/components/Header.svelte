<script lang="ts">
	import { page } from '$app/stores';

	let menuOpen = $state(false);

	function toggleMenu() {
		menuOpen = !menuOpen;
	}

	function closeMenu() {
		menuOpen = false;
	}

	// Navigation links
	const navLinks = [
		{ href: '/', label: 'Home' },
		{ href: '/qabalah', label: 'Qabalah' },
		{ href: '/cards', label: 'Cards' },
		{ href: '/learn', label: 'Learn' },
		{ href: '/journal', label: 'Journal' }
	];

	// Check if a link is active
	function isActive(href: string): boolean {
		if (href === '/') {
			return $page.url.pathname === '/';
		}
		return $page.url.pathname.startsWith(href);
	}
</script>

<header class="bg-black text-gold sticky top-0 z-50 shadow-lg">
	<nav class="container mx-auto px-4 py-4">
		<div class="flex items-center justify-between">
			<!-- Logo/Brand -->
			<a href="/" class="text-2xl font-bold hover:text-gold-300 transition-colors">
				Emerald
			</a>

			<!-- Desktop Navigation -->
			<div class="hidden md:flex items-center gap-6">
				{#each navLinks as link}
					<a
						href={link.href}
						class="text-gold hover:text-gold-300 transition-colors relative py-2 {isActive(
							link.href
						)
							? 'border-b-2 border-emerald'
							: ''}"
					>
						{link.label}
					</a>
				{/each}
			</div>

			<!-- Mobile Menu Toggle -->
			<button
				onclick={toggleMenu}
				class="md:hidden text-gold hover:text-gold-300 text-3xl focus:outline-none"
				aria-label="Toggle menu"
			>
				{menuOpen ? '×' : '☰'}
			</button>
		</div>

		<!-- Mobile Menu -->
		{#if menuOpen}
			<div class="md:hidden mt-4 pb-4 border-t border-gold-700 pt-4">
				{#each navLinks as link}
					<a
						href={link.href}
						onclick={closeMenu}
						class="block py-2 text-gold hover:text-gold-300 hover:pl-2 transition-all {isActive(
							link.href
						)
							? 'border-l-4 border-emerald pl-2 font-semibold'
							: ''}"
					>
						{link.label}
					</a>
				{/each}
			</div>
		{/if}
	</nav>
</header>

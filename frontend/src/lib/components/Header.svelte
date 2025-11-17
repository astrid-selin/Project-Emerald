<script lang="ts">
	import { page } from '$app/stores';
	import { authStore } from '$lib/stores/auth';
	import { goto } from '$app/navigation';
	import Card from './Card.svelte';
	import Button from './Button.svelte';

	let menuOpen = $state(false);
	let userDropdownOpen = $state(false);

	function toggleMenu() {
		menuOpen = !menuOpen;
	}

	function closeMenu() {
		menuOpen = false;
	}

	function toggleUserDropdown() {
		userDropdownOpen = !userDropdownOpen;
	}

	function closeUserDropdown() {
		userDropdownOpen = false;
	}

	async function handleSignOut() {
		try {
			await authStore.signOut();
			closeUserDropdown();
			goto('/');
		} catch (error) {
			console.error('Error signing out:', error);
		}
	}

	// Navigation links (for logged-in users)
	const navLinks = [
		{ href: '/', label: 'Home' },
		{ href: '/qabalah', label: 'Qabalah' },
		{ href: '/cards', label: 'Cards' },
		{ href: '/learn', label: 'Learn' },
		{ href: '/journal', label: 'Journal' },
		{ href: '/about', label: 'About' }
	];

	// Navigation links for logged-out users
	const publicNavLinks = [
		{ href: '/', label: 'Home' },
		{ href: '/about', label: 'About' },
		{ href: '/pricing', label: 'Pricing' }
	];

	// Check if a link is active
	function isActive(href: string): boolean {
		if (href === '/') {
			return $page.url.pathname === '/';
		}
		return $page.url.pathname.startsWith(href);
	}

	// Get user avatar color based on email
	function getAvatarColor(email: string): string {
		const colors = [
			'bg-emerald',
			'bg-purple-600',
			'bg-blue-600',
			'bg-pink-600',
			'bg-orange-600',
			'bg-teal-600'
		];
		const hash = email.split('').reduce((acc, char) => acc + char.charCodeAt(0), 0);
		return colors[hash % colors.length];
	}

	// Get first letter of email
	function getInitial(email: string): string {
		return email.charAt(0).toUpperCase();
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
				{#each ($authStore.user ? navLinks : publicNavLinks) as link}
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

				<!-- User Profile or Sign In -->
				{#if $authStore.user}
					<div class="relative">
						<button
							onclick={toggleUserDropdown}
							class="flex items-center justify-center w-10 h-10 rounded-full {getAvatarColor(
								$authStore.user.email || ''
							)} text-white font-semibold hover:ring-2 hover:ring-gold transition-all"
							aria-label="User menu"
						>
							{getInitial($authStore.user.email || 'U')}
						</button>

						{#if userDropdownOpen}
							<div class="absolute right-0 mt-2 w-56">
								<Card padding="sm" shadow={true}>
									<div class="py-2">
										<div class="px-3 py-2 border-b border-gray-200">
											<p class="text-sm font-medium text-gray-900 truncate">
												{$authStore.user.email}
											</p>
										</div>
										<a
											href="/"
											class="block w-full text-left px-3 py-2 text-sm text-gray-700 hover:bg-gray-100 transition-colors"
											onclick={closeUserDropdown}
										>
											Dashboard
										</a>
										<a
											href="/settings"
											class="block w-full text-left px-3 py-2 text-sm text-gray-700 hover:bg-gray-100 transition-colors"
											onclick={closeUserDropdown}
										>
											Settings
										</a>
										<button
											class="w-full text-left px-3 py-2 text-sm text-red-600 hover:bg-gray-100 transition-colors"
											onclick={handleSignOut}
										>
											Sign Out
										</button>
									</div>
								</Card>
							</div>
						{/if}
					</div>
				{:else}
					<Button href="/login" variant="primary" size="sm">Sign In</Button>
				{/if}
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
				{#each ($authStore.user ? navLinks : publicNavLinks) as link}
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

				<!-- Mobile User Section -->
				<div class="border-t border-gold-700 mt-4 pt-4">
					{#if $authStore.user}
						<div class="mb-3">
							<p class="text-sm text-gold-300 mb-2">Signed in as:</p>
							<p class="text-gold font-medium truncate">{$authStore.user.email}</p>
						</div>
						<a
							href="/settings"
							onclick={closeMenu}
							class="block py-2 text-gold hover:text-gold-300 transition-colors"
						>
							Settings
						</a>
						<button
							onclick={handleSignOut}
							class="block w-full text-left py-2 text-red-400 hover:text-red-300 transition-colors"
						>
							Sign Out
						</button>
					{:else}
						<a
							href="/login"
							onclick={closeMenu}
							class="block py-2 text-gold hover:text-gold-300 transition-colors"
						>
							Sign In
						</a>
					{/if}
				</div>
			</div>
		{/if}
	</nav>
</header>

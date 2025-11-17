<script lang="ts">
	import { authStore } from '$lib/stores/auth';
	import { goto } from '$app/navigation';
	import Card from '$lib/components/Card.svelte';
	import Button from '$lib/components/Button.svelte';

	let email = $state('');
	let password = $state('');
	let errorMessage = $state('');
	let loading = $state(false);

	async function handleEmailLogin() {
		if (!email || !password) {
			errorMessage = 'Please enter both email and password';
			return;
		}

		if (!isValidEmail(email)) {
			errorMessage = 'Please enter a valid email address';
			return;
		}

		if (password.length < 6) {
			errorMessage = 'Password must be at least 6 characters';
			return;
		}

		errorMessage = '';
		loading = true;

		try {
			await authStore.signInWithEmail(email, password);
			goto('/');
		} catch (error: any) {
			errorMessage = formatFirebaseError(error.message);
		} finally {
			loading = false;
		}
	}

	async function handleGoogleLogin() {
		errorMessage = '';
		loading = true;

		try {
			await authStore.signInWithGoogle();
			goto('/');
		} catch (error: any) {
			errorMessage = formatFirebaseError(error.message);
		} finally {
			loading = false;
		}
	}

	function isValidEmail(email: string): boolean {
		const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
		return emailRegex.test(email);
	}

	function formatFirebaseError(error: string): string {
		if (error.includes('auth/invalid-credential') || error.includes('auth/wrong-password')) {
			return 'Invalid email or password';
		}
		if (error.includes('auth/user-not-found')) {
			return 'No account found with this email';
		}
		if (error.includes('auth/too-many-requests')) {
			return 'Too many failed attempts. Please try again later';
		}
		if (error.includes('auth/popup-closed-by-user')) {
			return 'Sign-in cancelled';
		}
		return 'An error occurred. Please try again';
	}
</script>

<svelte:head>
	<title>Sign In - Project Emerald</title>
</svelte:head>

<div class="min-h-screen bg-gradient-to-b from-cream to-white flex items-center justify-center p-4">
	<div class="w-full max-w-md">
		<Card padding="lg">
			<!-- Logo/Title -->
			<div class="text-center mb-8">
				<h1 class="text-3xl font-bold text-emerald mb-2">Project Emerald</h1>
				<p class="text-gray-600">Sign in to your account</p>
			</div>

			<!-- Error Message -->
			{#if errorMessage}
				<div class="mb-4 p-3 bg-red-100 border border-red-400 text-red-700 rounded">
					{errorMessage}
				</div>
			{/if}

			<!-- Email/Password Form -->
			<form onsubmit={(e) => { e.preventDefault(); handleEmailLogin(); }} class="space-y-4">
				<div>
					<label for="email" class="block text-sm font-medium text-gray-700 mb-1">
						Email Address
					</label>
					<input
						type="email"
						id="email"
						bind:value={email}
						disabled={loading}
						class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald focus:border-emerald disabled:opacity-50 disabled:cursor-not-allowed"
						placeholder="you@example.com"
						autocomplete="email"
					/>
				</div>

				<div>
					<label for="password" class="block text-sm font-medium text-gray-700 mb-1">
						Password
					</label>
					<input
						type="password"
						id="password"
						bind:value={password}
						disabled={loading}
						class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald focus:border-emerald disabled:opacity-50 disabled:cursor-not-allowed"
						placeholder="Enter your password"
						autocomplete="current-password"
					/>
				</div>

				<Button type="submit" variant="primary" size="lg" fullWidth={true} disabled={loading}>
					{loading ? 'Signing in...' : 'Sign In'}
				</Button>
			</form>

			<!-- Divider -->
			<div class="flex items-center my-6">
				<div class="flex-1 border-t border-gray-300"></div>
				<span class="px-4 text-sm text-gray-500">or</span>
				<div class="flex-1 border-t border-gray-300"></div>
			</div>

			<!-- Google Sign In -->
			<Button
				variant="secondary"
				size="lg"
				fullWidth={true}
				disabled={loading}
				onclick={handleGoogleLogin}
			>
				<span class="mr-2">🔐</span>
				Sign in with Google
			</Button>

			<!-- Sign Up Link -->
			<div class="mt-6 text-center text-sm">
				<span class="text-gray-600">Don't have an account?</span>
				<a href="/signup" class="ml-1 text-emerald font-semibold hover:underline">Sign up</a>
			</div>
		</Card>
	</div>
</div>

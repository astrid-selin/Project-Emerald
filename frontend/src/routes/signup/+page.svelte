<script lang="ts">
	import { authStore } from '$lib/stores/auth';
	import { goto } from '$app/navigation';
	import Card from '$lib/components/Card.svelte';
	import Button from '$lib/components/Button.svelte';

	let email = $state('');
	let password = $state('');
	let confirmPassword = $state('');
	let acceptTerms = $state(false);
	let errorMessage = $state('');
	let loading = $state(false);

	async function handleEmailSignup() {
		if (!email || !password || !confirmPassword) {
			errorMessage = 'Please fill in all fields';
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

		if (password.length < 8) {
			errorMessage = 'For better security, we recommend a password of at least 8 characters';
		}

		if (password !== confirmPassword) {
			errorMessage = 'Passwords do not match';
			return;
		}

		if (!acceptTerms) {
			errorMessage = 'Please accept the terms and conditions';
			return;
		}

		errorMessage = '';
		loading = true;

		try {
			await authStore.signUpWithEmail(email, password);
			goto('/');
		} catch (error: any) {
			errorMessage = formatFirebaseError(error.message);
		} finally {
			loading = false;
		}
	}

	async function handleGoogleSignup() {
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
		if (error.includes('auth/email-already-in-use')) {
			return 'An account with this email already exists';
		}
		if (error.includes('auth/weak-password')) {
			return 'Password is too weak. Please choose a stronger password';
		}
		if (error.includes('auth/invalid-email')) {
			return 'Invalid email address';
		}
		if (error.includes('auth/popup-closed-by-user')) {
			return 'Sign-up cancelled';
		}
		return 'An error occurred. Please try again';
	}

	function getPasswordStrength(password: string): string {
		if (!password) return '';
		if (password.length < 6) return 'Too short';
		if (password.length < 8) return 'Weak';
		if (password.length >= 12) return 'Strong';
		return 'Good';
	}

	function getPasswordStrengthColor(password: string): string {
		const strength = getPasswordStrength(password);
		if (strength === 'Too short' || strength === 'Weak') return 'text-red-600';
		if (strength === 'Good') return 'text-yellow-600';
		if (strength === 'Strong') return 'text-green-600';
		return '';
	}
</script>

<svelte:head>
	<title>Sign Up - Project Emerald</title>
</svelte:head>

<div class="min-h-screen bg-gradient-to-b from-cream to-white flex items-center justify-center p-4">
	<div class="w-full max-w-md">
		<Card padding="lg">
			<!-- Logo/Title -->
			<div class="text-center mb-8">
				<h1 class="text-3xl font-bold text-emerald mb-2">Project Emerald</h1>
				<p class="text-gray-600">Create your account</p>
			</div>

			<!-- Error Message -->
			{#if errorMessage}
				<div class="mb-4 p-3 bg-red-100 border border-red-400 text-red-700 rounded">
					{errorMessage}
				</div>
			{/if}

			<!-- Email/Password Form -->
			<form onsubmit={(e) => { e.preventDefault(); handleEmailSignup(); }} class="space-y-4">
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
						placeholder="At least 6 characters"
						autocomplete="new-password"
					/>
					{#if password}
						<p class="mt-1 text-sm {getPasswordStrengthColor(password)}">
							Password strength: {getPasswordStrength(password)}
						</p>
					{/if}
				</div>

				<div>
					<label for="confirmPassword" class="block text-sm font-medium text-gray-700 mb-1">
						Confirm Password
					</label>
					<input
						type="password"
						id="confirmPassword"
						bind:value={confirmPassword}
						disabled={loading}
						class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald focus:border-emerald disabled:opacity-50 disabled:cursor-not-allowed"
						placeholder="Re-enter your password"
						autocomplete="new-password"
					/>
					{#if confirmPassword && password !== confirmPassword}
						<p class="mt-1 text-sm text-red-600">Passwords do not match</p>
					{/if}
				</div>

				<!-- Terms Acceptance -->
				<div class="flex items-start">
					<input
						type="checkbox"
						id="terms"
						bind:checked={acceptTerms}
						disabled={loading}
						class="mt-1 h-4 w-4 text-emerald focus:ring-emerald border-gray-300 rounded disabled:opacity-50"
					/>
					<label for="terms" class="ml-2 text-sm text-gray-700">
						I accept the terms and conditions
					</label>
				</div>

				<Button type="submit" variant="primary" size="lg" fullWidth={true} disabled={loading}>
					{loading ? 'Creating account...' : 'Sign Up'}
				</Button>
			</form>

			<!-- Divider -->
			<div class="flex items-center my-6">
				<div class="flex-1 border-t border-gray-300"></div>
				<span class="px-4 text-sm text-gray-500">or</span>
				<div class="flex-1 border-t border-gray-300"></div>
			</div>

			<!-- Google Sign Up -->
			<Button
				variant="secondary"
				size="lg"
				fullWidth={true}
				disabled={loading}
				onclick={handleGoogleSignup}
			>
				<span class="mr-2">🔐</span>
				Sign up with Google
			</Button>

			<!-- Sign In Link -->
			<div class="mt-6 text-center text-sm">
				<span class="text-gray-600">Already have an account?</span>
				<a href="/login" class="ml-1 text-emerald font-semibold hover:underline">Sign in</a>
			</div>
		</Card>
	</div>
</div>

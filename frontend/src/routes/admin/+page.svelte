<script lang="ts">
	import { userProfile } from '$lib/stores/userProfile';
	import Button from '$lib/components/Button.svelte';
	import Card from '$lib/components/Card.svelte';
	import ProtectedRoute from '$lib/components/ProtectedRoute.svelte';

	async function toggleTier() {
		const currentTier = $userProfile?.tier || 'free';
		const newTier = currentTier === 'free' ? 'paid' : 'free';
		await userProfile.updateTier(newTier);
	}
</script>

<ProtectedRoute>
	<div class="max-w-3xl mx-auto">
		<Card padding="lg" border="gold">
			<div class="mb-6">
				<div class="flex items-center gap-2 mb-4">
					<svg
						class="w-6 h-6 text-gold"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
						></path>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
						></path>
					</svg>
					<h1 class="text-3xl font-bold text-charcoal">Admin: Testing Tools</h1>
				</div>
				<div
					class="bg-yellow-50 border border-yellow-300 rounded-lg p-4 mb-6 flex items-start gap-2"
				>
					<svg
						class="w-5 h-5 text-yellow-600 flex-shrink-0 mt-0.5"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
						></path>
					</svg>
					<div>
						<p class="text-sm font-semibold text-yellow-900 mb-1">Testing Environment Only</p>
						<p class="text-sm text-yellow-800">
							This page is for development and testing only. Remove before production deployment.
						</p>
					</div>
				</div>
			</div>

			<!-- User Profile Info -->
			<div class="bg-charcoal/5 rounded-lg p-6 mb-6">
				<h2 class="text-xl font-bold text-charcoal mb-4">Current User Profile</h2>
				{#if $userProfile}
					<div class="space-y-2 text-charcoal/80">
						<div class="flex justify-between">
							<span class="font-medium">Email:</span>
							<span>{$userProfile.email}</span>
						</div>
						<div class="flex justify-between">
							<span class="font-medium">User ID:</span>
							<span class="text-xs font-mono">{$userProfile.uid}</span>
						</div>
						<div class="flex justify-between">
							<span class="font-medium">Current Tier:</span>
							<span
								class="px-3 py-1 rounded-full text-sm font-semibold {$userProfile.tier ===
								'paid'
									? 'bg-emerald text-white'
									: 'bg-charcoal/20 text-charcoal'}"
							>
								{$userProfile.tier === 'paid' ? '✓ Premium' : 'Free'}
							</span>
						</div>
						<div class="flex justify-between">
							<span class="font-medium">Lessons Completed:</span>
							<span>{$userProfile.lessons_completed.length}</span>
						</div>
						<div class="flex justify-between">
							<span class="font-medium">Current Grade:</span>
							<span>{$userProfile.current_grade}</span>
						</div>
					</div>
				{:else}
					<p class="text-charcoal/60">Loading profile...</p>
				{/if}
			</div>

			<!-- Toggle Tier Action -->
			<div class="border-t border-charcoal/10 pt-6">
				<h2 class="text-xl font-bold text-charcoal mb-4">Actions</h2>
				<div class="bg-white rounded-lg p-6 border border-charcoal/20">
					<h3 class="font-semibold text-charcoal mb-2">Toggle Premium Subscription</h3>
					<p class="text-sm text-charcoal/70 mb-4">
						Switch between free and premium tier to test paywall and premium features. This
						directly updates your Firestore profile.
					</p>
					<Button variant="primary" size="lg" onclick={toggleTier}>
						{$userProfile?.tier === 'free' ? 'Enable Premium' : 'Disable Premium'}
					</Button>
				</div>
			</div>

			<!-- Quick Links -->
			<div class="mt-6 flex gap-3">
				<Button variant="secondary" size="sm" href="/pricing">View Pricing Page</Button>
				<Button variant="secondary" size="sm" href="/learn">View Learn Page</Button>
				<Button variant="secondary" size="sm" href="/journal">View Journal</Button>
			</div>
		</Card>
	</div>
</ProtectedRoute>

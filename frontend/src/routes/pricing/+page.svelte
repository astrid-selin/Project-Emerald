<script lang="ts">
	import Card from '$lib/components/Card.svelte';
	import Button from '$lib/components/Button.svelte';
	import ProtectedRoute from '$lib/components/ProtectedRoute.svelte';
	import { userProfile } from '$lib/stores/userProfile';
</script>

<ProtectedRoute>
	<div class="max-w-6xl mx-auto">
		<!-- Header -->
		<div class="text-center mb-12">
			<h1 class="text-5xl font-bold text-charcoal mb-4">Choose Your Path</h1>
			<p class="text-xl text-charcoal/70">
				Begin your journey or unlock the complete curriculum
			</p>
		</div>

		<!-- Pricing Cards -->
		<div class="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
			<!-- Free Tier -->
			<Card padding="lg" shadow={true}>
				<div class="flex flex-col h-full">
					<div class="mb-6">
						<div class="flex items-center justify-between mb-2">
							<h2 class="text-3xl font-bold text-charcoal">Seeker</h2>
							<span class="text-sm text-charcoal/60 bg-charcoal/10 px-3 py-1 rounded-full"
								>Free</span
							>
						</div>
						<p class="text-4xl font-bold text-gold mb-2">$0<span class="text-xl text-charcoal/60">/month</span></p>
						<p class="text-charcoal/70">Start your esoteric journey</p>
					</div>

					<div class="flex-grow mb-6">
						<h3 class="font-bold text-charcoal mb-3">What's included:</h3>
						<ul class="space-y-3">
							<li class="flex items-start gap-2">
								<svg
									class="w-5 h-5 text-emerald flex-shrink-0 mt-0.5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M5 13l4 4L19 7"
									></path>
								</svg>
								<span class="text-charcoal/80">First 3 weeks of curriculum</span>
							</li>
							<li class="flex items-start gap-2">
								<svg
									class="w-5 h-5 text-emerald flex-shrink-0 mt-0.5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M5 13l4 4L19 7"
									></path>
								</svg>
								<span class="text-charcoal/80">Complete tarot reference database</span>
							</li>
							<li class="flex items-start gap-2">
								<svg
									class="w-5 h-5 text-emerald flex-shrink-0 mt-0.5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M5 13l4 4L19 7"
									></path>
								</svg>
								<span class="text-charcoal/80">Basic journal (100 entries)</span>
							</li>
							<li class="flex items-start gap-2">
								<svg
									class="w-5 h-5 text-emerald flex-shrink-0 mt-0.5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M5 13l4 4L19 7"
									></path>
								</svg>
								<span class="text-charcoal/80">Tree of Life visualization</span>
							</li>
						</ul>
					</div>

					<div>
						{#if $userProfile?.tier === 'free'}
							<Button variant="secondary" size="lg" fullWidth={true} disabled={true}>
								Current Plan
							</Button>
						{:else}
							<Button variant="secondary" size="lg" fullWidth={true} href="/signup">
								Sign Up Free
							</Button>
						{/if}
					</div>
				</div>
			</Card>

			<!-- Premium Tier -->
			<Card padding="lg" shadow={true} border="emerald">
				<div class="flex flex-col h-full">
					<div class="mb-6">
						<div class="flex items-center justify-between mb-2">
							<h2 class="text-3xl font-bold text-charcoal">Practitioner</h2>
							<span
								class="text-sm text-white bg-emerald px-3 py-1 rounded-full font-semibold"
								>Popular</span
							>
						</div>
						<p class="text-4xl font-bold text-emerald mb-2">
							$8<span class="text-xl text-charcoal/60">/month</span>
						</p>
						<p class="text-charcoal/70">Complete esoteric education</p>
					</div>

					<div class="flex-grow mb-6">
						<h3 class="font-bold text-charcoal mb-3">Everything in Free, plus:</h3>
						<ul class="space-y-3">
							<li class="flex items-start gap-2">
								<svg
									class="w-5 h-5 text-emerald flex-shrink-0 mt-0.5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M5 13l4 4L19 7"
									></path>
								</svg>
								<span class="text-charcoal/80 font-medium"
									>Complete curriculum (250+ lessons)</span
								>
							</li>
							<li class="flex items-start gap-2">
								<svg
									class="w-5 h-5 text-emerald flex-shrink-0 mt-0.5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M5 13l4 4L19 7"
									></path>
								</svg>
								<span class="text-charcoal/80 font-medium"
									>All Golden Dawn grades (0°=0° through 7°=4°)</span
								>
							</li>
							<li class="flex items-start gap-2">
								<svg
									class="w-5 h-5 text-emerald flex-shrink-0 mt-0.5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M5 13l4 4L19 7"
									></path>
								</svg>
								<span class="text-charcoal/80 font-medium">Unlimited journal entries</span>
							</li>
							<li class="flex items-start gap-2">
								<svg
									class="w-5 h-5 text-emerald flex-shrink-0 mt-0.5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M5 13l4 4L19 7"
									></path>
								</svg>
								<span class="text-charcoal/80">Progress tracking & streaks</span>
							</li>
							<li class="flex items-start gap-2">
								<svg
									class="w-5 h-5 text-emerald flex-shrink-0 mt-0.5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M5 13l4 4L19 7"
									></path>
								</svg>
								<span class="text-charcoal/80">Daily planner & scheduling</span>
							</li>
							<li class="flex items-start gap-2">
								<svg
									class="w-5 h-5 text-emerald flex-shrink-0 mt-0.5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M5 13l4 4L19 7"
									></path>
								</svg>
								<span class="text-charcoal/80">Pattern analysis & insights</span>
							</li>
							<li class="flex items-start gap-2">
								<svg
									class="w-5 h-5 text-emerald flex-shrink-0 mt-0.5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M5 13l4 4L19 7"
									></path>
								</svg>
								<span class="text-charcoal/80">Cross-device sync</span>
							</li>
						</ul>
					</div>

					<div>
						{#if $userProfile?.tier === 'paid'}
							<Button variant="primary" size="lg" fullWidth={true} disabled={true}>
								Current Plan
							</Button>
						{:else}
							<Button variant="primary" size="lg" fullWidth={true} href="/admin">
								Upgrade Now
							</Button>
							<p class="text-xs text-center text-charcoal/60 mt-2">
								(Testing: Use admin page to toggle premium)
							</p>
						{/if}
					</div>
				</div>
			</Card>
		</div>

		<!-- FAQ or Additional Info -->
		<div class="mt-16 max-w-3xl mx-auto">
			<Card padding="lg" background="cream">
				<h2 class="text-2xl font-bold text-charcoal mb-4">Why Premium?</h2>
				<div class="space-y-4 text-charcoal/80">
					<p>
						<strong>Emerald</strong> is a labor of love, combining decades of Golden Dawn tradition
						with modern technology. The premium subscription helps us:
					</p>
					<ul class="list-disc ml-6 space-y-2">
						<li>Maintain and improve the platform</li>
						<li>Create new lessons and content regularly</li>
						<li>Keep your data secure and synced across devices</li>
						<li>Provide an ad-free, focused learning environment</li>
					</ul>
					<p class="italic">
						Cancel anytime. Your progress and journal entries are always yours.
					</p>
				</div>
			</Card>
		</div>
	</div>
</ProtectedRoute>

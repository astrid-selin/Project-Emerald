<script lang="ts">
	interface Props {
		completed: number;
		total: number;
		showLabel?: boolean;
	}

	let { completed, total, showLabel = true }: Props = $props();

	let percentage = $derived(Math.round((completed / total) * 100));
</script>

<div class="w-full">
	{#if showLabel}
		<div class="flex justify-between items-center mb-2">
			<span class="text-sm font-medium text-charcoal">Progress</span>
			<span class="text-sm text-charcoal/70">
				{completed} / {total} lessons
			</span>
		</div>
	{/if}

	<div class="w-full bg-charcoal/10 rounded-full h-3 overflow-hidden">
		<div
			class="bg-emerald h-full rounded-full transition-all duration-500 ease-out relative overflow-hidden"
			style="width: {percentage}%"
		>
			<!-- Shine effect -->
			<div
				class="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent animate-shimmer"
			></div>
		</div>
	</div>

	{#if showLabel}
		<div class="mt-1 text-xs text-right text-emerald font-semibold">
			{percentage}% complete
		</div>
	{/if}
</div>

<style>
	@keyframes shimmer {
		0% {
			transform: translateX(-100%);
		}
		100% {
			transform: translateX(100%);
		}
	}

	.animate-shimmer {
		animation: shimmer 2s infinite;
	}
</style>

<script lang="ts">
	import type { Snippet } from 'svelte';

	interface Props {
		padding?: 'sm' | 'md' | 'lg';
		shadow?: boolean;
		hover?: boolean;
		border?: 'none' | 'emerald' | 'gold';
		background?: 'white' | 'cream';
		children?: Snippet;
	}

	let {
		padding = 'md',
		shadow = true,
		hover = false,
		border = 'none',
		background = 'white',
		children
	}: Props = $props();

	// Compute classes based on props
	const paddingClasses = {
		sm: 'p-3',
		md: 'p-6',
		lg: 'p-8'
	};

	const shadowClasses = shadow ? 'shadow-md' : '';
	const hoverClasses = hover ? 'transition-all duration-200 hover:shadow-lg hover:-translate-y-1' : '';

	const borderClasses = {
		none: '',
		emerald: 'border-2 border-emerald',
		gold: 'border-2 border-gold'
	};

	const backgroundClasses = {
		white: 'bg-white',
		cream: 'bg-cream'
	};
</script>

<div
	class="rounded-lg {paddingClasses[padding]} {shadowClasses} {hoverClasses} {borderClasses[
		border
	]} {backgroundClasses[background]}"
>
	{#if children}
		{@render children()}
	{/if}
</div>

<script lang="ts">
	import type { Snippet } from 'svelte';

	interface Props {
		variant?: 'primary' | 'secondary' | 'tertiary';
		size?: 'sm' | 'md' | 'lg';
		disabled?: boolean;
		fullWidth?: boolean;
		href?: string;
		onclick?: () => void;
		type?: 'button' | 'submit' | 'reset';
		children?: Snippet;
	}

	let {
		variant = 'primary',
		size = 'md',
		disabled = false,
		fullWidth = false,
		href,
		onclick,
		type = 'button',
		children
	}: Props = $props();

	// Size classes
	const sizeClasses = {
		sm: 'px-3 py-1.5 text-sm',
		md: 'px-4 py-2 text-base',
		lg: 'px-6 py-3 text-lg'
	};

	// Variant classes
	const variantClasses = {
		primary:
			'bg-emerald text-white hover:bg-emerald-700 active:bg-emerald-800 font-semibold rounded-lg transition-colors duration-150',
		secondary:
			'border-2 border-gold text-black hover:bg-gold hover:text-white active:bg-gold-700 font-semibold rounded-lg transition-colors duration-150',
		tertiary:
			'text-emerald hover:underline active:text-emerald-700 font-medium transition-colors duration-150'
	};

	// Disabled classes
	const disabledClasses = disabled ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer';

	// Full width classes
	const widthClasses = fullWidth ? 'w-full' : '';

	// Combined classes
	const buttonClasses = `${sizeClasses[size]} ${variantClasses[variant]} ${disabledClasses} ${widthClasses} inline-flex items-center justify-center`;
</script>

{#if href}
	<a {href} class={buttonClasses} aria-disabled={disabled}>
		{#if children}
			{@render children()}
		{/if}
	</a>
{:else}
	<button {onclick} {disabled} {type} class={buttonClasses}>
		{#if children}
			{@render children()}
		{/if}
	</button>
{/if}

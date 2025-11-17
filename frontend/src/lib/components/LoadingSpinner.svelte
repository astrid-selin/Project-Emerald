<script lang="ts">
	interface Props {
		size?: 'sm' | 'md' | 'lg';
		color?: 'emerald' | 'gold';
	}

	let { size = 'md', color = 'emerald' }: Props = $props();

	// Size classes (width and height)
	const sizeClasses = {
		sm: 'w-4 h-4 border-2',
		md: 'w-8 h-8 border-3',
		lg: 'w-12 h-12 border-4'
	};

	// Color classes
	const colorClasses = {
		emerald: 'border-emerald border-t-transparent',
		gold: 'border-gold border-t-transparent'
	};

	const spinnerClasses = `${sizeClasses[size]} ${colorClasses[color]} rounded-full animate-spin`;
</script>

<div class="flex items-center justify-center">
	<div class={spinnerClasses}></div>
</div>

<style>
	@keyframes spin {
		to {
			transform: rotate(360deg);
		}
	}

	.animate-spin {
		animation: spin 1s linear infinite;
	}
</style>

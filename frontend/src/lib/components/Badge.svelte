<script lang="ts">
	interface Props {
		text: string;
		color?: 'emerald' | 'gold' | 'gray';
		size?: 'sm' | 'md';
	}

	let { text, color = 'emerald', size = 'md' }: Props = $props();

	// Size classes
	const sizeClasses = {
		sm: 'px-2 py-0.5 text-xs',
		md: 'px-3 py-1 text-sm'
	};

	// Color classes
	const colorClasses = {
		emerald: 'bg-emerald-100 text-emerald-800 border border-emerald-300',
		gold: 'bg-gold-100 text-gold-800 border border-gold-300',
		gray: 'bg-gray-100 text-gray-800 border border-gray-300'
	};

	const badgeClasses = `${sizeClasses[size]} ${colorClasses[color]} rounded-full font-medium inline-flex items-center justify-center`;
</script>

<span class={badgeClasses}>
	{text}
</span>

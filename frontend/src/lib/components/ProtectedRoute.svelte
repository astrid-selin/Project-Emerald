<script lang="ts">
	import { authStore } from '$lib/stores/auth';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import type { Snippet } from 'svelte';
	import LoadingSpinner from './LoadingSpinner.svelte';

	interface Props {
		children?: Snippet;
	}

	let { children }: Props = $props();

	let isChecking = $state(true);

	onMount(() => {
		// Subscribe to auth state changes
		const unsubscribe = authStore.subscribe((state) => {
			isChecking = state.loading;

			// If not loading and no user, redirect to login
			if (!state.loading && !state.user) {
				goto('/login');
			}
		});

		return () => {
			unsubscribe();
		};
	});
</script>

{#if $authStore.loading || isChecking}
	<div class="min-h-screen flex items-center justify-center">
		<LoadingSpinner />
	</div>
{:else if $authStore.user}
	{#if children}
		{@render children()}
	{/if}
{/if}

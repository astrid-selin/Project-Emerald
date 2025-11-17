<script lang="ts">
	import type { Lesson } from '$lib/types';

	interface Props {
		currentLessonId: string;
		allLessons: Lesson[];
		completedLessons: string[];
	}

	let { currentLessonId, allLessons, completedLessons }: Props = $props();

	let currentLesson = $derived(allLessons.find((l) => l.id === currentLessonId));
	let previousLesson = $derived(
		currentLesson ? allLessons.find((l) => l.order === currentLesson.order - 1) : null
	);
	let nextLesson = $derived(
		currentLesson ? allLessons.find((l) => l.order === currentLesson.order + 1) : null
	);

	let isNextLocked = $derived(() => {
		if (!nextLesson || !currentLesson) return false;
		// Next lesson is locked if current lesson is not completed
		return !completedLessons.includes(currentLesson.id);
	});
</script>

<nav
	class="mt-8 mb-8 border-t border-b border-charcoal/10 py-6 flex items-center justify-between"
>
	<!-- Previous Lesson -->
	<div class="flex-1">
		{#if previousLesson}
			<a
				href="/learn/{previousLesson.id}"
				class="group flex items-center gap-2 text-charcoal hover:text-emerald transition-colors"
			>
				<svg
					class="w-5 h-5 group-hover:-translate-x-1 transition-transform"
					fill="none"
					stroke="currentColor"
					viewBox="0 0 24 24"
				>
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"
					></path>
				</svg>
				<div>
					<div class="text-xs text-charcoal/60 uppercase tracking-wide">Previous</div>
					<div class="font-medium">{previousLesson.title}</div>
				</div>
			</a>
		{/if}
	</div>

	<!-- Progress Indicator -->
	{#if currentLesson}
		<div class="text-center px-4">
			<div class="text-sm font-medium text-charcoal/70">
				Lesson {currentLesson.order} of {allLessons.length}
			</div>
			<div class="mt-2 flex gap-1">
				{#each allLessons as lesson}
					<div
						class="h-1.5 w-8 rounded-full {completedLessons.includes(lesson.id)
							? 'bg-emerald'
							: lesson.id === currentLessonId
								? 'bg-gold'
								: 'bg-charcoal/20'}"
					></div>
				{/each}
			</div>
		</div>
	{/if}

	<!-- Next Lesson -->
	<div class="flex-1 flex justify-end">
		{#if nextLesson}
			{#if isNextLocked()}
				<div class="flex items-center gap-2 text-charcoal/40 cursor-not-allowed">
					<div class="text-right">
						<div class="text-xs uppercase tracking-wide">Next (Locked)</div>
						<div class="font-medium">{nextLesson.title}</div>
					</div>
					<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"
						></path>
					</svg>
				</div>
			{:else}
				<a
					href="/learn/{nextLesson.id}"
					class="group flex items-center gap-2 text-charcoal hover:text-emerald transition-colors"
				>
					<div class="text-right">
						<div class="text-xs text-charcoal/60 uppercase tracking-wide">Next</div>
						<div class="font-medium">{nextLesson.title}</div>
					</div>
					<svg
						class="w-5 h-5 group-hover:translate-x-1 transition-transform"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
					>
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"
						></path>
					</svg>
				</a>
			{/if}
		{/if}
	</div>
</nav>

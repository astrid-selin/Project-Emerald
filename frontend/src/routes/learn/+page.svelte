<script lang="ts">
	import { mockLessons } from '$lib/data/mockLessons';
	import type { Lesson } from '$lib/types';
	import Card from '$lib/components/Card.svelte';
	import Badge from '$lib/components/Badge.svelte';
	import Button from '$lib/components/Button.svelte';
	import ProtectedRoute from '$lib/components/ProtectedRoute.svelte';
	import ProgressBar from '$lib/components/ProgressBar.svelte';
	import { userProfile } from '$lib/stores/userProfile';

	let lessons = $state<Lesson[]>(mockLessons);

	// Get completed lessons from user profile
	let completedLessons = $derived($userProfile?.lessons_completed || []);

	function isLessonLocked(lesson: Lesson): boolean {
		// First lesson is always unlocked
		if (lesson.order === 1) return false;

		// Check if previous lesson is completed
		const previousLesson = lessons.find((l) => l.order === lesson.order - 1);
		if (!previousLesson) return false;

		return !completedLessons.includes(previousLesson.id);
	}

	function isLessonCompleted(lessonId: string): boolean {
		return completedLessons.includes(lessonId);
	}
</script>

<ProtectedRoute>
<div class="max-w-4xl mx-auto">
	<!-- Page Header -->
	<div class="mb-8">
		<h2 class="text-4xl font-bold text-charcoal mb-2">Learn Tarot & Qabalah</h2>
		<p class="text-lg text-charcoal/70">
			Structured curriculum following the Golden Dawn tradition
		</p>
	</div>

	<!-- Progress Overview -->
	<Card padding="md" border="emerald" background="cream">
		<div class="mb-4">
			<h3 class="text-xl font-bold text-charcoal mb-1">Your Progress</h3>
			<p class="text-charcoal/70">Keep learning to advance through the grades</p>
		</div>
		<ProgressBar completed={completedLessons.length} total={lessons.length} showLabel={true} />
	</Card>

	<!-- Lessons List -->
	<div class="space-y-4">
		{#each lessons as lesson}
			{@const locked = isLessonLocked(lesson)}
			{@const completed = isLessonCompleted(lesson.id)}

			<a
				href={locked ? '#' : `/learn/${lesson.id}`}
				class="block bg-white rounded-lg shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden border border-charcoal/10 {locked
					? 'opacity-60 cursor-not-allowed'
					: 'hover:border-emerald/50 group'}"
			>
				<div class="p-6">
					<div class="flex items-start justify-between gap-4">
						<!-- Left side: Content -->
						<div class="flex-1">
							<!-- Lesson Number & Title -->
							<div class="flex items-center gap-3 mb-2">
								<span
									class="flex items-center justify-center w-10 h-10 rounded-full font-bold {completed
										? 'bg-emerald text-white'
										: locked
											? 'bg-charcoal/20 text-charcoal/50'
											: 'bg-charcoal text-cream'}"
								>
									{#if completed}
										<svg
											class="w-6 h-6"
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
									{:else}
										{lesson.order}
									{/if}
								</span>
								<h3
									class="text-xl font-bold text-charcoal {!locked && 'group-hover:text-emerald transition-colors'}"
								>
									{lesson.title}
								</h3>
							</div>

							<!-- Grade Badge & Time -->
							<div class="flex items-center gap-3 ml-13 mb-2">
								<Badge text="{lesson.grade_name} ({lesson.grade})" color="gold" size="sm" />
								<span class="text-sm text-charcoal/70 flex items-center gap-1">
									<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
										></path>
									</svg>
									{lesson.estimated_time} min
								</span>
								{#if lesson.is_free}
									<Badge text="Free" color="emerald" size="sm" />
								{/if}
							</div>

							<!-- Sephirah Context -->
							<p class="text-sm text-charcoal/70 ml-13">
								{lesson.sephirah_context} • {lesson.quiz.length} quiz questions
							</p>
						</div>

						<!-- Right side: Lock icon or Start button -->
						<div class="flex items-center">
							{#if locked}
								<div class="text-center">
									<svg
										class="w-8 h-8 text-charcoal/30 mb-1"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"
										></path>
									</svg>
									<p class="text-xs text-charcoal/50">Locked</p>
								</div>
							{:else if completed}
								<div class="text-center">
									<svg
										class="w-8 h-8 text-emerald mb-1"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
										></path>
									</svg>
									<p class="text-xs text-emerald">Review</p>
								</div>
							{:else}
								<Button variant="primary" size="md">Start</Button>
							{/if}
						</div>
					</div>
				</div>

				<!-- Hover Effect Footer (only for unlocked lessons) -->
				{#if !locked}
					<div class="bg-emerald/5 px-6 py-3 border-t border-emerald/10">
						<span class="text-sm text-emerald font-medium group-hover:underline">
							{completed ? 'Review lesson' : 'Begin lesson'} →
						</span>
					</div>
				{/if}
			</a>
		{/each}
	</div>

	<!-- Footer Note -->
	<Card padding="md" border="gold" background="cream">
		<h3 class="font-bold text-charcoal mb-2">📚 About This Curriculum</h3>
		<p class="text-sm text-charcoal/70">
			This course follows the traditional Golden Dawn grade system, ascending the Tree of Life
			from Malkuth (Kingdom) to Kether (Crown). Complete each lesson and pass the quiz to unlock
			the next one. All Neophyte lessons are free.
		</p>
	</Card>
</div>
</ProtectedRoute>

<script lang="ts">
	import { mockLessons } from '$lib/data/mockLessons';
	import type { Lesson } from '$lib/types';

	let lessons = $state<Lesson[]>(mockLessons);
	let completedLessons = $state<string[]>([]);

	// Load completed lessons from localStorage
	$effect(() => {
		if (typeof window !== 'undefined') {
			const stored = localStorage.getItem('completed_lessons');
			completedLessons = stored ? JSON.parse(stored) : [];
		}
	});

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

<div class="max-w-4xl mx-auto">
	<!-- Page Header -->
	<div class="mb-8">
		<h2 class="text-4xl font-bold text-charcoal mb-2">Learn Tarot & Qabalah</h2>
		<p class="text-lg text-charcoal/70">
			Structured curriculum following the Golden Dawn tradition
		</p>
	</div>

	<!-- Progress Overview -->
	<div class="bg-emerald/10 border border-emerald/20 rounded-lg p-6 mb-8">
		<div class="flex items-center justify-between">
			<div>
				<h3 class="text-xl font-bold text-charcoal mb-1">Your Progress</h3>
				<p class="text-charcoal/70">
					{completedLessons.length} of {lessons.length} lessons completed
				</p>
			</div>
			<div class="text-right">
				<div class="text-3xl font-bold text-emerald">
					{Math.round((completedLessons.length / lessons.length) * 100)}%
				</div>
				<p class="text-sm text-charcoal/70">Complete</p>
			</div>
		</div>
		<!-- Progress Bar -->
		<div class="mt-4 bg-charcoal/10 rounded-full h-2 overflow-hidden">
			<div
				class="bg-emerald h-full transition-all duration-500"
				style="width: {(completedLessons.length / lessons.length) * 100}%"
			></div>
		</div>
	</div>

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
								<span class="text-xs font-semibold text-gold bg-gold/10 px-3 py-1 rounded-full">
									{lesson.grade_name} ({lesson.grade})
								</span>
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
									<span
										class="text-xs font-semibold text-emerald bg-emerald/10 px-2 py-1 rounded-full"
									>
										Free
									</span>
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
								<button
									class="px-6 py-2 bg-emerald text-white font-medium rounded-lg hover:bg-emerald/90 transition-colors"
								>
									Start
								</button>
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
	<div class="mt-8 p-6 bg-gold/10 border border-gold/20 rounded-lg">
		<h3 class="font-bold text-charcoal mb-2">📚 About This Curriculum</h3>
		<p class="text-sm text-charcoal/70">
			This course follows the traditional Golden Dawn grade system, ascending the Tree of Life
			from Malkuth (Kingdom) to Kether (Crown). Complete each lesson and pass the quiz to unlock
			the next one. All Neophyte lessons are free.
		</p>
	</div>
</div>

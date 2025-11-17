<script lang="ts">
	import { goto } from '$app/navigation';
	import type { Lesson } from '$lib/types';
	import LessonNav from '$lib/components/LessonNav.svelte';

	let { data } = $props();
	let lesson: Lesson = $derived(data.lesson);
	let allLessons: Lesson[] = $derived(data.allLessons);

	// Quiz state
	let selectedAnswers = $state<number[]>([]);
	let submitted = $state(false);
	let quizPassed = $state(false);
	let showMeditation = $state(false);

	// Load completion state
	let completedLessons = $state<string[]>([]);

	$effect(() => {
		if (typeof window !== 'undefined') {
			const stored = localStorage.getItem('completed_lessons');
			completedLessons = stored ? JSON.parse(stored) : [];

			// Reset quiz state when lesson changes
			selectedAnswers = new Array(lesson.quiz.length).fill(-1);
			submitted = false;
			quizPassed = false;
			showMeditation = false;
		}
	});

	function selectAnswer(questionIndex: number, answerIndex: number) {
		selectedAnswers[questionIndex] = answerIndex;
	}

	function submitQuiz() {
		submitted = true;

		// Check if all answers are correct
		const allCorrect = lesson.quiz.every((q, i) => selectedAnswers[i] === q.correct);

		if (allCorrect) {
			quizPassed = true;
			completeLesson(lesson.id);
		} else {
			quizPassed = false;
		}
	}

	function completeLesson(lessonId: string) {
		if (!completedLessons.includes(lessonId)) {
			completedLessons = [...completedLessons, lessonId];
			localStorage.setItem('completed_lessons', JSON.stringify(completedLessons));
		}
	}

	function goToNextLesson() {
		const nextLesson = allLessons.find((l) => l.order === lesson.order + 1);
		if (nextLesson) {
			goto(`/learn/${nextLesson.id}`);
		}
	}

	function retryQuiz() {
		selectedAnswers = new Array(lesson.quiz.length).fill(-1);
		submitted = false;
		quizPassed = false;
	}

	// Format theory text with markdown-style formatting
	function formatText(text: string): string {
		return text
			.replace(/\*\*(.*?)\*\*/g, '<strong class="text-gold">$1</strong>')
			.replace(/\n\n/g, '</p><p class="mb-4">');
	}
</script>

<div class="max-w-4xl mx-auto">
	<!-- Breadcrumb -->
	<nav class="mb-6 text-sm text-charcoal/70">
		<a href="/learn" class="hover:text-emerald transition-colors">Learn</a>
		<span class="mx-2">›</span>
		<span class="text-gold">{lesson.grade_name}</span>
		<span class="mx-2">›</span>
		<span class="text-charcoal">{lesson.title}</span>
	</nav>

	<!-- Lesson Header -->
	<div class="mb-8">
		<div class="flex items-start justify-between mb-2">
			<h1 class="text-4xl font-bold text-charcoal">{lesson.title}</h1>
			<span
				class="text-xs font-semibold text-gold bg-gold/10 px-3 py-1 rounded-full whitespace-nowrap ml-4"
			>
				{lesson.grade_name}
			</span>
		</div>
		<div class="flex items-center gap-4 text-charcoal/70">
			<span class="flex items-center gap-1">
				<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
					></path>
				</svg>
				{lesson.estimated_time} minutes
			</span>
			<span>•</span>
			<span>{lesson.sephirah_context}</span>
		</div>
	</div>

	<!-- Theory Section -->
	<section class="mb-8">
		<h2 class="text-2xl font-bold text-gold mb-4">Theory</h2>
		<div
			class="prose prose-lg max-w-none bg-white rounded-lg shadow-md p-8 border border-charcoal/10"
		>
			<div class="text-charcoal/90 leading-relaxed text-lg">
				{@html formatText(lesson.content.theory)}
			</div>
		</div>
	</section>

	<!-- Practice Section -->
	<section class="mb-8">
		<h2 class="text-2xl font-bold text-gold mb-4">Practice Exercise</h2>
		<div
			class="bg-emerald/5 border-2 border-emerald/20 rounded-lg p-8 shadow-md"
			style="max-width: 65ch;"
		>
			<div class="flex items-start gap-3 mb-4">
				<svg class="w-6 h-6 text-emerald flex-shrink-0 mt-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
					></path>
				</svg>
				<div class="text-charcoal/90 leading-relaxed">
					{@html formatText(lesson.content.practice)}
				</div>
			</div>
		</div>
	</section>

	<!-- Meditation Section (Collapsible) -->
	{#if lesson.content.meditation}
		<section class="mb-8">
			<button
				onclick={() => (showMeditation = !showMeditation)}
				class="w-full text-left flex items-center justify-between bg-charcoal/5 hover:bg-charcoal/10 transition-colors rounded-lg p-4 mb-2"
			>
				<h2 class="text-2xl font-bold text-gold">Meditation</h2>
				<svg
					class="w-6 h-6 text-gold transition-transform {showMeditation ? 'rotate-180' : ''}"
					fill="none"
					stroke="currentColor"
					viewBox="0 0 24 24"
				>
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
				</svg>
			</button>
			{#if showMeditation}
				<div class="bg-purple-50 border border-purple-200 rounded-lg p-8 shadow-md" style="max-width: 65ch;">
					<div class="flex items-start gap-3">
						<svg
							class="w-6 h-6 text-purple-600 flex-shrink-0 mt-1"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"
							></path>
						</svg>
						<div class="text-charcoal/90 leading-relaxed italic">
							{@html formatText(lesson.content.meditation)}
						</div>
					</div>
				</div>
			{/if}
		</section>
	{/if}

	<!-- Quiz Section -->
	<section class="mb-8">
		<h2 class="text-2xl font-bold text-gold mb-4">Knowledge Check</h2>
		<div class="bg-white rounded-lg shadow-md p-8 border border-charcoal/10">
			<p class="text-charcoal/70 mb-6">
				Answer all questions correctly to complete this lesson and unlock the next one.
			</p>

			<!-- Questions -->
			<div class="space-y-6">
				{#each lesson.quiz as question, qIndex}
					<div class="border-b border-charcoal/10 pb-6 last:border-b-0">
						<h3 class="font-bold text-charcoal mb-3">
							{qIndex + 1}. {question.question}
						</h3>

						<!-- Answer Options -->
						<div class="space-y-2">
							{#each question.answers as answer, aIndex}
								{@const isSelected = selectedAnswers[qIndex] === aIndex}
								{@const isCorrect = aIndex === question.correct}
								{@const showResult = submitted}

								<button
									onclick={() => !submitted && selectAnswer(qIndex, aIndex)}
									disabled={submitted}
									class="w-full text-left p-4 rounded-lg border-2 transition-all {submitted
										? isCorrect
											? 'border-green-500 bg-green-50'
											: isSelected
												? 'border-red-500 bg-red-50'
												: 'border-charcoal/10 bg-gray-50'
										: isSelected
											? 'border-emerald bg-emerald/10'
											: 'border-charcoal/20 hover:border-emerald/50 hover:bg-charcoal/5'}"
								>
									<div class="flex items-center gap-3">
										<!-- Radio Circle -->
										<div
											class="w-5 h-5 rounded-full border-2 flex items-center justify-center flex-shrink-0 {submitted
												? isCorrect
													? 'border-green-500 bg-green-500'
													: isSelected
														? 'border-red-500 bg-red-500'
														: 'border-charcoal/30'
												: isSelected
													? 'border-emerald bg-emerald'
													: 'border-charcoal/30'}"
										>
											{#if isSelected}
												<div class="w-2 h-2 rounded-full bg-white"></div>
											{/if}
											{#if submitted && isCorrect}
												<svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
													<path
														stroke-linecap="round"
														stroke-linejoin="round"
														stroke-width="3"
														d="M5 13l4 4L19 7"
													></path>
												</svg>
											{/if}
										</div>

										<!-- Answer Text -->
										<span
											class="{submitted
												? isCorrect
													? 'text-green-900 font-medium'
													: isSelected
														? 'text-red-900'
														: 'text-charcoal/60'
												: isSelected
													? 'text-charcoal font-medium'
													: 'text-charcoal'}"
										>
											{answer}
										</span>
									</div>
								</button>
							{/each}
						</div>

						<!-- Explanation (shown after submission) -->
						{#if submitted}
							<div
								class="mt-3 p-4 rounded-lg {selectedAnswers[qIndex] === question.correct
									? 'bg-green-50 border border-green-200'
									: 'bg-blue-50 border border-blue-200'}"
							>
								<p class="text-sm text-charcoal/80">
									<strong>Explanation:</strong>
									{question.explanation}
								</p>
							</div>
						{/if}
					</div>
				{/each}
			</div>

			<!-- Submit/Retry Button -->
			<div class="mt-8 flex flex-col items-center gap-4">
				{#if !submitted}
					<button
						onclick={submitQuiz}
						disabled={selectedAnswers.includes(-1)}
						class="px-8 py-3 bg-emerald text-white font-bold rounded-lg hover:bg-emerald/90 transition-colors disabled:bg-charcoal/30 disabled:cursor-not-allowed"
					>
						Submit Answers
					</button>
					{#if selectedAnswers.includes(-1)}
						<p class="text-sm text-charcoal/60">Please answer all questions before submitting</p>
					{/if}
				{:else if quizPassed}
					<div class="text-center">
						<div class="flex items-center gap-2 text-green-600 mb-2">
							<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
								></path>
							</svg>
							<span class="text-lg font-bold">Perfect! Lesson completed!</span>
						</div>
						<p class="text-charcoal/70 mb-4">You've mastered this material.</p>
					</div>
				{:else}
					<div class="text-center">
						<div class="flex items-center gap-2 text-red-600 mb-2">
							<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M6 18L18 6M6 6l12 12"
								></path>
							</svg>
							<span class="text-lg font-bold">Not quite. Review and try again!</span>
						</div>
						<p class="text-charcoal/70 mb-4">Review the incorrect answers and retry the quiz.</p>
						<button
							onclick={retryQuiz}
							class="px-6 py-2 bg-charcoal text-white font-medium rounded-lg hover:bg-charcoal/90 transition-colors"
						>
							Retry Quiz
						</button>
					</div>
				{/if}
			</div>
		</div>
	</section>

	<!-- References Section -->
	{#if lesson.content.references && lesson.content.references.length > 0}
		<section class="mb-8">
			<h2 class="text-xl font-bold text-charcoal mb-3">Further Reading</h2>
			<ul class="text-sm text-charcoal/70 space-y-1">
				{#each lesson.content.references as reference}
					<li class="flex items-start gap-2">
						<svg
							class="w-4 h-4 mt-0.5 flex-shrink-0 text-gold"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
							></path>
						</svg>
						{reference}
					</li>
				{/each}
			</ul>
		</section>
	{/if}

	<!-- Navigation -->
	<LessonNav currentLessonId={lesson.id} {allLessons} {completedLessons} />

	<!-- Next Lesson Button (shown only after passing quiz) -->
	{#if quizPassed}
		{@const nextLesson = allLessons.find((l) => l.order === lesson.order + 1)}
		{#if nextLesson}
			<div class="mt-8 text-center">
				<button
					onclick={goToNextLesson}
					class="px-8 py-4 bg-emerald text-white font-bold rounded-lg hover:bg-emerald/90 transition-all shadow-lg hover:shadow-xl text-lg"
				>
					Continue to Next Lesson →
				</button>
			</div>
		{:else}
			<div class="mt-8 p-6 bg-gold/10 border border-gold/20 rounded-lg text-center">
				<h3 class="font-bold text-charcoal mb-2">🎉 Congratulations!</h3>
				<p class="text-charcoal/70">
					You've completed all available lessons. Check back soon for more content!
				</p>
			</div>
		{/if}
	{/if}
</div>

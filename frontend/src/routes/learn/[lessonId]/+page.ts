import { mockLessons } from '$lib/data/mockLessons';
import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';

export const load: PageLoad = ({ params }) => {
	const lesson = mockLessons.find((l) => l.id === params.lessonId);

	if (!lesson) {
		throw error(404, 'Lesson not found');
	}

	return {
		lesson,
		allLessons: mockLessons
	};
};

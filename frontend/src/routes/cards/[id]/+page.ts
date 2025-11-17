import { error } from '@sveltejs/kit';
import { getCardWithCorrespondences } from '$lib/api';
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ params }) => {
	const cardId = parseInt(params.id);

	// Validate card ID (0-77 for standard tarot deck)
	if (isNaN(cardId) || cardId < 0 || cardId > 77) {
		throw error(404, {
			message: 'Card not found'
		});
	}

	try {
		const cardData = await getCardWithCorrespondences(cardId);
		return {
			cardData
		};
	} catch (err) {
		console.error('Error loading card:', err);
		throw error(500, {
			message: 'Failed to load card data'
		});
	}
};

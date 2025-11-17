import type {
	Card,
	CardWithCorrespondences,
	CardsResponse,
	CardQueryOptions,
	CardDetailWithCorrespondences,
	TreeOfLife
} from './types';

const API_BASE = 'http://localhost:5000';

/**
 * Fetch all tarot cards
 * @param options Query options (systems, arcana, suit, element)
 * @returns Array of cards
 */
export async function getCards(options: CardQueryOptions = {}): Promise<Card[]> {
	const params = new URLSearchParams();

	// Default to systems=false for compact format
	if (options.systems !== undefined) {
		params.append('systems', String(options.systems));
	} else {
		params.append('systems', 'false');
	}

	if (options.arcana) params.append('arcana', options.arcana);
	if (options.suit) params.append('suit', options.suit);
	if (options.element) params.append('element', options.element);

	const url = `${API_BASE}/cards${params.toString() ? '?' + params.toString() : ''}`;

	try {
		const response = await fetch(url);

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`);
		}

		const data: CardsResponse = await response.json();
		return data.cards;
	} catch (error) {
		console.error('Error fetching cards:', error);
		throw error;
	}
}

/**
 * Fetch a single card by ID (basic info)
 * @param id Card number (0-77)
 * @returns Single card
 */
export async function getCard(id: number): Promise<Card> {
	const url = `${API_BASE}/cards/${id}`;

	try {
		const response = await fetch(url);

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`);
		}

		return await response.json();
	} catch (error) {
		console.error(`Error fetching card ${id}:`, error);
		throw error;
	}
}

/**
 * Fetch a single card with full correspondences (Qabalah, Astrology)
 * @param id Card number (0-77)
 * @returns Card with correspondences
 */
export async function getCardWithCorrespondences(id: number): Promise<CardDetailWithCorrespondences> {
	const url = `${API_BASE}/cards/${id}/correspondences`;

	try {
		const response = await fetch(url);

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`);
		}

		return await response.json();
	} catch (error) {
		console.error(`Error fetching card correspondences for ${id}:`, error);
		throw error;
	}
}

/**
 * Get cards filtered by arcana type
 * @param arcana 'Major Arcana' or 'Minor Arcana'
 * @returns Array of cards
 */
export async function getCardsByArcana(arcana: 'Major Arcana' | 'Minor Arcana'): Promise<Card[]> {
	return getCards({ arcana });
}

/**
 * Get cards filtered by suit (for Minor Arcana)
 * @param suit Card suit (Wands, Cups, Swords, Pentacles)
 * @returns Array of cards
 */
export async function getCardsBySuit(suit: string): Promise<Card[]> {
	return getCards({ suit });
}

/**
 * Get cards filtered by element
 * @param element Element (Fire, Water, Air, Earth)
 * @returns Array of cards
 */
export async function getCardsByElement(element: string): Promise<Card[]> {
	return getCards({ element });
}

/**
 * Fetch the Tree of Life with all Sephiroth and Paths
 * @returns Tree of Life data with sephiroth and paths
 */
export async function getTreeOfLife(): Promise<TreeOfLife> {
	const url = `${API_BASE}/api/qabalah/tree`;

	try {
		const response = await fetch(url);

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`);
		}

		return await response.json();
	} catch (error) {
		console.error('Error fetching Tree of Life:', error);
		throw error;
	}
}

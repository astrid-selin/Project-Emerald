// Core Card Interface
export interface Card {
	number: number;
	name: string;
	arcana: 'Major Arcana' | 'Minor Arcana';
	suit?: string | null;
	element?: string | null;
	keywords: string[];
	upright_meaning: string;
	reversed_meaning: string;
}

// Qabalah Correspondence Interface
export interface QabalahCorrespondence {
	path_number?: number | null;
	hebrew_letter?: string | null;
	hebrew_meaning?: string | null;
	sephirah?: string | null;
	tree_position?: string | null;
	associated_deity?: string | null;
	spiritual_lesson?: string | null;
}

// Astrology Correspondence Interface
export interface AstrologyCorrespondence {
	planet?: string | null;
	zodiac_sign?: string | null;
	decan?: string | null;
	element?: string | null;
	modality?: string | null;
	house?: string | null;
	planetary_influence?: string | null;
}

// Full Card with Correspondences
export interface CardWithCorrespondences extends Card {
	qabalah?: QabalahCorrespondence | null;
	astrology?: AstrologyCorrespondence | null;
}

// API Response Types
export interface CardsResponse {
	cards: Card[];
}

export interface CardDetailResponse extends CardWithCorrespondences {}

// Filter/Query Options
export interface CardQueryOptions {
	systems?: boolean;
	arcana?: 'Major Arcana' | 'Minor Arcana';
	suit?: string;
	element?: string;
}

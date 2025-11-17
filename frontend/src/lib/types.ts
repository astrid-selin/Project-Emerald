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

// Sephirah Interface (Tree of Life)
export interface Sephirah {
	number: number;
	name: string;
	hebrew_name: string;
	divine_name: string;
	archangel: string;
	virtue: string;
	vice: string;
}

// Path Interface (22 Paths on Tree of Life)
export interface Path {
	number: number;
	hebrew_letter: string;
	hebrew_letter_meaning: string;
	connects_from: number;
	connects_to: number;
	card_number?: number;
	card_name?: string;
	from_sephirah_name?: string;
	to_sephirah_name?: string;
}

// Tree of Life Response
export interface TreeOfLife {
	name: string;
	description: string;
	sephiroth: {
		count: number;
		spheres: Sephirah[];
	};
	paths: {
		count: number;
		connections: Path[];
	};
}

// Card Detail Response with Full Correspondences
export interface CardDetailWithCorrespondences {
	card: Card;
	qabalah_path: {
		number: number;
		hebrew_letter: string;
		letter_meaning: string;
		from_sephirah_name: string;
		to_sephirah_name: string;
		intelligence: string;
	} | null;
	connected_sephiroth: {
		from: Sephirah;
		to: Sephirah;
	} | null;
	astrology: {
		planet?: string;
		sign?: string;
		element?: string;
	};
}

// Lesson System Types
export interface Lesson {
	id: string;
	title: string;
	grade: string;
	grade_name: string;
	sephirah_context: string;
	order: number;
	estimated_time: number; // minutes
	content: LessonContent;
	quiz: QuizQuestion[];
	unlocks_after_days: number;
	is_free: boolean;
}

export interface LessonContent {
	theory: string;
	practice: string;
	meditation?: string;
	references?: string[];
}

export interface QuizQuestion {
	question: string;
	answers: string[];
	correct: number; // index of correct answer
	explanation: string;
}

export interface UserProgress {
	lessons_completed: string[];
	current_grade: string;
	streak_days: number;
	last_activity: string;
}

// Journal System Types
export interface JournalEntry {
	id: string;
	date: string; // ISO format
	title: string;
	entry_type: 'reading' | 'dream' | 'practice' | 'reflection';
	cards_drawn?: number[]; // Card IDs
	spread_type?: string;
	notes: string;
	moon_phase?: string;
	tags?: string[];
	created_at: string;
}

export interface MoonPhase {
	phase: string; // "New Moon", "Waxing Crescent", etc.
	illumination: number; // 0-100
	emoji: string;
}

// User Profile Interface
export interface UserProfile {
	uid: string;
	email: string;
	display_name?: string;
	created_at: string;
	tier: 'free' | 'paid';
	subscription_status?: 'active' | 'canceled' | 'past_due';
	lessons_completed: string[];
	current_grade: string;
	streak_days: number;
	last_activity: string;
}

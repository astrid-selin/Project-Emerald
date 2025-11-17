import { writable, get } from 'svelte/store';
import type { JournalEntry } from '$lib/types';

function createJournalStore() {
	const { subscribe, set, update } = writable<JournalEntry[]>([]);

	// Load from localStorage on init
	if (typeof window !== 'undefined') {
		const stored = localStorage.getItem('journal_entries');
		if (stored) {
			try {
				set(JSON.parse(stored));
			} catch (e) {
				console.error('Failed to parse journal entries from localStorage:', e);
				set([]);
			}
		}
	}

	return {
		subscribe,

		addEntry: (entry: Omit<JournalEntry, 'id' | 'created_at'>) => {
			const newEntry: JournalEntry = {
				...entry,
				id: crypto.randomUUID(),
				created_at: new Date().toISOString()
			};

			update((entries) => {
				const updated = [newEntry, ...entries];
				if (typeof window !== 'undefined') {
					localStorage.setItem('journal_entries', JSON.stringify(updated));
				}
				return updated;
			});

			return newEntry.id;
		},

		updateEntry: (id: string, updates: Partial<JournalEntry>) => {
			update((entries) => {
				const updated = entries.map((e) => (e.id === id ? { ...e, ...updates } : e));
				if (typeof window !== 'undefined') {
					localStorage.setItem('journal_entries', JSON.stringify(updated));
				}
				return updated;
			});
		},

		deleteEntry: (id: string) => {
			update((entries) => {
				const updated = entries.filter((e) => e.id !== id);
				if (typeof window !== 'undefined') {
					localStorage.setItem('journal_entries', JSON.stringify(updated));
				}
				return updated;
			});
		},

		getEntry: (id: string): JournalEntry | undefined => {
			const entries = get({ subscribe });
			return entries.find((e) => e.id === id);
		}
	};
}

export const journal = createJournalStore();

import { writable, get } from 'svelte/store';
import { authStore } from './auth';
import * as firestoreService from '$lib/firebase/firestore';
import type { JournalEntry } from '$lib/types';

function createJournalStore() {
	const { subscribe, set, update } = writable<JournalEntry[]>([]);
	let currentUserId: string | null = null;

	// Load entries when user changes
	authStore.subscribe(async (authState) => {
		if (authState.user && authState.user.uid !== currentUserId) {
			currentUserId = authState.user.uid;
			try {
				const entries = await firestoreService.getJournalEntries(authState.user.uid);
				set(entries);
			} catch (error) {
				console.error('Failed to load journal entries:', error);
				set([]);
			}
		} else if (!authState.user) {
			currentUserId = null;
			set([]);
		}
	});

	return {
		subscribe,

		addEntry: async (entry: Omit<JournalEntry, 'id' | 'created_at'>) => {
			// Get current user synchronously
			let userId: string | null = null;
			authStore.subscribe(state => {
				if (state.user) userId = state.user.uid;
			})();

			if (!userId) throw new Error('Must be logged in to add journal entry');

			const newEntry = await firestoreService.addJournalEntry(userId, entry);

			// Update local state
			update(entries => [newEntry, ...entries]);

			return newEntry.id;
		},

		updateEntry: async (id: string, updates: Partial<JournalEntry>) => {
			// Note: This function is not implemented in the Firestore service yet
			// For now, we'll just update locally
			update((entries) => {
				return entries.map((e) => (e.id === id ? { ...e, ...updates } : e));
			});
		},

		deleteEntry: async (id: string) => {
			let userId: string | null = null;
			authStore.subscribe(state => {
				if (state.user) userId = state.user.uid;
			})();

			if (!userId) throw new Error('Must be logged in to delete journal entry');

			await firestoreService.deleteJournalEntry(userId, id);

			// Update local state
			update(entries => entries.filter((e) => e.id !== id));
		},

		getEntry: (id: string): JournalEntry | undefined => {
			const entries = get({ subscribe });
			return entries.find((e) => e.id === id);
		},

		refresh: async () => {
			let userId: string | null = null;
			authStore.subscribe(state => {
				if (state.user) userId = state.user.uid;
			})();

			if (!userId) return;

			const entries = await firestoreService.getJournalEntries(userId);
			set(entries);
		}
	};
}

export const journal = createJournalStore();

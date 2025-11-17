import * as firestoreService from '$lib/firebase/firestore';
import type { JournalEntry } from '$lib/types';

/**
 * Migrates journal entries from localStorage to Firestore
 * Should be called once after user's first login
 */
export async function migrateLocalStorageToFirestore(userId: string): Promise<void> {
	if (typeof window === 'undefined') return;

	try {
		// Check if migration has already been done
		const migrationKey = `migration_complete_${userId}`;
		if (localStorage.getItem(migrationKey)) {
			console.log('Migration already completed for this user');
			return;
		}

		// Get localStorage data
		const localEntries = localStorage.getItem('journal_entries');
		if (!localEntries) {
			console.log('No local journal entries to migrate');
			// Mark migration as complete even if there's nothing to migrate
			localStorage.setItem(migrationKey, 'true');
			return;
		}

		const entries: JournalEntry[] = JSON.parse(localEntries);
		console.log(`Migrating ${entries.length} journal entries to Firestore...`);

		// Upload to Firestore
		let successCount = 0;
		for (const entry of entries) {
			try {
				// Remove the old ID since Firestore will generate a new one
				const { id, created_at, ...entryData } = entry;
				await firestoreService.addJournalEntry(userId, entryData);
				successCount++;
			} catch (error) {
				console.error('Failed to migrate entry:', entry.id, error);
			}
		}

		console.log(`Successfully migrated ${successCount} out of ${entries.length} entries`);

		// Clear localStorage after successful migration
		localStorage.removeItem('journal_entries');

		// Mark migration as complete
		localStorage.setItem(migrationKey, 'true');

		console.log('Migration complete! Local storage cleared.');
	} catch (error) {
		console.error('Migration failed:', error);
		throw error;
	}
}

/**
 * Migrates completed lessons from localStorage to Firestore
 * Should be called once after user's first login
 */
export async function migrateCompletedLessons(userId: string): Promise<void> {
	if (typeof window === 'undefined') return;

	try {
		// Check if migration has already been done
		const migrationKey = `lessons_migration_complete_${userId}`;
		if (localStorage.getItem(migrationKey)) {
			console.log('Lessons migration already completed for this user');
			return;
		}

		// Get localStorage data
		const localLessons = localStorage.getItem('completed_lessons');
		if (!localLessons) {
			console.log('No completed lessons to migrate');
			localStorage.setItem(migrationKey, 'true');
			return;
		}

		const completedLessons: string[] = JSON.parse(localLessons);
		console.log(`Migrating ${completedLessons.length} completed lessons to Firestore...`);

		// Get current profile
		const profile = await firestoreService.getUserProfile(userId);
		if (!profile) {
			console.error('User profile not found');
			return;
		}

		// Merge with existing completed lessons (in case user completed some after login)
		const mergedLessons = Array.from(
			new Set([...profile.lessons_completed, ...completedLessons])
		);

		// Update profile
		await firestoreService.updateUserProfile(userId, {
			lessons_completed: mergedLessons
		});

		console.log(`Successfully migrated ${completedLessons.length} lessons`);

		// Clear localStorage
		localStorage.removeItem('completed_lessons');

		// Mark migration as complete
		localStorage.setItem(migrationKey, 'true');

		console.log('Lessons migration complete! Local storage cleared.');
	} catch (error) {
		console.error('Lessons migration failed:', error);
		throw error;
	}
}

/**
 * Migrates all data from localStorage to Firestore
 * Call this after successful login
 */
export async function migrateAllData(userId: string): Promise<void> {
	console.log('Starting data migration for user:', userId);

	try {
		await migrateLocalStorageToFirestore(userId);
		await migrateCompletedLessons(userId);
		console.log('All data migration complete!');
	} catch (error) {
		console.error('Data migration failed:', error);
		// Don't throw - we want the app to continue working even if migration fails
	}
}

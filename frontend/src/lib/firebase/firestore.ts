import {
  collection,
  doc,
  addDoc,
  getDoc,
  getDocs,
  updateDoc,
  deleteDoc,
  query,
  where,
  orderBy,
  setDoc,
  type DocumentData
} from 'firebase/firestore';
import { db } from './config';
import type { JournalEntry, UserProfile } from '$lib/types';

// Journal entries collection
export const journalCollection = (userId: string) =>
  collection(db, 'users', userId, 'journal');

export async function addJournalEntry(userId: string, entry: Omit<JournalEntry, 'id' | 'created_at'>) {
  const newEntry = {
    ...entry,
    created_at: new Date().toISOString(),
    user_id: userId
  };

  const docRef = await addDoc(journalCollection(userId), newEntry);
  // Update streak when adding journal entry
  await updateStreak(userId);
  return { ...newEntry, id: docRef.id };
}

export async function getJournalEntries(userId: string): Promise<JournalEntry[]> {
  const q = query(journalCollection(userId), orderBy('date', 'desc'));
  const snapshot = await getDocs(q);
  return snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() } as JournalEntry));
}

export async function getJournalEntry(userId: string, entryId: string): Promise<JournalEntry | null> {
  const docRef = doc(journalCollection(userId), entryId);
  const snapshot = await getDoc(docRef);
  if (!snapshot.exists()) return null;
  return { id: snapshot.id, ...snapshot.data() } as JournalEntry;
}

export async function deleteJournalEntry(userId: string, entryId: string) {
  const docRef = doc(journalCollection(userId), entryId);
  await deleteDoc(docRef);
}

// User profile collection
export const userProfileDoc = (userId: string) =>
  doc(db, 'users', userId);

export async function createUserProfile(userId: string, email: string) {
  const profile: UserProfile = {
    uid: userId,
    email,
    created_at: new Date().toISOString(),
    tier: 'free',
    lessons_completed: [],
    current_grade: '0°=0°',
    streak_days: 0,
    last_activity: new Date().toISOString()
  };

  await setDoc(userProfileDoc(userId), profile);
  return profile;
}

export async function getUserProfile(userId: string): Promise<UserProfile | null> {
  const snapshot = await getDoc(userProfileDoc(userId));
  if (!snapshot.exists()) return null;
  return snapshot.data() as UserProfile;
}

export async function updateUserProfile(userId: string, updates: Partial<UserProfile>) {
  await updateDoc(userProfileDoc(userId), updates as DocumentData);
}

export async function completeLesson(userId: string, lessonId: string) {
  const profile = await getUserProfile(userId);
  if (!profile) throw new Error('User profile not found');

  if (!profile.lessons_completed.includes(lessonId)) {
    const updated = [...profile.lessons_completed, lessonId];
    await updateUserProfile(userId, {
      lessons_completed: updated,
      last_activity: new Date().toISOString()
    });
    // Update streak when completing a lesson
    await updateStreak(userId);
  }
}

export async function updateStreak(userId: string) {
  const profile = await getUserProfile(userId);
  if (!profile) return;

  const today = new Date().toISOString().split('T')[0];
  const lastActivity = profile.last_activity.split('T')[0];

  const daysDiff = Math.floor(
    (new Date(today).getTime() - new Date(lastActivity).getTime()) / 86400000
  );

  let newStreak = profile.streak_days;

  if (daysDiff === 0) {
    // Same day, no change
    return;
  } else if (daysDiff === 1) {
    // Consecutive day, increment
    newStreak += 1;
  } else {
    // Streak broken, reset
    newStreak = 1;
  }

  await updateUserProfile(userId, {
    streak_days: newStreak,
    last_activity: new Date().toISOString()
  });
}

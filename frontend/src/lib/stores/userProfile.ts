import { writable } from 'svelte/store';
import { authStore } from './auth';
import * as firestoreService from '$lib/firebase/firestore';
import type { UserProfile } from '$lib/types';

function createUserProfileStore() {
  const { subscribe, set, update } = writable<UserProfile | null>(null);
  let currentUserId: string | null = null;

  // Load profile when user changes
  authStore.subscribe(async (authState) => {
    if (authState.user && authState.user.uid !== currentUserId) {
      currentUserId = authState.user.uid;
      try {
        let profile = await firestoreService.getUserProfile(authState.user.uid);

        // Create profile if doesn't exist
        if (!profile) {
          profile = await firestoreService.createUserProfile(
            authState.user.uid,
            authState.user.email || ''
          );
        }

        set(profile);
      } catch (error) {
        console.error('Failed to load user profile:', error);
        set(null);
      }
    } else if (!authState.user) {
      currentUserId = null;
      set(null);
    }
  });

  return {
    subscribe,

    completeLesson: async (lessonId: string) => {
      let userId: string | null = null;
      authStore.subscribe(state => {
        if (state.user) userId = state.user.uid;
      })();

      if (!userId) return;

      await firestoreService.completeLesson(userId, lessonId);

      // Refresh profile
      const profile = await firestoreService.getUserProfile(userId);
      set(profile);
    },

    updateTier: async (tier: 'free' | 'paid') => {
      let userId: string | null = null;
      authStore.subscribe(state => {
        if (state.user) userId = state.user.uid;
      })();

      if (!userId) return;

      await firestoreService.updateUserProfile(userId, { tier });

      const profile = await firestoreService.getUserProfile(userId);
      set(profile);
    },

    refresh: async () => {
      let userId: string | null = null;
      authStore.subscribe(state => {
        if (state.user) userId = state.user.uid;
      })();

      if (!userId) return;

      const profile = await firestoreService.getUserProfile(userId);
      set(profile);
    }
  };
}

export const userProfile = createUserProfileStore();

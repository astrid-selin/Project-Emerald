import { writable } from 'svelte/store';
import {
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  signInWithPopup,
  GoogleAuthProvider,
  signOut as firebaseSignOut,
  onAuthStateChanged,
  type User
} from 'firebase/auth';
import { auth } from '$lib/firebase/config';

interface AuthState {
  user: User | null;
  loading: boolean;
  error: string | null;
}

function createAuthStore() {
  const { subscribe, set, update } = writable<AuthState>({
    user: null,
    loading: true,
    error: null
  });

  // Listen to auth state changes
  onAuthStateChanged(auth, (user) => {
    set({ user, loading: false, error: null });
  });

  return {
    subscribe,

    signInWithEmail: async (email: string, password: string) => {
      update(state => ({ ...state, loading: true, error: null }));
      try {
        const result = await signInWithEmailAndPassword(auth, email, password);
        return result.user;
      } catch (error: any) {
        update(state => ({ ...state, error: error.message, loading: false }));
        throw error;
      }
    },

    signUpWithEmail: async (email: string, password: string) => {
      update(state => ({ ...state, loading: true, error: null }));
      try {
        const result = await createUserWithEmailAndPassword(auth, email, password);
        return result.user;
      } catch (error: any) {
        update(state => ({ ...state, error: error.message, loading: false }));
        throw error;
      }
    },

    signInWithGoogle: async () => {
      update(state => ({ ...state, loading: true, error: null }));
      try {
        const provider = new GoogleAuthProvider();
        const result = await signInWithPopup(auth, provider);
        return result.user;
      } catch (error: any) {
        update(state => ({ ...state, error: error.message, loading: false }));
        throw error;
      }
    },

    signOut: async () => {
      try {
        await firebaseSignOut(auth);
      } catch (error: any) {
        update(state => ({ ...state, error: error.message }));
        throw error;
      }
    }
  };
}

export const authStore = createAuthStore();

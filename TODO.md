# Project Emerald - TODO List

## 🚨 CRITICAL - Do This First

### Set Up Firestore Security Rules
**Status:** ⏳ Not Done
**Priority:** HIGH - Required for the app to work properly

Go to Firebase Console → Firestore Database → Rules and paste this:

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;

      match /journal/{entryId} {
        allow read, write: if request.auth != null && request.auth.uid == userId;
      }
    }
  }
}
```

**Why:** Without these rules, Firestore operations will fail due to permission denied errors.

---

## ✅ Testing Checklist

### Initial Setup Testing
- [ ] Log in with an existing account
- [ ] Create a new account
- [ ] Verify user profile is auto-created in Firestore
- [ ] Check Firestore console to see user document created

### Journal Migration Testing
- [ ] Log in with account that has old localStorage journal entries
- [ ] Verify entries migrated to Firestore
- [ ] Check console logs for "Migration complete!" message
- [ ] Verify localStorage cleared after migration
- [ ] Test creating new journal entry (should go directly to Firestore)

### Lesson Progress Testing
- [ ] Complete a lesson quiz
- [ ] Verify completion saved to Firestore user profile
- [ ] Check progress bar updates on Learn page
- [ ] Log out and log back in - verify progress persisted

### Paywall Testing
- [ ] As free user, visit lesson 1-3 (should be accessible)
- [ ] As free user, visit lesson 4-6 (should show paywall)
- [ ] Go to `/admin` and toggle to premium
- [ ] Visit lesson 4-6 (should now be accessible)
- [ ] Toggle back to free, verify paywall returns

### Pricing Page Testing
- [ ] Visit `/pricing` page
- [ ] Verify Free and Premium tiers display correctly
- [ ] Check buttons reflect current tier
- [ ] Test navigation from paywall → pricing page

### Cross-Device Sync Testing
- [ ] Log in on Device A, create journal entry
- [ ] Log in on Device B with same account
- [ ] Verify journal entry appears on Device B
- [ ] Complete lesson on Device B
- [ ] Verify completion shows on Device A

---

## 🛠️ Before Production

### Security & Cleanup
- [ ] **REMOVE** `/frontend/src/routes/admin/+page.svelte`
  ⚠️ This is a security risk in production - anyone can toggle premium!

- [ ] Update pricing page button to remove admin page reference
  - Change `href="/admin"` to `href="/api/create-checkout"`
  - Remove testing note text

- [ ] Review all console.log statements and remove sensitive data logging

### Stripe Integration
- [ ] Sign up for Stripe account
- [ ] Create products/prices in Stripe dashboard
  - Free tier: $0/month (or skip this)
  - Premium tier: $8/month recurring subscription

- [ ] Install Stripe SDK: `npm install stripe @stripe/stripe-js`

- [ ] Implement `/frontend/src/routes/api/create-checkout/+server.ts`
  - Create checkout session
  - Set up success/cancel URLs
  - Add metadata (userId, tier)

- [ ] Create webhook endpoint `/frontend/src/routes/api/webhook/stripe/+server.ts`
  - Handle `checkout.session.completed` event
  - Update user tier in Firestore
  - Handle `customer.subscription.deleted` for cancellations

- [ ] Add webhook URL to Stripe dashboard
- [ ] Test payment flow end-to-end
- [ ] Test subscription cancellation flow

### Environment Variables
- [ ] Ensure `.env` file has:
  ```
  VITE_FIREBASE_API_KEY=...
  VITE_FIREBASE_AUTH_DOMAIN=...
  VITE_FIREBASE_PROJECT_ID=...
  VITE_FIREBASE_STORAGE_BUCKET=...
  VITE_FIREBASE_MESSAGING_SENDER_ID=...
  VITE_FIREBASE_APP_ID=...
  STRIPE_SECRET_KEY=sk_live_...
  STRIPE_WEBHOOK_SECRET=whsec_...
  ```

- [ ] Add to deployment platform (Vercel/Netlify)

### Firebase Settings
- [ ] Enable email/password authentication (if not already enabled)
- [ ] Configure authorized domains for production URL
- [ ] Set up Firebase indexes if needed (check Firestore logs)
- [ ] Review Firebase quotas (free tier limits)

---

## 📋 Future Enhancements

### User Experience
- [ ] Add loading states while Firestore loads data
- [ ] Add error boundaries for Firestore failures
- [ ] Implement offline support with Firestore offline persistence
- [ ] Add "Manage Subscription" page (cancel, upgrade, billing history)
- [ ] Add email notifications for lesson completion milestones

### Features
- [ ] Add pattern analysis for journal entries
- [ ] Create daily planner functionality
- [ ] Implement streak tracking
- [ ] Add more lessons (currently only 6)
- [ ] Create achievement/badge system

### Content
- [ ] Add lessons for Zelator grade (1°=10°)
- [ ] Add lessons for Theoricus grade (2°=9°)
- [ ] Continue through all Golden Dawn grades
- [ ] Add practical exercises and meditations

### Analytics & Monitoring
- [ ] Set up error tracking (Sentry)
- [ ] Add analytics (Google Analytics, Plausible)
- [ ] Monitor Firestore usage and costs
- [ ] Track conversion rate (free → premium)

---

## 📝 Notes

### Migration Behavior
- Migration runs **once per user** on first login
- Migration status stored in localStorage with keys:
  - `migration_complete_{userId}` - for journal entries
  - `lessons_migration_complete_{userId}` - for lesson progress
- If migration fails, app continues to work (non-blocking)

### Current Lesson Distribution
- **Free (Lessons 1-3):**
  1. Introduction to the Four Elements
  2. The Ten Sephiroth: An Overview
  3. Major Arcana: The Fool's Journey

- **Premium (Lessons 4-6):**
  4. The Minor Arcana: Court Cards
  5. The Minor Arcana: Numbered Cards
  6. Creating Sacred Space

### Admin Page Location
- Dev/Testing: `http://localhost:5173/admin`
- Shows current user profile
- Toggle premium/free tier
- **Must be removed before production!**

---

## 🎯 Success Criteria

The Firestore migration is successful when:
- ✅ Journal entries save to Firestore (not localStorage)
- ✅ Journal loads from Firestore on all devices
- ✅ Lesson progress tracked in user profile
- ✅ Paywall works correctly (free users blocked from lessons 4+)
- ✅ Premium users can access all lessons
- ✅ Data persists across sessions and devices
- ✅ Old localStorage data migrated automatically

---

Last Updated: 2025-11-17

<script lang="ts">
  import { authStore } from '$lib/stores/auth';
  import { userProfile } from '$lib/stores/userProfile';
  import { journal } from '$lib/stores/journal';
  import Card from '$lib/components/Card.svelte';
  import Button from '$lib/components/Button.svelte';
  import Badge from '$lib/components/Badge.svelte';
  import LoadingSpinner from '$lib/components/LoadingSpinner.svelte';
  import ProtectedRoute from '$lib/components/ProtectedRoute.svelte';

  $: user = $authStore.user;
  $: profile = $userProfile;
  $: entries = $journal;

  let displayName = $state('');
  let saving = $state(false);
  let saveMessage = $state('');
  let showDeleteConfirm = $state(false);

  // Initialize display name from profile
  $: if (profile && !displayName) {
    displayName = profile.email.split('@')[0];
  }

  async function handleSaveProfile() {
    if (!profile) return;

    saving = true;
    saveMessage = '';

    try {
      // In a real app, you'd save the display name to the profile
      // For now, just show a success message
      await new Promise(resolve => setTimeout(resolve, 500));
      saveMessage = 'Profile saved successfully!';
      setTimeout(() => saveMessage = '', 3000);
    } catch (error) {
      saveMessage = 'Failed to save profile';
    } finally {
      saving = false;
    }
  }

  function handleExportJournal() {
    if (!entries || entries.length === 0) {
      alert('No journal entries to export');
      return;
    }

    const dataStr = JSON.stringify(entries, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `emerald-journal-${new Date().toISOString().split('T')[0]}.json`;
    link.click();
    URL.revokeObjectURL(url);
  }

  async function handleDeleteAccount() {
    if (!confirm('Are you absolutely sure you want to delete your account? This action cannot be undone.')) {
      showDeleteConfirm = false;
      return;
    }

    if (!confirm('This will permanently delete all your data including journal entries and progress. Type "DELETE" to confirm.')) {
      showDeleteConfirm = false;
      return;
    }

    // In a real app, you'd implement account deletion here
    alert('Account deletion would happen here. Not implemented in this demo.');
    showDeleteConfirm = false;
  }
</script>

<ProtectedRoute>
  <div class="max-w-4xl mx-auto">
    <div class="mb-8">
      <h1 class="text-4xl font-bold text-charcoal mb-2">Settings</h1>
      <p class="text-lg text-charcoal/70">Manage your account and preferences</p>
    </div>

    {#if !profile}
      <div class="flex justify-center py-12">
        <LoadingSpinner size="lg" />
      </div>
    {:else}
      <div class="space-y-6">
        <!-- Account Settings -->
        <Card padding="lg">
          <h2 class="text-2xl font-bold text-charcoal mb-6">Account Settings</h2>

          <div class="space-y-4">
            <div>
              <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
                Email Address
              </label>
              <input
                id="email"
                type="email"
                value={profile.email}
                disabled
                class="w-full px-4 py-2 border border-gray-300 rounded-lg bg-gray-50 text-gray-600 cursor-not-allowed"
              />
              <p class="text-sm text-gray-500 mt-1">Email cannot be changed</p>
            </div>

            <div>
              <label for="displayName" class="block text-sm font-medium text-gray-700 mb-2">
                Display Name
              </label>
              <input
                id="displayName"
                type="text"
                bind:value={displayName}
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald focus:border-emerald"
                placeholder="Enter your display name"
              />
            </div>

            <div class="pt-4">
              <Button onclick={handleSaveProfile} variant="primary" disabled={saving}>
                {saving ? 'Saving...' : 'Save Changes'}
              </Button>
              {#if saveMessage}
                <span class="ml-4 text-sm text-emerald">{saveMessage}</span>
              {/if}
            </div>
          </div>
        </Card>

        <!-- Subscription -->
        <Card padding="lg">
          <h2 class="text-2xl font-bold text-charcoal mb-6">Subscription</h2>

          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <div>
                <h3 class="font-semibold text-charcoal mb-1">Current Plan</h3>
                <p class="text-sm text-gray-600">
                  {profile.tier === 'paid' ? 'Premium - Full access to all features' : 'Free - Limited lesson access'}
                </p>
              </div>
              <Badge
                text={profile.tier === 'paid' ? 'Premium' : 'Free'}
                color={profile.tier === 'paid' ? 'emerald' : 'gray'}
                size="lg"
              />
            </div>

            {#if profile.tier === 'free'}
              <div class="pt-4">
                <Button href="/pricing" variant="primary" size="lg">
                  Upgrade to Premium
                </Button>
                <p class="text-sm text-gray-600 mt-2">
                  Unlock all 250+ lessons and advanced features for $8/month
                </p>
              </div>
            {:else}
              <div class="pt-4">
                <Button href="#" variant="secondary" disabled>
                  Manage Subscription (Coming Soon)
                </Button>
                <p class="text-sm text-gray-600 mt-2">
                  Billing portal integration coming soon
                </p>
              </div>
            {/if}
          </div>
        </Card>

        <!-- Preferences -->
        <Card padding="lg">
          <h2 class="text-2xl font-bold text-charcoal mb-6">Preferences</h2>

          <div class="space-y-4">
            <div class="flex items-center justify-between py-2">
              <div>
                <h3 class="font-semibold text-charcoal mb-1">Email Notifications</h3>
                <p class="text-sm text-gray-600">Receive daily practice reminders</p>
              </div>
              <label class="relative inline-flex items-center cursor-not-allowed">
                <input type="checkbox" class="sr-only peer" disabled />
                <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-emerald/30 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-emerald"></div>
                <span class="ml-3 text-sm text-gray-400">Coming Soon</span>
              </label>
            </div>

            <div class="flex items-center justify-between py-2">
              <div>
                <h3 class="font-semibold text-charcoal mb-1">Daily Reminder Time</h3>
                <p class="text-sm text-gray-600">When to send practice reminders</p>
              </div>
              <select disabled class="px-4 py-2 border border-gray-300 rounded-lg bg-gray-50 text-gray-400 cursor-not-allowed">
                <option>9:00 AM</option>
                <option>12:00 PM</option>
                <option>6:00 PM</option>
              </select>
            </div>

            <div class="flex items-center justify-between py-2">
              <div>
                <h3 class="font-semibold text-charcoal mb-1">Theme</h3>
                <p class="text-sm text-gray-600">Choose your preferred theme</p>
              </div>
              <select disabled class="px-4 py-2 border border-gray-300 rounded-lg bg-gray-50 text-gray-400 cursor-not-allowed">
                <option>Light</option>
                <option>Dark</option>
                <option>Auto</option>
              </select>
            </div>

            <p class="text-sm text-gray-500 italic pt-2">
              Preference controls will be available in a future update
            </p>
          </div>
        </Card>

        <!-- Data & Privacy -->
        <Card padding="lg">
          <h2 class="text-2xl font-bold text-charcoal mb-6">Data & Privacy</h2>

          <div class="space-y-4">
            <div>
              <h3 class="font-semibold text-charcoal mb-2">Export Journal Data</h3>
              <p class="text-sm text-gray-600 mb-3">
                Download all your journal entries as JSON
              </p>
              <Button onclick={handleExportJournal} variant="secondary">
                Export Journal
              </Button>
            </div>

            <div class="pt-6 border-t border-gray-200">
              <h3 class="font-semibold text-red-600 mb-2">Danger Zone</h3>
              <p class="text-sm text-gray-600 mb-3">
                Permanently delete your account and all associated data
              </p>

              {#if !showDeleteConfirm}
                <Button
                  onclick={() => showDeleteConfirm = true}
                  variant="secondary"
                  class="bg-red-50 text-red-600 border-red-300 hover:bg-red-100"
                >
                  Delete Account
                </Button>
              {:else}
                <div class="bg-red-50 border border-red-300 rounded-lg p-4">
                  <p class="text-sm text-red-800 mb-4">
                    <strong>Warning:</strong> This will permanently delete your account, all journal entries,
                    progress, and personal data. This action cannot be undone.
                  </p>
                  <div class="flex gap-3">
                    <Button
                      onclick={handleDeleteAccount}
                      class="bg-red-600 text-white hover:bg-red-700 border-red-700"
                    >
                      Yes, Delete My Account
                    </Button>
                    <Button
                      onclick={() => showDeleteConfirm = false}
                      variant="secondary"
                    >
                      Cancel
                    </Button>
                  </div>
                </div>
              {/if}
            </div>
          </div>
        </Card>

        <!-- Account Info -->
        <Card padding="lg" background="cream">
          <h2 class="text-xl font-semibold text-charcoal mb-4">Account Information</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
            <div>
              <span class="text-gray-600">Member since:</span>
              <span class="font-medium text-charcoal ml-2">
                {new Date(profile.created_at).toLocaleDateString()}
              </span>
            </div>
            <div>
              <span class="text-gray-600">Current streak:</span>
              <span class="font-medium text-charcoal ml-2">
                🔥 {profile.streak_days} days
              </span>
            </div>
            <div>
              <span class="text-gray-600">Lessons completed:</span>
              <span class="font-medium text-charcoal ml-2">
                {profile.lessons_completed.length}
              </span>
            </div>
            <div>
              <span class="text-gray-600">Current grade:</span>
              <span class="font-medium text-charcoal ml-2">
                {profile.current_grade}
              </span>
            </div>
          </div>
        </Card>
      </div>
    {/if}
  </div>
</ProtectedRoute>

<script lang="ts">
  import { authStore } from '$lib/stores/auth';
  import { userProfile } from '$lib/stores/userProfile';
  import { journal } from '$lib/stores/journal';
  import { getCurrentMoonPhase } from '$lib/utils/moonPhase';
  import Card from '$lib/components/Card.svelte';
  import Button from '$lib/components/Button.svelte';
  import Badge from '$lib/components/Badge.svelte';
  import LoadingSpinner from '$lib/components/LoadingSpinner.svelte';
  import ProgressBar from '$lib/components/ProgressBar.svelte';
  import CardOfDay from '$lib/components/CardOfDay.svelte';

  // Reactive subscriptions
  $: user = $authStore.user;
  $: loading = $authStore.loading;
  $: profile = $userProfile;
  $: entries = $journal;

  // Moon phase info
  const moonPhase = getCurrentMoonPhase();

  // Calculate progress percentage
  $: progressPercent = profile ? Math.round((profile.lessons_completed.length / 250) * 100) : 0;

  // Get recent journal entries (last 3)
  $: recentEntries = entries.slice(0, 3);
</script>

{#if loading}
  <div class="flex items-center justify-center min-h-[60vh]">
    <LoadingSpinner size="lg" />
  </div>
{:else if user && profile}
  <!-- Dashboard for logged-in users -->
  <div class="max-w-7xl mx-auto">
    <!-- Welcome Section -->
    <div class="mb-8">
      <h1 class="text-4xl font-bold text-charcoal mb-2">
        Welcome back, {profile.email.split('@')[0]}
      </h1>
      <div class="flex items-center gap-4 text-lg">
        <div class="flex items-center gap-2">
          <span class="text-2xl">🔥</span>
          <span class="font-semibold text-charcoal">{profile.streak_days} day streak</span>
        </div>
        <div class="flex items-center gap-2">
          <Badge text={profile.current_grade} color="gold" size="md" />
        </div>
      </div>
    </div>

    <!-- Today's Practice Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
      <!-- Card of the Day -->
      <CardOfDay />

      <!-- Moon Phase Widget -->
      <Card>
        <div class="space-y-4">
          <div class="flex items-center justify-between">
            <h3 class="text-xl font-semibold text-gray-900">Moon Phase</h3>
            <span class="text-3xl">{moonPhase.emoji}</span>
          </div>

          <div class="text-center py-4">
            <h4 class="text-2xl font-bold text-gray-900 mb-2">{moonPhase.phase}</h4>
            <p class="text-lg text-gray-600 mb-1">{moonPhase.illumination}% illuminated</p>
          </div>

          <div class="bg-indigo-50 rounded-lg p-4">
            <p class="text-sm text-gray-700 leading-relaxed">
              <span class="font-semibold">Magical Timing:</span>
              {moonPhase.magicalTiming}
            </p>
          </div>
        </div>
      </Card>
    </div>

    <!-- Your Progress -->
    <div class="mb-8">
      <Card padding="lg">
        <div class="space-y-4">
          <div class="flex items-center justify-between">
            <h3 class="text-2xl font-bold text-charcoal">Your Progress</h3>
            <Badge text={profile.tier === 'paid' ? 'Premium' : 'Free'} color={profile.tier === 'paid' ? 'emerald' : 'gray'} size="md" />
          </div>

          <div class="space-y-2">
            <div class="flex justify-between text-sm text-gray-600">
              <span>Lessons completed</span>
              <span class="font-semibold">{profile.lessons_completed.length}/250</span>
            </div>
            <ProgressBar progress={progressPercent} />
          </div>

          <div class="flex gap-3 pt-2">
            <Button href="/learn" variant="primary" size="lg">Continue Learning</Button>
            <Button href="/qabalah" variant="secondary" size="lg">Tree of Life</Button>
          </div>
        </div>
      </Card>
    </div>

    <!-- Recent Journal Entries and Quick Actions -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <!-- Recent Journal Entries (2/3 width) -->
      <div class="lg:col-span-2">
        <Card>
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <h3 class="text-xl font-semibold text-gray-900">Recent Journal Entries</h3>
              <Button href="/journal" variant="secondary" size="sm">View All</Button>
            </div>

            {#if recentEntries.length > 0}
              <div class="space-y-3">
                {#each recentEntries as entry}
                  <a href="/journal/{entry.id}" class="block hover:bg-gray-50 rounded-lg p-3 transition-colors border border-gray-200">
                    <div class="flex justify-between items-start mb-2">
                      <h4 class="font-semibold text-charcoal">{entry.title}</h4>
                      <span class="text-xs text-gray-500">{new Date(entry.date).toLocaleDateString()}</span>
                    </div>
                    {#if entry.notes}
                      <p class="text-sm text-gray-600 line-clamp-2">{entry.notes}</p>
                    {/if}
                  </a>
                {/each}
              </div>
            {:else}
              <div class="text-center py-8">
                <p class="text-5xl mb-3">📔</p>
                <p class="text-gray-600 mb-4">No journal entries yet</p>
                <Button href="/journal/new" variant="primary" size="sm">Create Your First Entry</Button>
              </div>
            {/if}
          </div>
        </Card>
      </div>

      <!-- Quick Actions (1/3 width) -->
      <div>
        <Card>
          <div class="space-y-4">
            <h3 class="text-xl font-semibold text-gray-900">Quick Actions</h3>

            <div class="space-y-2">
              <Button href="/journal/new" variant="primary" size="md" fullWidth>
                📝 Record a Reading
              </Button>
              <Button href="/learn" variant="secondary" size="md" fullWidth>
                📚 Continue Lesson
              </Button>
              <Button href="/qabalah" variant="secondary" size="md" fullWidth>
                🌳 Tree of Life
              </Button>
              <Button href="/cards" variant="secondary" size="md" fullWidth>
                🃏 Browse Cards
              </Button>
            </div>
          </div>
        </Card>
      </div>
    </div>
  </div>
{:else}
  <!-- Landing Page for logged-out users -->
  <div class="max-w-7xl mx-auto">
    <!-- Hero Section -->
    <div class="text-center mb-16 pt-8">
      <h1 class="text-5xl md:text-6xl font-bold text-charcoal mb-6 leading-tight">
        Learn the System,<br />Not Just the Cards
      </h1>
      <p class="text-xl md:text-2xl text-charcoal/70 mb-8 max-w-3xl mx-auto">
        Master Tarot, Qabalah, and Astrology through the Western Hermetic tradition
      </p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <Button href="/signup" variant="primary" size="lg">Start Free</Button>
        <Button href="#features" variant="secondary" size="lg">Learn More</Button>
      </div>

      <!-- Visual placeholder - Tree of Life -->
      <div class="mt-12 mb-8">
        <div class="inline-block bg-gradient-to-br from-emerald-100 to-gold-100 rounded-2xl p-12 shadow-lg">
          <div class="text-8xl">🌳</div>
          <p class="text-sm text-charcoal/60 mt-4">Tree of Life</p>
        </div>
      </div>
    </div>

    <!-- Features Section -->
    <div id="features" class="mb-16">
      <h2 class="text-3xl font-bold text-charcoal text-center mb-12">Everything You Need to Master the Tradition</h2>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Feature 1 -->
        <Card padding="lg">
          <div class="text-center space-y-4">
            <div class="text-5xl mb-4">📚</div>
            <h3 class="text-2xl font-bold text-charcoal">Comprehensive Reference</h3>
            <div class="text-left text-charcoal/70 space-y-2">
              <p>• Complete tarot correspondence database</p>
              <p>• Qabalah Tree of Life</p>
              <p>• Astrological associations</p>
              <p>• Cross-reference any card</p>
            </div>
          </div>
        </Card>

        <!-- Feature 2 -->
        <Card padding="lg">
          <div class="text-center space-y-4">
            <div class="text-5xl mb-4">📖</div>
            <h3 class="text-2xl font-bold text-charcoal">Structured Curriculum</h3>
            <div class="text-left text-charcoal/70 space-y-2">
              <p>• Progress through Golden Dawn grades</p>
              <p>• Daily lessons with quizzes</p>
              <p>• Ascending the Tree of Life</p>
              <p>• Learn the system, not just meanings</p>
            </div>
          </div>
        </Card>

        <!-- Feature 3 -->
        <Card padding="lg">
          <div class="text-center space-y-4">
            <div class="text-5xl mb-4">📔</div>
            <h3 class="text-2xl font-bold text-charcoal">Practice Journal</h3>
            <div class="text-left text-charcoal/70 space-y-2">
              <p>• Track readings and dreams</p>
              <p>• Auto-capture moon phases</p>
              <p>• Pattern analysis over time</p>
              <p>• Cross-device sync</p>
            </div>
          </div>
        </Card>
      </div>
    </div>

    <!-- How It Works -->
    <div class="mb-16">
      <h2 class="text-3xl font-bold text-charcoal text-center mb-12">How It Works</h2>

      <Card padding="lg" background="cream">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div class="text-center">
            <div class="text-3xl font-bold text-emerald mb-2">1</div>
            <h4 class="font-semibold text-charcoal mb-2">Start Free</h4>
            <p class="text-sm text-charcoal/70">Begin with Neophyte lessons</p>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-emerald mb-2">2</div>
            <h4 class="font-semibold text-charcoal mb-2">Explore</h4>
            <p class="text-sm text-charcoal/70">Browse the correspondence database</p>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-emerald mb-2">3</div>
            <h4 class="font-semibold text-charcoal mb-2">Practice</h4>
            <p class="text-sm text-charcoal/70">Journal your readings</p>
          </div>
          <div class="text-center">
            <div class="text-3xl font-bold text-emerald mb-2">4</div>
            <h4 class="font-semibold text-charcoal mb-2">Ascend</h4>
            <p class="text-sm text-charcoal/70">Progress through the grades</p>
          </div>
        </div>
      </Card>
    </div>

    <!-- Pricing Teaser -->
    <div class="mb-16">
      <Card padding="lg" border="gold">
        <div class="text-center space-y-4">
          <h2 class="text-3xl font-bold text-charcoal">Start Free, Upgrade When Ready</h2>
          <p class="text-xl text-charcoal/70">
            Access core features free forever. Unlock the complete curriculum for $8/month.
          </p>
          <div class="pt-4">
            <Button href="/pricing" variant="primary" size="lg">View Pricing</Button>
          </div>
        </div>
      </Card>
    </div>

    <!-- Footer CTA -->
    <div class="text-center py-12 border-t border-charcoal/10">
      <p class="text-charcoal/60 mb-6">
        Built with 🖤 for the esoteric community
      </p>
      <div class="flex justify-center gap-6 text-sm">
        <a href="/about" class="text-emerald hover:underline">About Emerald</a>
        <a href="/pricing" class="text-emerald hover:underline">Pricing</a>
        <a href="https://github.com/astrid-selin/Project-Emerald" class="text-emerald hover:underline" target="_blank" rel="noopener noreferrer">GitHub</a>
      </div>
    </div>
  </div>
{/if}

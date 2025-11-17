<script lang="ts">
  import Card from '$lib/components/Card.svelte';
  import Button from '$lib/components/Button.svelte';
</script>

<div class="max-w-4xl mx-auto">
  <!-- Header -->
  <div class="text-center mb-12">
    <div class="text-6xl mb-4">✨</div>
    <h1 class="text-5xl font-bold text-charcoal mb-4">About Emerald</h1>
    <p class="text-xl text-charcoal/70">
      Making Western esotericism accessible to modern seekers
    </p>
  </div>

  <!-- Main Content -->
  <div class="prose prose-lg max-w-none space-y-8">
    <!-- What is Emerald -->
    <Card padding="lg">
      <h2 class="text-3xl font-bold text-charcoal mb-4">What is Emerald?</h2>
      <p class="text-gray-700 leading-relaxed mb-4">
        Emerald is a comprehensive learning platform for the Western esoteric tradition, with a focus
        on the interconnected systems of Tarot, Qabalah, and Astrology as taught by the Hermetic Order
        of the Golden Dawn.
      </p>
      <p class="text-gray-700 leading-relaxed">
        Unlike apps that simply list card meanings, Emerald teaches you the underlying system—the
        architecture of correspondences that connects the Tree of Life, the Zodiac, the planets, and
        the 78 cards of the Tarot into a unified framework for understanding reality and consciousness.
      </p>
    </Card>

    <!-- The Approach -->
    <Card padding="lg" background="cream">
      <h2 class="text-3xl font-bold text-charcoal mb-4">The Approach</h2>

      <h3 class="text-xl font-semibold text-charcoal mb-3">Based on Golden Dawn Tradition</h3>
      <p class="text-gray-700 leading-relaxed mb-4">
        Our curriculum follows the grade structure of the Hermetic Order of the Golden Dawn, one of the
        most influential magical orders in Western esotericism. You'll progress through the grades,
        ascending the Tree of Life from Malkuth to Kether, learning the correspondences associated
        with each sephirah.
      </p>

      <h3 class="text-xl font-semibold text-charcoal mb-3">Teach the System, Not Just Facts</h3>
      <p class="text-gray-700 leading-relaxed mb-4">
        We don't just give you a list of correspondences to memorize. Each lesson explains <em>why</em>
        the connections exist—why The Emperor is associated with Aries, why The Moon corresponds to
        the 29th Path between Netzach and Malkuth, why certain cards relate to specific astrological
        decans.
      </p>

      <h3 class="text-xl font-semibold text-charcoal mb-3">Structured Learning Path</h3>
      <p class="text-gray-700 leading-relaxed">
        Starting as a Neophyte (0°=0°), you'll work through 250+ lessons organized by grade and topic.
        Each lesson includes interactive quizzes to reinforce your understanding. The curriculum is
        carefully sequenced to build knowledge progressively, ensuring you have a solid foundation
        before moving to advanced topics.
      </p>
    </Card>

    <!-- What You'll Learn -->
    <Card padding="lg">
      <h2 class="text-3xl font-bold text-charcoal mb-4">What You'll Learn</h2>

      <div class="space-y-4">
        <div>
          <h3 class="text-xl font-semibold text-charcoal mb-2">🌳 The Tree of Life</h3>
          <p class="text-gray-700 leading-relaxed">
            The fundamental structure of Qabalistic philosophy—the ten sephiroth and twenty-two paths,
            their meanings, attributions, and relationships.
          </p>
        </div>

        <div>
          <h3 class="text-xl font-semibold text-charcoal mb-2">🃏 Tarot Correspondences</h3>
          <p class="text-gray-700 leading-relaxed">
            How the 22 Major Arcana map to the paths of the Tree, and how the 56 Minor Arcana relate
            to the four elements, the zodiac, and the astrological decans.
          </p>
        </div>

        <div>
          <h3 class="text-xl font-semibold text-charcoal mb-2">⭐ Astrological Associations</h3>
          <p class="text-gray-700 leading-relaxed">
            The connections between planets, zodiac signs, and the Tarot. Why Saturn rules The World,
            why Mars governs The Tower, and how the decans structure the Minor Arcana.
          </p>
        </div>

        <div>
          <h3 class="text-xl font-semibold text-charcoal mb-2">🔮 How Everything Connects</h3>
          <p class="text-gray-700 leading-relaxed">
            The web of correspondences that unifies these systems—colors, Hebrew letters, elements,
            numbers, and more. You'll understand how to navigate the entire system with confidence.
          </p>
        </div>
      </div>
    </Card>

    <!-- Who Is This For -->
    <Card padding="lg" background="cream">
      <h2 class="text-3xl font-bold text-charcoal mb-4">Who Is This For?</h2>

      <div class="space-y-3">
        <div class="flex items-start gap-3">
          <span class="text-2xl">🌱</span>
          <div>
            <h3 class="font-semibold text-charcoal mb-1">Curious Beginners</h3>
            <p class="text-gray-700">
              You've seen tarot cards and want to understand what they really mean, beyond simple fortune-telling.
            </p>
          </div>
        </div>

        <div class="flex items-start gap-3">
          <span class="text-2xl">🔍</span>
          <div>
            <h3 class="font-semibold text-charcoal mb-1">Practicing Tarot Readers</h3>
            <p class="text-gray-700">
              You know the basic meanings but want to deepen your understanding of the esoteric structure behind them.
            </p>
          </div>
        </div>

        <div class="flex items-start gap-3">
          <span class="text-2xl">📚</span>
          <div>
            <h3 class="font-semibold text-charcoal mb-1">Students of Western Esotericism</h3>
            <p class="text-gray-700">
              You're studying Qabalah, ceremonial magic, or Hermetic philosophy and want a structured curriculum.
            </p>
          </div>
        </div>

        <div class="flex items-start gap-3">
          <span class="text-2xl">⚡</span>
          <div>
            <h3 class="font-semibold text-charcoal mb-1">System Thinkers</h3>
            <p class="text-gray-700">
              You love understanding how complex systems fit together and want to explore one of the most intricate
              symbolic systems ever created.
            </p>
          </div>
        </div>
      </div>
    </Card>

    <!-- Open Source -->
    <Card padding="lg">
      <h2 class="text-3xl font-bold text-charcoal mb-4">Open Source & Community</h2>

      <p class="text-gray-700 leading-relaxed mb-4">
        Emerald is open source and built in the open. We believe esoteric knowledge should be accessible
        to everyone, not locked behind proprietary systems. The entire codebase is available on GitHub,
        and we welcome contributions from the community.
      </p>

      <p class="text-gray-700 leading-relaxed mb-4">
        Built with modern web technologies: SvelteKit, TypeScript, Tailwind CSS, Firebase, and Python.
        The curriculum content is stored in structured formats that can be extended and improved by the
        community.
      </p>

      <div class="pt-4">
        <Button
          href="https://github.com/astrid-selin/Project-Emerald"
          variant="secondary"
          target="_blank"
        >
          View on GitHub
        </Button>
      </div>
    </Card>

    <!-- Credits -->
    <Card padding="lg" border="gold">
      <h2 class="text-3xl font-bold text-charcoal mb-4">Standing on the Shoulders of Giants</h2>

      <p class="text-gray-700 leading-relaxed mb-4">
        This work draws heavily on the writings and teachings of the masters of Western esotericism:
      </p>

      <ul class="list-disc list-inside space-y-2 text-gray-700 mb-4">
        <li><strong>Arthur Edward Waite</strong> — The Pictorial Key to the Tarot</li>
        <li><strong>Aleister Crowley</strong> — The Book of Thoth</li>
        <li><strong>Paul Foster Case</strong> — The Tarot: A Key to the Wisdom of the Ages</li>
        <li><strong>Israel Regardie</strong> — The Golden Dawn</li>
        <li><strong>Dion Fortune</strong> — The Mystical Qabalah</li>
        <li><strong>S.L. MacGregor Mathers</strong> — The Kabbalah Unveiled</li>
      </ul>

      <p class="text-gray-700 leading-relaxed italic">
        We are deeply grateful to these teachers for preserving and transmitting this knowledge.
        Emerald is our humble attempt to make their wisdom accessible to a new generation of seekers.
      </p>
    </Card>

    <!-- CTA -->
    <div class="text-center py-12">
      <h2 class="text-3xl font-bold text-charcoal mb-4">Ready to Begin Your Journey?</h2>
      <p class="text-lg text-charcoal/70 mb-6">
        Start your studies as a Neophyte and ascend the Tree of Life
      </p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <Button href="/signup" variant="primary" size="lg">Start Free</Button>
        <Button href="/pricing" variant="secondary" size="lg">View Pricing</Button>
      </div>
    </div>
  </div>
</div>

<style>
  /* Add line-clamp utility if not available */
  .line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
</style>

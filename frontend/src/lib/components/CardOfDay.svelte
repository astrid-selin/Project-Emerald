<script lang="ts">
  import { getCardOfDay, getCardOfDayMeaning, getCardName } from '$lib/utils/cardOfDay';
  import Card from './Card.svelte';
  import Button from './Button.svelte';

  const cardNumber = getCardOfDay();
  const cardName = getCardName(cardNumber);
  const meaning = getCardOfDayMeaning(cardNumber);

  export let showActions = true;
</script>

<Card>
  <div class="space-y-4">
    <div class="flex items-center justify-between">
      <h3 class="text-xl font-semibold text-gray-900">Card of the Day</h3>
      <span class="text-2xl">🃏</span>
    </div>

    <div class="text-center py-6">
      <!-- Card visual placeholder - in a real app, you'd show the actual card image -->
      <div class="inline-block bg-gradient-to-br from-purple-600 to-indigo-600 text-white rounded-lg p-8 mb-4 shadow-lg">
        <div class="text-6xl mb-2">✨</div>
        <div class="text-sm uppercase tracking-wide opacity-90">Major Arcana</div>
      </div>

      <h4 class="text-2xl font-bold text-gray-900 mb-2">{cardName}</h4>
      <p class="text-sm text-gray-500 mb-4">Card {cardNumber}</p>
    </div>

    <div class="bg-purple-50 rounded-lg p-4">
      <p class="text-gray-700 text-sm leading-relaxed italic">
        {meaning}
      </p>
    </div>

    {#if showActions}
      <div class="flex gap-2 pt-2">
        <Button href="/cards/{cardNumber}" variant="secondary" size="sm" fullWidth>
          View Card Details
        </Button>
        <Button href="/journal/new?card={cardNumber}" variant="primary" size="sm" fullWidth>
          Add to Journal
        </Button>
      </div>
    {/if}
  </div>
</Card>

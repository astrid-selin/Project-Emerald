<script lang="ts">
  import { page } from '$app/stores';
  import { getCardOfDay, getCardName } from '$lib/utils/cardOfDay';
  import Card from '$lib/components/Card.svelte';
  import Button from '$lib/components/Button.svelte';

  $: error = $page.error;
  $: status = $page.status;

  // Get a random card based on the error code
  const cardNumber = status ? status % 22 : getCardOfDay();
  const cardName = getCardName(cardNumber);

  const errorMessages: Record<number, string> = {
    404: "This page has wandered off the path, like The Fool seeking new adventures.",
    403: "Access forbidden. Some mysteries require initiation.",
    500: "The Tower moment—something has collapsed on the server.",
    503: "The Hanged Man—the server is in suspended animation."
  };

  const defaultMessage = "An unexpected card has been drawn.";
  const message = status ? errorMessages[status] || defaultMessage : defaultMessage;
</script>

<svelte:head>
  <title>{status || 'Error'} - Emerald</title>
</svelte:head>

<div class="min-h-[60vh] flex items-center justify-center px-4">
  <div class="max-w-2xl mx-auto text-center">
    <Card padding="lg">
      <!-- Error Code -->
      <div class="mb-6">
        <h1 class="text-8xl font-bold text-charcoal/20 mb-2">
          {status || '???'}
        </h1>
        <h2 class="text-3xl font-bold text-charcoal mb-4">
          {status === 404 ? 'Page Not Found' : 'Oops! Something Went Wrong'}
        </h2>
      </div>

      <!-- Card of Error -->
      <div class="mb-8">
        <div class="inline-block bg-gradient-to-br from-purple-600 to-indigo-600 text-white rounded-lg p-6 mb-4 shadow-lg">
          <div class="text-5xl mb-2">✨</div>
          <div class="text-sm uppercase tracking-wide opacity-90">Card {cardNumber}</div>
        </div>
        <h3 class="text-xl font-bold text-charcoal mb-2">{cardName}</h3>
      </div>

      <!-- Error Message -->
      <p class="text-lg text-charcoal/70 mb-8 italic">
        {message}
      </p>

      {#if error?.message}
        <div class="bg-red-50 border border-red-200 rounded-lg p-4 mb-8">
          <p class="text-sm text-red-800 font-mono">
            {error.message}
          </p>
        </div>
      {/if}

      <!-- Actions -->
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <Button href="/" variant="primary" size="lg">
          Return Home
        </Button>
        <Button href="/learn" variant="secondary" size="lg">
          Continue Learning
        </Button>
      </div>

      <!-- Helpful Links -->
      <div class="mt-8 pt-6 border-t border-gray-200">
        <p class="text-sm text-gray-600 mb-3">Looking for something specific?</p>
        <div class="flex flex-wrap justify-center gap-4 text-sm">
          <a href="/cards" class="text-emerald hover:underline">Browse Cards</a>
          <a href="/qabalah" class="text-emerald hover:underline">Tree of Life</a>
          <a href="/journal" class="text-emerald hover:underline">Journal</a>
          <a href="/about" class="text-emerald hover:underline">About</a>
        </div>
      </div>
    </Card>
  </div>
</div>

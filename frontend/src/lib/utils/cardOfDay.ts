/**
 * Card of the Day utility functions
 * Generates a consistent daily card based on the current date
 */

export function getCardOfDay(): number {
  // Generate consistent card for today's date
  const today = new Date();
  const dayOfYear = Math.floor(
    (today.getTime() - new Date(today.getFullYear(), 0, 0).getTime()) / 86400000
  );

  // Use date as seed for consistent daily card
  // Only Major Arcana (0-21)
  return dayOfYear % 22;
}

export function getCardOfDayMeaning(cardNumber: number): string {
  const meanings: Record<number, string> = {
    0: "New beginnings and infinite potential await you today. The Fool invites you to take a leap of faith.",
    1: "Focus your will and take conscious action. Channel your inner power with intention.",
    2: "Trust your intuition and inner wisdom. The High Priestess reveals hidden knowledge.",
    3: "Nurture your creative projects. The Empress brings abundance and growth.",
    4: "Establish structure and authority in your endeavors. Build solid foundations.",
    5: "Seek wisdom from tradition and teaching. The Hierophant brings spiritual guidance.",
    6: "Make choices aligned with your values. The Lovers remind you of harmony and union.",
    7: "Move forward with determination and willpower. Victory comes through focused effort.",
    8: "Seek balance and justice in all matters. Act with fairness and integrity.",
    9: "Take time for introspection and inner guidance. The Hermit illuminates the path within.",
    10: "Embrace the cycles of change and fortune. What goes around comes around.",
    11: "Cultivate inner strength and courage. Gentle power overcomes all obstacles.",
    12: "Shift your perspective and let go. The Hanged Man brings enlightenment through surrender.",
    13: "Welcome transformation and new beginnings. Death brings necessary endings and rebirth.",
    14: "Practice moderation and balance. Temperance brings harmony through integration.",
    15: "Examine what binds you. The Devil reveals illusions and material attachments.",
    16: "Prepare for sudden change and revelation. The Tower breaks down false structures.",
    17: "Hope and inspiration shine upon you. The Star brings healing and renewal.",
    18: "Trust your dreams and navigate uncertainty. The Moon reveals what lies beneath.",
    19: "Step into clarity and success. The Sun brings joy, vitality, and achievement.",
    20: "Reflect on your journey and heed the call to awakening. Judgement brings renewal.",
    21: "Completion and integration - celebrate your progress. The World brings fulfillment and wholeness."
  };

  return meanings[cardNumber] || "Reflect on the wisdom of this card.";
}

export function getCardName(cardNumber: number): string {
  const names: Record<number, string> = {
    0: "The Fool",
    1: "The Magician",
    2: "The High Priestess",
    3: "The Empress",
    4: "The Emperor",
    5: "The Hierophant",
    6: "The Lovers",
    7: "The Chariot",
    8: "Justice",
    9: "The Hermit",
    10: "Wheel of Fortune",
    11: "Strength",
    12: "The Hanged Man",
    13: "Death",
    14: "Temperance",
    15: "The Devil",
    16: "The Tower",
    17: "The Star",
    18: "The Moon",
    19: "The Sun",
    20: "Judgement",
    21: "The World"
  };

  return names[cardNumber] || `Card ${cardNumber}`;
}

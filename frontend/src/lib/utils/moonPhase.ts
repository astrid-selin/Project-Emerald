/**
 * Moon phase utility functions
 * Calculates current moon phase and provides magical timing information
 */

export interface MoonPhaseInfo {
  phase: string;
  emoji: string;
  illumination: number;
  magicalTiming: string;
}

export function getCurrentMoonPhase(): MoonPhaseInfo {
  const now = new Date();

  // Known new moon (January 11, 2024)
  const knownNewMoon = new Date('2024-01-11T11:57:00Z').getTime();
  const lunarCycle = 29.53059 * 24 * 60 * 60 * 1000; // in milliseconds

  // Calculate days since known new moon
  const timeSinceNewMoon = now.getTime() - knownNewMoon;
  const daysSinceNewMoon = (timeSinceNewMoon % lunarCycle) / (24 * 60 * 60 * 1000);

  // Calculate illumination (0-100%)
  const illumination = Math.round((1 - Math.cos((daysSinceNewMoon / 29.53059) * 2 * Math.PI)) * 50);

  // Determine phase and return info
  if (daysSinceNewMoon < 1.84566) {
    return {
      phase: "New Moon",
      emoji: "🌑",
      illumination,
      magicalTiming: "Perfect for new beginnings, setting intentions, and planting seeds"
    };
  } else if (daysSinceNewMoon < 7.38264) {
    return {
      phase: "Waxing Crescent",
      emoji: "🌒",
      illumination,
      magicalTiming: "Good for growth, attraction, and building momentum"
    };
  } else if (daysSinceNewMoon < 9.22830) {
    return {
      phase: "First Quarter",
      emoji: "🌓",
      illumination,
      magicalTiming: "Time for action, decision-making, and overcoming obstacles"
    };
  } else if (daysSinceNewMoon < 14.76529) {
    return {
      phase: "Waxing Gibbous",
      emoji: "🌔",
      illumination,
      magicalTiming: "Excellent for refinement, editing, and perfecting your work"
    };
  } else if (daysSinceNewMoon < 16.61095) {
    return {
      phase: "Full Moon",
      emoji: "🌕",
      illumination,
      magicalTiming: "Peak power for manifestation, celebration, and gratitude"
    };
  } else if (daysSinceNewMoon < 22.14793) {
    return {
      phase: "Waning Gibbous",
      emoji: "🌖",
      illumination,
      magicalTiming: "Good for sharing wisdom, teaching, and reflection"
    };
  } else if (daysSinceNewMoon < 23.99359) {
    return {
      phase: "Last Quarter",
      emoji: "🌗",
      illumination,
      magicalTiming: "Time for release, letting go, and forgiveness"
    };
  } else {
    return {
      phase: "Waning Crescent",
      emoji: "🌘",
      illumination,
      magicalTiming: "Perfect for rest, retreat, and inner work"
    };
  }
}

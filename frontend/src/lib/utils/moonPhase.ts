import type { MoonPhase } from '$lib/types';

export function getCurrentMoonPhase(): MoonPhase {
	// Calculate moon phase based on current date
	// Simple algorithm:
	const date = new Date();

	// Known new moon: Jan 11, 2024
	const knownNewMoon = new Date(2024, 0, 11);
	const synodicMonth = 29.53058867; // days

	const diff = (date.getTime() - knownNewMoon.getTime()) / (1000 * 60 * 60 * 24);
	const phase = (diff % synodicMonth) / synodicMonth;

	const phases = [
		{ name: 'New Moon', emoji: '🌑', min: 0, max: 0.03 },
		{ name: 'Waxing Crescent', emoji: '🌒', min: 0.03, max: 0.22 },
		{ name: 'First Quarter', emoji: '🌓', min: 0.22, max: 0.28 },
		{ name: 'Waxing Gibbous', emoji: '🌔', min: 0.28, max: 0.47 },
		{ name: 'Full Moon', emoji: '🌕', min: 0.47, max: 0.53 },
		{ name: 'Waning Gibbous', emoji: '🌖', min: 0.53, max: 0.72 },
		{ name: 'Last Quarter', emoji: '🌗', min: 0.72, max: 0.78 },
		{ name: 'Waning Crescent', emoji: '🌘', min: 0.78, max: 0.97 },
		{ name: 'New Moon', emoji: '🌑', min: 0.97, max: 1 }
	];

	const currentPhase = phases.find((p) => phase >= p.min && phase < p.max) || phases[0];

	return {
		phase: currentPhase.name,
		illumination: Math.round(phase * 100),
		emoji: currentPhase.emoji
	};
}

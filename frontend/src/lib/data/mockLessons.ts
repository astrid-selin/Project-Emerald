import type { Lesson } from '$lib/types';

export const mockLessons: Lesson[] = [
	{
		id: 'neophyte_01',
		title: 'Introduction to the Four Elements',
		grade: '0°=0°',
		grade_name: 'Neophyte',
		sephirah_context: 'Malkuth',
		order: 1,
		estimated_time: 15,
		content: {
			theory: `The four classical elements - Fire, Water, Air, and Earth - form the foundation of Western esoteric thought. These aren't physical elements, but archetypal forces that describe different qualities of energy and manifestation.

**Fire** represents will, passion, and transformation. In tarot, Fire corresponds to the suit of Wands.

**Water** represents emotion, intuition, and the unconscious. In tarot, Water corresponds to the suit of Cups.

**Air** represents intellect, communication, and ideas. In tarot, Air corresponds to the suit of Swords.

**Earth** represents physical reality, stability, and manifestation. In tarot, Earth corresponds to the suit of Pentacles.

Each element has its own qualities, but they work together in dynamic balance. Understanding these elements is the first step in understanding the tarot's symbolic language.`,

			practice: `Take a moment to observe your environment. Can you identify each element?

- **Fire**: Sunlight, heat, electricity, your own energy
- **Water**: Any liquids, emotions you're feeling, flow and adaptation
- **Air**: Your breath, thoughts, sounds, movement of air
- **Earth**: Solid objects, your physical body, structure around you

Spend 5-10 minutes journaling about which element you feel most connected to today and why.`,

			meditation: `Close your eyes and imagine standing at the center of a crossroads. To your south burns a warm fire. To your west flows a calm stream. To your east blows a gentle breeze. To your north stands a solid mountain. Feel the balance of all four elements surrounding you.`,

			references: [
				'Israel Regardie, The Golden Dawn, Book 1',
				'Paul Foster Case, The Tarot: A Key to the Wisdom of the Ages'
			]
		},
		quiz: [
			{
				question: 'Which tarot suit corresponds to the Fire element?',
				answers: ['Wands', 'Cups', 'Swords', 'Pentacles'],
				correct: 0,
				explanation: 'Wands represent Fire - will, passion, and creative energy.'
			},
			{
				question: 'What does the Water element represent?',
				answers: [
					'Intellect and communication',
					'Emotion and intuition',
					'Physical reality',
					'Willpower'
				],
				correct: 1,
				explanation:
					'Water represents the emotional, intuitive, and unconscious aspects of experience.'
			},
			{
				question: 'Which element corresponds to the suit of Swords?',
				answers: ['Fire', 'Water', 'Air', 'Earth'],
				correct: 2,
				explanation: 'Air corresponds to Swords, representing the mind, intellect, and communication.'
			}
		],
		unlocks_after_days: 0,
		is_free: true
	},
	{
		id: 'neophyte_02',
		title: 'The Ten Sephiroth: An Overview',
		grade: '0°=0°',
		grade_name: 'Neophyte',
		sephirah_context: 'Malkuth',
		order: 2,
		estimated_time: 20,
		content: {
			theory: `The Tree of Life consists of ten spheres called Sephiroth (singular: Sephirah), each representing a different aspect of divine emanation and human consciousness.

From top to bottom, they are:

1. **Kether** (Crown) - Pure consciousness, the source
2. **Chokmah** (Wisdom) - Dynamic, creative force
3. **Binah** (Understanding) - Form-giving, receptive
4. **Chesed** (Mercy) - Expansion, benevolence
5. **Geburah** (Severity) - Restriction, discipline
6. **Tiphareth** (Beauty) - Harmony, balance, the central sun
7. **Netzach** (Victory) - Emotion, desire, nature
8. **Hod** (Glory) - Intellect, form, pattern
9. **Yesod** (Foundation) - Subconscious, dreams, astral
10. **Malkuth** (Kingdom) - Physical reality, where we begin

Each Sephirah has correspondences to planets, tarot cards, colors, and spiritual experiences. We'll explore each one in depth as you progress through the grades.`,

			practice: `Visit the Tree of Life visualization in the app (Qabalah section). Click on each Sephirah and read its basic information. Try to memorize the names and numbers of all ten Sephiroth. Write them down from memory.`,

			meditation: `Visualize a column of light descending from above your head (Kether) down through your body to your feet (Malkuth). Feel the energy flowing through each center. This is the Middle Pillar of the Tree within you.`,

			references: [
				'Dion Fortune, The Mystical Qabalah',
				'Gareth Knight, A Practical Guide to Qabalistic Symbolism'
			]
		},
		quiz: [
			{
				question: 'Which Sephirah is at the top of the Tree of Life?',
				answers: ['Malkuth', 'Tiphareth', 'Kether', 'Chokmah'],
				correct: 2,
				explanation: 'Kether, meaning Crown, is the highest Sephirah representing pure consciousness.'
			},
			{
				question: 'What does Tiphareth represent?',
				answers: [
					'Physical reality',
					'Harmony and balance',
					'Pure intellect',
					'Creative force'
				],
				correct: 1,
				explanation:
					'Tiphareth, the central Sephirah, represents harmony, balance, and is associated with the Sun.'
			},
			{
				question: 'Which Sephirah represents the physical world where we begin?',
				answers: ['Kether', 'Yesod', 'Malkuth', 'Hod'],
				correct: 2,
				explanation:
					'Malkuth, the Kingdom, represents physical reality and earthly existence - our starting point.'
			}
		],
		unlocks_after_days: 1,
		is_free: true
	},
	{
		id: 'neophyte_03',
		title: "Major Arcana: The Fool's Journey",
		grade: '0°=0°',
		grade_name: 'Neophyte',
		sephirah_context: 'Malkuth',
		order: 3,
		estimated_time: 25,
		content: {
			theory: `The 22 Major Arcana cards represent the Fool's Journey - a symbolic passage through life's major lessons and spiritual development.

The Fool (0) begins as pure potential, innocent and open to experience. Through encounters with archetypal figures and situations (The Magician, High Priestess, etc.), the Fool learns, grows, and is transformed.

The journey ends with The World (21), representing completion, integration, and cosmic consciousness.

Each Major Arcana card corresponds to one of the 22 paths on the Tree of Life, connecting the Sephiroth. This means every card represents not just an archetype, but a specific spiritual journey between two states of consciousness.

For example:
- **The Fool** walks the path from Kether (Crown) to Chokmah (Wisdom)
- **The Magician** walks from Kether to Binah (Understanding)
- **Death** walks from Netzach (Victory) to Tiphareth (Beauty)

We'll explore each card in detail in future lessons.`,

			practice: `Draw or look at each of the 22 Major Arcana cards in order (0-21). Can you identify a story? What is the Fool learning at each stage? Write a brief journal entry describing your own "Fool's Journey" through a recent life challenge.`,

			meditation: `Imagine yourself as the Fool, standing at the edge of a cliff with unlimited potential before you. What step will you take? Where does your journey lead?`,

			references: [
				'Rachel Pollack, Seventy-Eight Degrees of Wisdom',
				'Arthur Edward Waite, The Pictorial Key to the Tarot'
			]
		},
		quiz: [
			{
				question: 'How many Major Arcana cards are there?',
				answers: ['21', '22', '23', '78'],
				correct: 1,
				explanation:
					'There are 22 Major Arcana cards, numbered 0-21, corresponding to the 22 paths on the Tree of Life.'
			},
			{
				question: 'What does The Fool (0) represent?',
				answers: [
					'Completion and mastery',
					'Pure potential and innocence',
					'Hidden knowledge',
					'Material success'
				],
				correct: 1,
				explanation:
					'The Fool represents pure potential, innocence, and the beginning of the spiritual journey.'
			},
			{
				question: 'Each Major Arcana card corresponds to:',
				answers: [
					'A planet',
					'A Sephirah',
					'A path on the Tree of Life',
					'An element'
				],
				correct: 2,
				explanation:
					'Each of the 22 Major Arcana corresponds to one of the 22 paths connecting the Sephiroth on the Tree of Life.'
			}
		],
		unlocks_after_days: 2,
		is_free: true
	}
];

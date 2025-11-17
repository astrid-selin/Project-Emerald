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
	},
	{
		id: 'neophyte_04',
		title: 'The Minor Arcana: Court Cards',
		grade: '0°=0°',
		grade_name: 'Neophyte',
		sephirah_context: 'Malkuth',
		order: 4,
		estimated_time: 30,
		content: {
			theory: `The Court Cards - Page, Knight, Queen, and King - represent people, personality types, and stages of mastery in each element.

**Pages** represent the student, the beginner, youthful energy, and messages. They are learning their element.

**Knights** represent action, movement, and the element in its most active form. They take the Page's lessons and put them into motion.

**Queens** represent mastery of the inner, receptive aspect of their element. They embody emotional and spiritual maturity.

**Kings** represent mastery of the outer, active aspect of their element. They embody worldly power and authority.

Each court card combines its rank with its suit's element:
- Page of Wands: Enthusiastic beginner in creative pursuits
- Knight of Cups: Romantic, emotional action
- Queen of Swords: Intellectual and perceptive wisdom
- King of Pentacles: Material success and practical mastery`,

			practice: `Choose one court card from each suit. Study their imagery. Can you identify the Page, Knight, Queen, or King energy in people you know? In yourself? Journal about which court card you feel most aligned with today.`,

			meditation: `Visualize yourself progressing through the four stages: Page (learning), Knight (doing), Queen (being), King (mastering). What stage are you at in different areas of your life?`,

			references: [
				'Mary K. Greer, Understanding the Tarot Court',
				'Rachel Pollack, Seventy-Eight Degrees of Wisdom'
			]
		},
		quiz: [
			{
				question: 'Which court card represents the beginner or student?',
				answers: ['Page', 'Knight', 'Queen', 'King'],
				correct: 0,
				explanation: 'The Page represents the student, beginner, and learning phase of each element.'
			},
			{
				question: 'What does the Knight represent?',
				answers: [
					'Mastery and authority',
					'Learning and messages',
					'Action and movement',
					'Emotional wisdom'
				],
				correct: 2,
				explanation: 'Knights represent action, movement, and the element in its most dynamic form.'
			},
			{
				question: 'Which court card embodies mature inner mastery?',
				answers: ['Page', 'Knight', 'Queen', 'King'],
				correct: 2,
				explanation: 'The Queen represents mastery of the inner, receptive aspect of the element.'
			}
		],
		unlocks_after_days: 3,
		is_free: false
	},
	{
		id: 'neophyte_05',
		title: 'The Minor Arcana: Numbered Cards',
		grade: '0°=0°',
		grade_name: 'Neophyte',
		sephirah_context: 'Malkuth',
		order: 5,
		estimated_time: 35,
		content: {
			theory: `The numbered cards (Ace through Ten) of each suit tell a story of that element's journey and manifestation.

**Aces** represent the pure, undiluted essence and potential of each element - the seed.

**Twos** represent duality, choice, and balance.

**Threes** represent initial manifestation and growth.

**Fours** represent stability and structure.

**Fives** represent conflict, challenge, and change.

**Sixes** represent harmony, success, and movement forward.

**Sevens** represent reflection, assessment, and spiritual challenges.

**Eights** represent mastery, speed, and transformation.

**Nines** represent near-completion and the culmination of the journey.

**Tens** represent completion, endings, and the transition to new beginnings.

Each number also corresponds to a Sephirah on the Tree of Life, adding another layer of meaning.`,

			practice: `Lay out all four Aces, then all four Twos, etc. Study each row. What patterns do you notice? How does each element express that number differently? Choose one number and journal about what it means to you.`,

			meditation: `Imagine yourself holding an Ace - pure potential. Watch it grow through the numbers, developing, facing challenges, achieving mastery, and finally completing. This is the cycle of all endeavors.`,

			references: [
				'Israel Regardie, The Golden Dawn',
				'Rachel Pollack, Seventy-Eight Degrees of Wisdom'
			]
		},
		quiz: [
			{
				question: 'What do the Aces represent?',
				answers: [
					'Completion and endings',
					'Pure potential and essence',
					'Conflict and challenge',
					'Stability and structure'
				],
				correct: 1,
				explanation: 'Aces represent the pure, undiluted essence and potential of each element.'
			},
			{
				question: 'Which number represents conflict and challenge?',
				answers: ['Three', 'Four', 'Five', 'Six'],
				correct: 2,
				explanation: 'Fives represent conflict, challenge, and the need for change.'
			},
			{
				question: 'What do the Tens represent?',
				answers: [
					'Beginning of the journey',
					'Stability and structure',
					'Completion and transition',
					'Initial growth'
				],
				correct: 2,
				explanation: 'Tens represent completion, endings, and the transition to new beginnings.'
			}
		],
		unlocks_after_days: 4,
		is_free: false
	},
	{
		id: 'neophyte_06',
		title: 'Creating Sacred Space',
		grade: '0°=0°',
		grade_name: 'Neophyte',
		sephirah_context: 'Malkuth',
		order: 6,
		estimated_time: 25,
		content: {
			theory: `Before engaging in magical or divinatory work, practitioners create sacred space. This serves multiple purposes:

1. **Psychological**: Signals to your mind that you're entering a special state of awareness
2. **Energetic**: Clears and purifies the working area
3. **Protective**: Establishes boundaries against unwanted influences
4. **Focusing**: Centers your attention and intention

The most common method in the Golden Dawn tradition is the **Lesser Banishing Ritual of the Pentagram (LBRP)**, but simpler methods work too:

- Lighting a candle with intention
- Cleansing with incense or sound
- Visualizing protective light
- Calling the four directions/elements
- Simply stating your sacred intention

The key is consistent practice and genuine intention.`,

			practice: `Create your own simple sacred space ritual. It might include:
1. Taking three deep breaths to center yourself
2. Lighting a candle
3. Acknowledging the four directions and their elements
4. Stating your intention (e.g., "I enter this space for wisdom and truth")
5. Proceeding with your work
6. Giving thanks and extinguishing the candle when done

Practice this before your next tarot reading.`,

			meditation: `Visualize yourself surrounded by a sphere of white light. This light extends 6 feet in all directions. Nothing harmful can pass through it. This is your sacred space, and you control it completely.`,

			references: [
				'Israel Regardie, The Middle Pillar',
				'Dion Fortune, Psychic Self-Defense'
			]
		},
		quiz: [
			{
				question: 'What is the primary purpose of creating sacred space?',
				answers: [
					'To impress others',
					'To make magic stronger',
					'To signal a shift in awareness and intention',
					'To follow tradition'
				],
				correct: 2,
				explanation:
					'Sacred space primarily signals to your consciousness that you are entering a special state of awareness and intention.'
			},
			{
				question: 'What is the most important element of sacred space creation?',
				answers: [
					'Expensive tools',
					'Complex rituals',
					'Consistent practice and genuine intention',
					'Perfect memorization'
				],
				correct: 2,
				explanation:
					'Genuine intention and consistent practice are far more important than elaborate tools or complex rituals.'
			},
			{
				question: 'In the Golden Dawn tradition, what is LBRP?',
				answers: [
					'A tarot spread',
					'The Lesser Banishing Ritual of the Pentagram',
					'A meditation technique',
					'A type of incense'
				],
				correct: 1,
				explanation: 'LBRP stands for the Lesser Banishing Ritual of the Pentagram, a foundational Golden Dawn practice.'
			}
		],
		unlocks_after_days: 5,
		is_free: false
	}
];

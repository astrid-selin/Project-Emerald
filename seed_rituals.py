#!/usr/bin/env python3
"""
Seed data for Esoteric Rituals
Focus on Golden Dawn rituals and foundational Hermetic practices
"""

import json

RITUALS = [
    {
        'name': 'Lesser Banishing Ritual of the Pentagram',
        'abbreviation': 'LBRP',
        'tradition': 'Golden Dawn',
        'category': 'Banishing',
        'purpose': 'To banish unwanted energies and establish sacred space for magical work',
        'difficulty': 'Beginner',
        'duration_minutes': 10,
        'requires_tools': json.dumps(['Ritual dagger or wand (optional)']),
        'elemental_focus': None,
        'sephiroth_focus': None,
        'planetary_focus': None,
        'timing_notes': 'Can be performed any time, traditionally morning and evening',
        'instructions': '''1. Face East. Perform the Qabalistic Cross:
   - Touch forehead: "Atah" (Thou art)
   - Touch chest: "Malkuth" (the Kingdom)
   - Touch right shoulder: "ve-Geburah" (and the Power)
   - Touch left shoulder: "ve-Gedulah" (and the Glory)
   - Clasp hands at chest: "le-Olam, Amen" (forever, Amen)

2. Face East, trace large pentagram, vibrate "YHVH" (yod-heh-vav-heh)
3. Face South, trace pentagram, vibrate "ADONAI"
4. Face West, trace pentagram, vibrate "EHEIEH"
5. Face North, trace pentagram, vibrate "AGLA"

6. Return to East, extend arms in cross:
   "Before me, RAPHAEL
    Behind me, GABRIEL
    On my right hand, MICHAEL
    On my left hand, AURIEL
    For about me flames the Pentagram
    And in the column shines the Six-Rayed Star"

7. Repeat the Qabalistic Cross to close''',
        'visualization': 'Blue-white pentagrams blazing at the quarters, archangels as towering figures in their elemental colors',
        'words_of_power': 'YHVH, ADONAI, EHEIEH, AGLA, Raphael, Gabriel, Michael, Auriel',
        'benefits': 'Daily practice establishes psychic boundaries, clears space, balances energies, and strengthens the aura',
        'warnings': 'None - this is a safe foundational practice suitable for all',
        'source': 'Hermetic Order of the Golden Dawn',
        'description': 'The cornerstone ritual of Western ceremonial magic, establishing sacred space and invoking divine protection through the four quarters and archangels.'
    },
    {
        'name': 'Lesser Invoking Ritual of the Pentagram',
        'abbreviation': 'LIRP',
        'tradition': 'Golden Dawn',
        'category': 'Invoking',
        'purpose': 'To invoke and concentrate elemental energies for magical work',
        'difficulty': 'Beginner',
        'duration_minutes': 10,
        'requires_tools': json.dumps(['Ritual dagger or wand (optional)']),
        'elemental_focus': None,
        'sephiroth_focus': None,
        'planetary_focus': None,
        'timing_notes': 'After LBRP, before specific magical workings',
        'instructions': '''Identical to LBRP except:
- Pentagrams are traced starting from opposite point (invoking form)
- Used to draw energies in rather than banish them out
- Typically followed by specific elemental or planetary work

Structure same as LBRP with Qabalistic Cross opening and closing.''',
        'visualization': 'Golden pentagrams drawing energy inward, spiraling toward the center',
        'words_of_power': 'Same divine names as LBRP',
        'benefits': 'Concentrates energies for magical operations, charges talismans, enhances manifestation work',
        'warnings': 'Should only be used when you want to invoke energies. Always banish afterward to avoid residual buildup.',
        'source': 'Hermetic Order of the Golden Dawn',
        'description': 'The invoking counterpart to the LBRP, used to draw in and concentrate energies for active magical work.'
    },
    {
        'name': 'Middle Pillar Ritual',
        'abbreviation': 'MPR',
        'tradition': 'Golden Dawn',
        'category': 'Middle Pillar',
        'purpose': 'To awaken and balance the Middle Pillar of the Tree of Life within the body',
        'difficulty': 'Intermediate',
        'duration_minutes': 20,
        'requires_tools': json.dumps([]),
        'elemental_focus': None,
        'sephiroth_focus': 'Kether, Daath, Tiphareth, Yesod, Malkuth',
        'planetary_focus': None,
        'timing_notes': 'After LBRP, daily practice recommended',
        'instructions': '''1. Perform LBRP first

2. Stand facing East, visualize and vibrate:
   - Crown (Kether): White brilliance, vibrate "EHEIEH" (eh-heh-yeh)
   - Throat (Daath): Lavender-grey light, vibrate "YHVH ELOHIM"
   - Heart (Tiphareth): Golden-yellow sun, vibrate "YHVH ELOAH VE-DAATH"
   - Groin (Yesod): Purple or violet, vibrate "SHADDAI EL CHAI"
   - Feet (Malkuth): Earthy colors, vibrate "ADONAI HA-ARETZ"

3. Circulate the light:
   - Draw light down left side of body, up right side, forming circuit
   - Circulate several times
   - Draw down front, up back
   - Expand aura in all directions as sphere of light

4. Stand in balanced state, close with gratitude''',
        'visualization': 'Spheres of colored light at each center, connecting as pillars of light. Energy circulating through the body.',
        'words_of_power': 'EHEIEH, YHVH ELOHIM, YHVH ELOAH VE-DAATH, SHADDAI EL CHAI, ADONAI HA-ARETZ',
        'benefits': 'Balances subtle energies, enhances vitality, aligns with Tree of Life, develops psychic centers, healing',
        'warnings': 'Take time to ground afterward. Some may feel lightheaded initially - reduce duration if needed.',
        'source': 'Israel Regardie / Golden Dawn',
        'description': 'A powerful energy work ritual that establishes the Middle Pillar of the Tree of Life within the practitioner\'s subtle body, balancing and energizing the major psychic centers.'
    },
    {
        'name': 'Banishing Ritual of the Hexagram',
        'abbreviation': 'BRH',
        'tradition': 'Golden Dawn',
        'category': 'Banishing',
        'purpose': 'To banish planetary and zodiacal influences, working at a higher level than the pentagram',
        'difficulty': 'Intermediate',
        'duration_minutes': 15,
        'requires_tools': json.dumps(['Ritual dagger or wand']),
        'elemental_focus': None,
        'sephiroth_focus': None,
        'planetary_focus': None,
        'timing_notes': 'When planetary influences need to be banished, or for deeper cleansing than LBRP',
        'instructions': '''1. Perform LBRP and Qabalistic Cross

2. Face East, trace banishing hexagram of Fire (two interlaced triangles):
   - Trace from upper point of Fire triangle
   - Vibrate "ARARITA" (Notariqon: One is His Beginning, One is His Individuality, His Permutation is One)

3. Repeat in South, West, North with appropriate hexagrams

4. Analysis of Keyword:
   - Stand in form of cross, say: "I.N.R.I."
   - "Yod Nun Resh Yod"
   - "Virgo, Isis, Mighty Mother"
   - "Scorpio, Apophis, Destroyer"
   - "Sol, Osiris, Slain and Risen"
   - "Isis, Apophis, Osiris: IAO"

5. Signs of L.V.X.:
   - Raise arms in V: "The Sign of Osiris Slain" (L)
   - Arms crossed on chest: "The Sign of Mourning Isis" (V)
   - Arms raised, head back: "The Sign of Apophis and Typhon" (X)
   - Make L sign again: "L.V.X., the Light of the Cross"

6. Repeat Qabalistic Cross''',
        'visualization': 'Golden hexagrams blazing with solar light at each quarter',
        'words_of_power': 'ARARITA, I.N.R.I., IAO, L.V.X.',
        'benefits': 'Banishes deeper, more persistent influences than LBRP. Invokes solar energies. Powerful purification.',
        'warnings': 'Requires solid foundation in LBRP first. The Analysis of the Keyword is a profound formula - study its symbolism.',
        'source': 'Hermetic Order of the Golden Dawn',
        'description': 'An advanced banishing ritual using hexagrams (six-pointed stars) instead of pentagrams, operating on the planetary and zodiacal levels of consciousness.'
    },
    {
        'name': 'Invoking Ritual of the Hexagram',
        'abbreviation': 'IRH',
        'tradition': 'Golden Dawn',
        'category': 'Invoking',
        'purpose': 'To invoke specific planetary forces for magical operations',
        'difficulty': 'Advanced',
        'duration_minutes': 20,
        'requires_tools': json.dumps(['Ritual dagger or wand', 'Appropriate planetary symbols/colors']),
        'elemental_focus': None,
        'sephiroth_focus': None,
        'planetary_focus': 'Variable - depends on intended working',
        'timing_notes': 'During appropriate planetary day/hour for the force being invoked',
        'instructions': '''Similar to BRH but:
1. Use invoking forms of hexagrams specific to the planet
2. Each planet has unique hexagram and divine name
3. Trace planetary symbol in center of hexagram
4. Vibrate appropriate divine name for that planet

Example for Sun:
- Draw invoking hexagram of Sun
- Trace Sun symbol (⊙) in center
- Vibrate "YHVH ELOAH VE-DAATH"

Planets and their divine names:
- Sun: YHVH ELOAH VE-DAATH
- Moon: SHADDAI EL CHAI
- Mercury: ELOHIM TZABAOTH
- Venus: YHVH TZABAOTH
- Mars: ELOHIM GIBOR
- Jupiter: EL
- Saturn: YHVH ELOHIM''',
        'visualization': 'Planet-colored hexagrams with planetary symbols glowing within them',
        'words_of_power': 'Planetary divine names from Qabalah',
        'benefits': 'Invokes specific planetary energies for talismanic work, timing rituals, or developing specific qualities',
        'warnings': 'Advanced practice. Must understand planetary forces. Always banish with BRH after completion. Requires study of planetary correspondences.',
        'source': 'Hermetic Order of the Golden Dawn',
        'description': 'The advanced invoking ritual for working with specific planetary forces through hexagram geometry and divine names.'
    },
    {
        'name': 'Rose Cross Ritual',
        'abbreviation': 'RC',
        'tradition': 'Golden Dawn',
        'category': 'Banishing',
        'purpose': 'To create a gentle but powerful protective barrier, more subtle than LBRP',
        'difficulty': 'Intermediate',
        'duration_minutes': 15,
        'requires_tools': json.dumps([]),
        'elemental_focus': None,
        'sephiroth_focus': None,
        'planetary_focus': None,
        'timing_notes': 'Before meditation, sleep, or when gentle protection is needed',
        'instructions': '''1. Face East, extend right hand, trace a large cross:
   - From East to West (horizontal line)
   - From zenith to nadir (vertical line)
   - Creates a cross of light in each of six directions

2. Trace cross in East, South, West, North, Above, Below

3. In each direction, add a circle to create Rose Cross symbol

4. Draw connecting line linking all six crosses into a continuous sphere

5. Visualize yourself sealed within a golden sphere of rose crosses

6. Vibrate: "YEHESHUAH" (the divine name of salvation)

7. Close with statement of intent''',
        'visualization': 'Golden crosses blooming into roses, forming a complete sphere of soft golden light',
        'words_of_power': 'YEHESHUAH',
        'benefits': 'Gentle protection, good for sleep, meditation, or when aggressive banishing is inappropriate. Seals aura.',
        'warnings': 'Very passive - not for clearing existing negativity, but for maintaining a protected space',
        'source': 'Hermetic Order of the Golden Dawn',
        'description': 'A gentle, protective ritual using the symbol of the Rose Cross to create a sphere of soft protective light, ideal for meditation and sleep.'
    },
    {
        'name': 'Opening by Watchtower',
        'abbreviation': 'OWT',
        'tradition': 'Golden Dawn',
        'category': 'Invoking',
        'purpose': 'Supreme invoking ritual of the elements and quarters for major magical operations',
        'difficulty': 'Expert',
        'duration_minutes': 45,
        'requires_tools': json.dumps(['Full temple setup', 'Elemental weapons', 'Enochian tablets']),
        'elemental_focus': 'All four elements',
        'sephiroth_focus': None,
        'planetary_focus': None,
        'timing_notes': 'For major rituals, initiations, or significant magical operations',
        'instructions': '''Complex ritual involving:
1. LBRP and BRH
2. Invocation of elements in all four quarters using Supreme Invoking Pentagrams
3. Use of Enochian divine names and calls
4. Full invocations of each quarter with its sub-elements
5. Drawing together of elemental forces into the center

Each quarter includes:
- Supreme invoking pentagram
- Enochian divine names
- Full invocation of ruling powers
- Visualization of elemental forces

(Full text requires extensive study of Golden Dawn material)''',
        'visualization': 'Full temple with elemental watchtowers, kerubic forms, vivid elemental landscapes at each quarter',
        'words_of_power': 'Enochian divine names, elemental god-names, archangelic names',
        'benefits': 'Creates powerful consecrated space for major workings. Full elemental balance and invocation.',
        'warnings': 'EXPERT LEVEL ONLY. Requires extensive study, experience, and proper training. Always close properly afterward.',
        'source': 'Hermetic Order of the Golden Dawn - Adeptus Minor material',
        'description': 'The supreme elemental ritual of the Golden Dawn system, creating a fully consecrated magical temple by invoking the four quarters with their complete hierarchies.'
    }
]


def seed_rituals(cursor):
    """Insert rituals into the database"""
    print("\nSeeding Rituals...")

    for ritual in RITUALS:
        cursor.execute("""
            INSERT INTO rituals (
                name, abbreviation, tradition, category, purpose,
                difficulty, duration_minutes, requires_tools,
                elemental_focus, sephiroth_focus, planetary_focus,
                timing_notes, instructions, visualization,
                words_of_power, benefits, warnings, source, description
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            ritual['name'], ritual['abbreviation'], ritual['tradition'],
            ritual['category'], ritual['purpose'], ritual['difficulty'],
            ritual['duration_minutes'], ritual['requires_tools'],
            ritual['elemental_focus'], ritual['sephiroth_focus'],
            ritual['planetary_focus'], ritual['timing_notes'],
            ritual['instructions'], ritual['visualization'],
            ritual['words_of_power'], ritual['benefits'],
            ritual['warnings'], ritual['source'], ritual['description']
        ))

    print(f"  ✓ Inserted {len(RITUALS)} rituals")


if __name__ == '__main__':
    import sqlite3

    # Test the seeding function
    conn = sqlite3.connect('esoteric_knowledge.db')
    cursor = conn.cursor()

    try:
        seed_rituals(cursor)
        conn.commit()
        print("\n✓ Rituals data seeded successfully!")
    except Exception as e:
        print(f"\n✗ Error seeding data: {e}")
        conn.rollback()
    finally:
        conn.close()

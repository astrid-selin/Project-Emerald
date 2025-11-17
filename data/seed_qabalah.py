#!/usr/bin/env python3
"""
Seed data for Qabalah: 10 Sephiroth and 22 Paths
Based on Golden Dawn and traditional Hermetic Qabalah correspondences
"""

# The 10 Sephiroth on the Tree of Life
SEPHIROTH = [
    {
        'number': 1,
        'name': 'Kether',
        'name_hebrew': 'כֶּתֶר',
        'meaning': 'Crown',
        'divine_name': 'Eheieh (I Am)',
        'archangel': 'Metatron',
        'angelic_order': 'Chaioth ha-Qadesh (Holy Living Creatures)',
        'planet': 'Primum Mobile',
        'mundane_chakra': 'First Swirlings',
        'spiritual_experience': 'Union with God',
        'virtue': 'Attainment, Completion of the Great Work',
        'vice': None,
        'color_atziluth': 'Brilliance',
        'color_briah': 'Pure white brilliance',
        'color_yetzirah': 'Pure white brilliance',
        'color_assiah': 'White, flecked gold',
        'tarot_association': 'Four Aces',
        'description': 'The Crown, the first emanation, the point of unity before manifestation. Pure divine will and the source of all creation.'
    },
    {
        'number': 2,
        'name': 'Chokmah',
        'name_hebrew': 'חָכְמָה',
        'meaning': 'Wisdom',
        'divine_name': 'Jehovah (Yah)',
        'archangel': 'Raziel',
        'angelic_order': 'Auphanim (Wheels)',
        'planet': 'Zodiac',
        'mundane_chakra': 'Sphere of the Zodiac',
        'spiritual_experience': 'Vision of God face to face',
        'virtue': 'Devotion',
        'vice': None,
        'color_atziluth': 'Pure soft blue',
        'color_briah': 'Grey',
        'color_yetzirah': 'Pearl grey, iridescent',
        'color_assiah': 'White, flecked red, blue, yellow',
        'tarot_association': 'Four Twos, The Four Knights',
        'description': 'Wisdom, the first masculine principle. Dynamic, outpouring force and the first differentiation of unity.'
    },
    {
        'number': 3,
        'name': 'Binah',
        'name_hebrew': 'בִּינָה',
        'meaning': 'Understanding',
        'divine_name': 'Jehovah Elohim',
        'archangel': 'Tzaphkiel',
        'angelic_order': 'Aralim (Thrones)',
        'planet': 'Saturn',
        'mundane_chakra': 'Sphere of Saturn',
        'spiritual_experience': 'Vision of Sorrow',
        'virtue': 'Silence',
        'vice': 'Avarice',
        'color_atziluth': 'Crimson',
        'color_briah': 'Black',
        'color_yetzirah': 'Dark brown',
        'color_assiah': 'Grey, flecked pink',
        'tarot_association': 'Four Threes, The Four Queens',
        'description': 'Understanding, the Great Mother, the womb of form. Receptive, limiting principle that gives structure to the outpouring of Chokmah.'
    },
    {
        'number': 4,
        'name': 'Chesed',
        'name_hebrew': 'חֶסֶד',
        'meaning': 'Mercy',
        'divine_name': 'El',
        'archangel': 'Tzadkiel',
        'angelic_order': 'Chasmalim (Brilliant Ones)',
        'planet': 'Jupiter',
        'mundane_chakra': 'Sphere of Jupiter',
        'spiritual_experience': 'Vision of Love',
        'virtue': 'Obedience',
        'vice': 'Bigotry, Hypocrisy, Gluttony, Tyranny',
        'color_atziluth': 'Deep violet',
        'color_briah': 'Blue',
        'color_yetzirah': 'Deep purple',
        'color_assiah': 'Deep azure, flecked yellow',
        'tarot_association': 'Four Fours',
        'description': 'Mercy and loving-kindness. Benevolent, expansive force of grace and abundance. The builder and organizer.'
    },
    {
        'number': 5,
        'name': 'Geburah',
        'name_hebrew': 'גְּבוּרָה',
        'meaning': 'Severity',
        'divine_name': 'Elohim Gibor',
        'archangel': 'Samael',
        'angelic_order': 'Seraphim (Fiery Serpents)',
        'planet': 'Mars',
        'mundane_chakra': 'Sphere of Mars',
        'spiritual_experience': 'Vision of Power',
        'virtue': 'Energy, Courage',
        'vice': 'Cruelty, Destruction',
        'color_atziluth': 'Orange',
        'color_briah': 'Scarlet red',
        'color_yetzirah': 'Bright scarlet',
        'color_assiah': 'Red, flecked black',
        'tarot_association': 'Four Fives',
        'description': 'Strength and severity. Destructive, limiting force that breaks down excess. Justice and necessary harshness.'
    },
    {
        'number': 6,
        'name': 'Tiphareth',
        'name_hebrew': 'תִּפְאֶרֶת',
        'meaning': 'Beauty',
        'divine_name': 'Jehovah Aloah va Daath',
        'archangel': 'Michael',
        'angelic_order': 'Malachim (Kings)',
        'planet': 'Sun',
        'mundane_chakra': 'Sphere of the Sun',
        'spiritual_experience': 'Vision of the Harmony of Things, Mysteries of the Crucifixion',
        'virtue': 'Devotion to the Great Work',
        'vice': 'Pride',
        'color_atziluth': 'Clear pink rose',
        'color_briah': 'Yellow',
        'color_yetzirah': 'Rich salmon pink',
        'color_assiah': 'Golden amber',
        'tarot_association': 'Four Sixes, The Four Princes',
        'description': 'Beauty and harmony. The central balancing point of the Tree. The seat of the Higher Self and Solar consciousness.'
    },
    {
        'number': 7,
        'name': 'Netzach',
        'name_hebrew': 'נֶצַח',
        'meaning': 'Victory',
        'divine_name': 'Jehovah Tzabaoth',
        'archangel': 'Haniel',
        'angelic_order': 'Elohim (Gods)',
        'planet': 'Venus',
        'mundane_chakra': 'Sphere of Venus',
        'spiritual_experience': 'Vision of Beauty Triumphant',
        'virtue': 'Unselfishness',
        'vice': 'Impurity, Lust',
        'color_atziluth': 'Amber',
        'color_briah': 'Emerald',
        'color_yetzirah': 'Bright yellow-green',
        'color_assiah': 'Olive, flecked gold',
        'tarot_association': 'Four Sevens',
        'description': 'Victory and endurance. The realm of emotion, desire, and creative inspiration. Nature, art, and the aesthetic sense.'
    },
    {
        'number': 8,
        'name': 'Hod',
        'name_hebrew': 'הוֹד',
        'meaning': 'Glory',
        'divine_name': 'Elohim Tzabaoth',
        'archangel': 'Raphael',
        'angelic_order': 'Beni Elohim (Sons of God)',
        'planet': 'Mercury',
        'mundane_chakra': 'Sphere of Mercury',
        'spiritual_experience': 'Vision of Splendor',
        'virtue': 'Truthfulness',
        'vice': 'Falsehood, Dishonesty',
        'color_atziluth': 'Violet purple',
        'color_briah': 'Orange',
        'color_yetzirah': 'Russet red',
        'color_assiah': 'Yellowish black, flecked white',
        'tarot_association': 'Four Eights',
        'description': 'Splendor and intellect. The realm of thought, communication, and magic. Science, learning, and the rational mind.'
    },
    {
        'number': 9,
        'name': 'Yesod',
        'name_hebrew': 'יְסוֹד',
        'meaning': 'Foundation',
        'divine_name': 'Shaddai El Chai',
        'archangel': 'Gabriel',
        'angelic_order': 'Cherubim (The Strong)',
        'planet': 'Moon',
        'mundane_chakra': 'Sphere of the Moon',
        'spiritual_experience': 'Vision of the Machinery of the Universe',
        'virtue': 'Independence',
        'vice': 'Idleness',
        'color_atziluth': 'Indigo',
        'color_briah': 'Violet',
        'color_yetzirah': 'Very dark purple',
        'color_assiah': 'Citrine, flecked azure',
        'tarot_association': 'Four Nines',
        'description': 'The Foundation, the astral realm. The subconscious mind, dreams, and the etheric template of physical reality.'
    },
    {
        'number': 10,
        'name': 'Malkuth',
        'name_hebrew': 'מַלְכוּת',
        'meaning': 'Kingdom',
        'divine_name': 'Adonai ha-Aretz',
        'archangel': 'Sandalphon',
        'angelic_order': 'Ashim (Souls of Fire)',
        'planet': 'Earth',
        'mundane_chakra': 'Sphere of the Elements',
        'spiritual_experience': 'Vision of the Holy Guardian Angel',
        'virtue': 'Discrimination',
        'vice': 'Avarice, Inertia',
        'color_atziluth': 'Yellow',
        'color_briah': 'Citrine, olive, russet, black',
        'color_yetzirah': 'Citrine, olive, russet, black, flecked gold',
        'color_assiah': 'Black, rayed yellow',
        'tarot_association': 'Four Tens, The Four Princesses',
        'description': 'The Kingdom, the physical world. The material plane where all the other Sephiroth manifest in concrete form.'
    }
]

# The 22 Paths connecting the Sephiroth
# Each path corresponds to a Hebrew letter and a Major Arcana card
# Paths are numbered 11-32 in traditional Qabalah
PATHS = [
    {
        'number': 11,
        'name': 'The Path of Aleph',
        'hebrew_letter': 'Aleph',
        'hebrew_letter_meaning': 'Ox',
        'tarot_card_number': 0,  # The Fool
        'connects_from': 1,  # Kether
        'connects_to': 2,    # Chokmah
        'element': 'Air',
        'planet': None,
        'sign': None,
        'color': 'Bright pale yellow',
        'description': 'The Path of Air connecting Crown to Wisdom. The Fool\'s journey from unity into manifestation.'
    },
    {
        'number': 12,
        'name': 'The Path of Beth',
        'hebrew_letter': 'Beth',
        'hebrew_letter_meaning': 'House',
        'tarot_card_number': 1,  # The Magician
        'connects_from': 1,  # Kether
        'connects_to': 3,    # Binah
        'element': None,
        'planet': 'Mercury',
        'sign': None,
        'color': 'Yellow',
        'description': 'The Path of Mercury. The channel of divine will into form through communication and magic.'
    },
    {
        'number': 13,
        'name': 'The Path of Gimel',
        'hebrew_letter': 'Gimel',
        'hebrew_letter_meaning': 'Camel',
        'tarot_card_number': 2,  # The High Priestess
        'connects_from': 1,  # Kether
        'connects_to': 6,    # Tiphareth
        'element': None,
        'planet': 'Moon',
        'sign': None,
        'color': 'Blue',
        'description': 'The Path of the Moon. The channel of divine light into beauty through intuition and the unconscious.'
    },
    {
        'number': 14,
        'name': 'The Path of Daleth',
        'hebrew_letter': 'Daleth',
        'hebrew_letter_meaning': 'Door',
        'tarot_card_number': 3,  # The Empress
        'connects_from': 2,  # Chokmah
        'connects_to': 3,    # Binah
        'element': None,
        'planet': 'Venus',
        'sign': None,
        'color': 'Emerald green',
        'description': 'The Path of Venus connecting Wisdom to Understanding. The union of opposites in love.'
    },
    {
        'number': 15,
        'name': 'The Path of Heh',
        'hebrew_letter': 'Heh',
        'hebrew_letter_meaning': 'Window',
        'tarot_card_number': 4,  # The Emperor
        'connects_from': 2,  # Chokmah
        'connects_to': 6,    # Tiphareth
        'element': None,
        'planet': None,
        'sign': 'Aries',
        'color': 'Scarlet',
        'description': 'The Path of Aries. The masculine force of will and authority descending to the heart center.'
    },
    {
        'number': 16,
        'name': 'The Path of Vav',
        'hebrew_letter': 'Vav',
        'hebrew_letter_meaning': 'Nail',
        'tarot_card_number': 5,  # The Hierophant
        'connects_from': 2,  # Chokmah
        'connects_to': 4,    # Chesed
        'element': None,
        'planet': None,
        'sign': 'Taurus',
        'color': 'Red-orange',
        'description': 'The Path of Taurus. The channel of divine wisdom into mercy through spiritual teaching.'
    },
    {
        'number': 17,
        'name': 'The Path of Zain',
        'hebrew_letter': 'Zain',
        'hebrew_letter_meaning': 'Sword',
        'tarot_card_number': 6,  # The Lovers
        'connects_from': 3,  # Binah
        'connects_to': 6,    # Tiphareth
        'element': None,
        'planet': None,
        'sign': 'Gemini',
        'color': 'Orange',
        'description': 'The Path of Gemini. The descent from Understanding through the choices and dualities of life.'
    },
    {
        'number': 18,
        'name': 'The Path of Cheth',
        'hebrew_letter': 'Cheth',
        'hebrew_letter_meaning': 'Fence',
        'tarot_card_number': 7,  # The Chariot
        'connects_from': 3,  # Binah
        'connects_to': 5,    # Geburah
        'element': None,
        'planet': None,
        'sign': 'Cancer',
        'color': 'Amber',
        'description': 'The Path of Cancer. The channel of form-giving understanding into the severity of discipline.'
    },
    {
        'number': 19,
        'name': 'The Path of Teth',
        'hebrew_letter': 'Teth',
        'hebrew_letter_meaning': 'Serpent',
        'tarot_card_number': 8,  # Strength (Lust in Thoth)
        'connects_from': 4,  # Chesed
        'connects_to': 5,    # Geburah
        'element': None,
        'planet': None,
        'sign': 'Leo',
        'color': 'Yellow-green',
        'description': 'The Path of Leo. The balance between mercy and severity through controlled passion.'
    },
    {
        'number': 20,
        'name': 'The Path of Yod',
        'hebrew_letter': 'Yod',
        'hebrew_letter_meaning': 'Hand',
        'tarot_card_number': 9,  # The Hermit
        'connects_from': 4,  # Chesed
        'connects_to': 6,    # Tiphareth
        'element': None,
        'planet': None,
        'sign': 'Virgo',
        'color': 'Yellow-green',
        'description': 'The Path of Virgo. The descent of mercy into beauty through introspection and wisdom.'
    },
    {
        'number': 21,
        'name': 'The Path of Kaph',
        'hebrew_letter': 'Kaph',
        'hebrew_letter_meaning': 'Fist',
        'tarot_card_number': 10,  # Wheel of Fortune
        'connects_from': 4,  # Chesed
        'connects_to': 7,    # Netzach
        'element': None,
        'planet': 'Jupiter',
        'sign': None,
        'color': 'Violet',
        'description': 'The Path of Jupiter. The expansive force of fortune descending from mercy to victory.'
    },
    {
        'number': 22,
        'name': 'The Path of Lamed',
        'hebrew_letter': 'Lamed',
        'hebrew_letter_meaning': 'Ox Goad',
        'tarot_card_number': 11,  # Justice (Adjustment in Thoth)
        'connects_from': 5,  # Geburah
        'connects_to': 6,    # Tiphareth
        'element': None,
        'planet': None,
        'sign': 'Libra',
        'color': 'Emerald green',
        'description': 'The Path of Libra. The balancing of severity into the harmony of beauty.'
    },
    {
        'number': 23,
        'name': 'The Path of Mem',
        'hebrew_letter': 'Mem',
        'hebrew_letter_meaning': 'Water',
        'tarot_card_number': 12,  # The Hanged Man
        'connects_from': 5,  # Geburah
        'connects_to': 8,    # Hod
        'element': 'Water',
        'planet': None,
        'sign': None,
        'color': 'Deep blue',
        'description': 'The Path of Water. The descent of severity into the realm of intellect through sacrifice.'
    },
    {
        'number': 24,
        'name': 'The Path of Nun',
        'hebrew_letter': 'Nun',
        'hebrew_letter_meaning': 'Fish',
        'tarot_card_number': 13,  # Death
        'connects_from': 6,  # Tiphareth
        'connects_to': 7,    # Netzach
        'element': None,
        'planet': None,
        'sign': 'Scorpio',
        'color': 'Green-blue',
        'description': 'The Path of Scorpio. Transformation from the center of beauty into the realm of emotion.'
    },
    {
        'number': 25,
        'name': 'The Path of Samekh',
        'hebrew_letter': 'Samekh',
        'hebrew_letter_meaning': 'Prop',
        'tarot_card_number': 14,  # Temperance (Art in Thoth)
        'connects_from': 6,  # Tiphareth
        'connects_to': 9,    # Yesod
        'element': None,
        'planet': None,
        'sign': 'Sagittarius',
        'color': 'Blue',
        'description': 'The Path of Sagittarius. The arrow from beauty to foundation, the path of spiritual alchemy.'
    },
    {
        'number': 26,
        'name': 'The Path of Ayin',
        'hebrew_letter': 'Ayin',
        'hebrew_letter_meaning': 'Eye',
        'tarot_card_number': 15,  # The Devil
        'connects_from': 6,  # Tiphareth
        'connects_to': 8,    # Hod
        'element': None,
        'planet': None,
        'sign': 'Capricorn',
        'color': 'Indigo',
        'description': 'The Path of Capricorn. The binding of beauty to intellect through earthly manifestation.'
    },
    {
        'number': 27,
        'name': 'The Path of Peh',
        'hebrew_letter': 'Peh',
        'hebrew_letter_meaning': 'Mouth',
        'tarot_card_number': 16,  # The Tower
        'connects_from': 7,  # Netzach
        'connects_to': 8,    # Hod
        'element': None,
        'planet': 'Mars',
        'sign': None,
        'color': 'Scarlet',
        'description': 'The Path of Mars. The destructive force breaking down between emotion and intellect.'
    },
    {
        'number': 28,
        'name': 'The Path of Tzaddi',
        'hebrew_letter': 'Tzaddi',
        'hebrew_letter_meaning': 'Fish Hook',
        'tarot_card_number': 17,  # The Star
        'connects_from': 7,  # Netzach
        'connects_to': 9,    # Yesod
        'element': None,
        'planet': None,
        'sign': 'Aquarius',
        'color': 'Violet',
        'description': 'The Path of Aquarius. Hope and inspiration flowing from victory to foundation.'
    },
    {
        'number': 29,
        'name': 'The Path of Qoph',
        'hebrew_letter': 'Qoph',
        'hebrew_letter_meaning': 'Back of Head',
        'tarot_card_number': 18,  # The Moon
        'connects_from': 7,  # Netzach
        'connects_to': 10,   # Malkuth
        'element': None,
        'planet': None,
        'sign': 'Pisces',
        'color': 'Crimson (ultra-violet)',
        'description': 'The Path of Pisces. The descent from emotion into the material realm through illusion.'
    },
    {
        'number': 30,
        'name': 'The Path of Resh',
        'hebrew_letter': 'Resh',
        'hebrew_letter_meaning': 'Head',
        'tarot_card_number': 19,  # The Sun
        'connects_from': 8,  # Hod
        'connects_to': 9,    # Yesod
        'element': None,
        'planet': 'Sun',
        'sign': None,
        'color': 'Orange',
        'description': 'The Path of the Sun. The illumination connecting intellect to the astral foundation.'
    },
    {
        'number': 31,
        'name': 'The Path of Shin',
        'hebrew_letter': 'Shin',
        'hebrew_letter_meaning': 'Tooth',
        'tarot_card_number': 20,  # Judgement (The Aeon in Thoth)
        'connects_from': 8,  # Hod
        'connects_to': 10,   # Malkuth
        'element': 'Fire',
        'planet': None,
        'sign': None,
        'color': 'Glowing orange-scarlet',
        'description': 'The Path of Fire. The final judgment and awakening from mind into matter.'
    },
    {
        'number': 32,
        'name': 'The Path of Tau',
        'hebrew_letter': 'Tau',
        'hebrew_letter_meaning': 'Cross',
        'tarot_card_number': 21,  # The World (The Universe in Thoth)
        'connects_from': 9,  # Yesod
        'connects_to': 10,   # Malkuth
        'element': 'Earth',
        'planet': 'Saturn',
        'sign': None,
        'color': 'Indigo',
        'description': 'The Path of Earth and Saturn. The final descent from foundation into complete manifestation.'
    }
]


def seed_sephiroth(cursor):
    """Insert all 10 Sephiroth into the database"""
    print("\nSeeding Sephiroth...")

    for seph in SEPHIROTH:
        cursor.execute("""
            INSERT INTO sephiroth (
                number, name, name_hebrew, meaning, divine_name,
                archangel, angelic_order, planet, mundane_chakra,
                spiritual_experience, virtue, vice,
                color_atziluth, color_briah, color_yetzirah, color_assiah,
                tarot_association, description
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            seph['number'], seph['name'], seph['name_hebrew'], seph['meaning'],
            seph['divine_name'], seph['archangel'], seph['angelic_order'],
            seph['planet'], seph['mundane_chakra'], seph['spiritual_experience'],
            seph['virtue'], seph['vice'], seph['color_atziluth'], seph['color_briah'],
            seph['color_yetzirah'], seph['color_assiah'], seph['tarot_association'],
            seph['description']
        ))

    print(f"  ✓ Inserted {len(SEPHIROTH)} Sephiroth")


def seed_paths(cursor):
    """Insert all 22 Paths into the database, linking to tarot cards"""
    print("\nSeeding Paths...")

    for path in PATHS:
        # Get the tarot card ID from the card number
        cursor.execute(
            "SELECT id FROM cards WHERE number = ?",
            (path['tarot_card_number'],)
        )
        card_result = cursor.fetchone()
        tarot_card_id = card_result[0] if card_result else None

        cursor.execute("""
            INSERT INTO paths (
                number, name, hebrew_letter, hebrew_letter_meaning,
                tarot_card_id, connects_from, connects_to,
                element, planet, sign, color, description
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            path['number'], path['name'], path['hebrew_letter'],
            path['hebrew_letter_meaning'], tarot_card_id,
            path['connects_from'], path['connects_to'],
            path['element'], path['planet'], path['sign'],
            path['color'], path['description']
        ))

    print(f"  ✓ Inserted {len(PATHS)} Paths")


if __name__ == '__main__':
    import sqlite3

    # Test the seeding functions
    conn = sqlite3.connect('esoteric_knowledge.db')
    cursor = conn.cursor()

    try:
        seed_sephiroth(cursor)
        seed_paths(cursor)
        conn.commit()
        print("\n✓ Qabalah data seeded successfully!")
    except Exception as e:
        print(f"\n✗ Error seeding data: {e}")
        conn.rollback()
    finally:
        conn.close()

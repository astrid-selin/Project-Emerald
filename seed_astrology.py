#!/usr/bin/env python3
"""
Seed data for Astrology: Planets and Zodiac Signs
Based on traditional Western/Hermetic astrology correspondences
"""

import json

# The 7 Classical Planets + Sun and Moon
PLANETS = [
    {
        'name': 'Sun',
        'symbol': '☉',
        'day_of_week': 'Sunday',
        'metal': 'Gold',
        'color': 'Gold, Yellow',
        'gemstone': 'Diamond, Ruby, Sunstone',
        'sephiroth_number': 6,  # Tiphareth
        'rules_signs': json.dumps(['Leo']),
        'exalted_in': 'Aries',
        'detriment_in': 'Aquarius',
        'fall_in': 'Libra',
        'quality': 'Hot, Dry',
        'tarot_association': 'The Sun (XIX)',
        'magical_powers': 'Success, vitality, leadership, illumination, healing, spiritual development',
        'description': 'The luminary of day, representing the conscious self, vitality, life force, and the divine spark within. Rules identity, ego, and creative expression.'
    },
    {
        'name': 'Moon',
        'symbol': '☽',
        'day_of_week': 'Monday',
        'metal': 'Silver',
        'color': 'Silver, White',
        'gemstone': 'Moonstone, Pearl, Selenite',
        'sephiroth_number': 9,  # Yesod
        'rules_signs': json.dumps(['Cancer']),
        'exalted_in': 'Taurus',
        'detriment_in': 'Capricorn',
        'fall_in': 'Scorpio',
        'quality': 'Cold, Moist',
        'tarot_association': 'The High Priestess (II), The Moon (XVIII)',
        'magical_powers': 'Psychic ability, intuition, dreams, emotions, tides, cycles, feminine mysteries',
        'description': 'The luminary of night, representing the subconscious mind, emotions, instincts, and the soul. Rules memory, habits, and the inner life.'
    },
    {
        'name': 'Mercury',
        'symbol': '☿',
        'day_of_week': 'Wednesday',
        'metal': 'Quicksilver (Mercury)',
        'color': 'Orange, Multi-colored',
        'gemstone': 'Agate, Citrine, Aventurine',
        'sephiroth_number': 8,  # Hod
        'rules_signs': json.dumps(['Gemini', 'Virgo']),
        'exalted_in': 'Virgo',
        'detriment_in': 'Sagittarius, Pisces',
        'fall_in': 'Pisces',
        'quality': 'Cold, Dry',
        'tarot_association': 'The Magician (I)',
        'magical_powers': 'Communication, intellect, magic, travel, commerce, writing, divination, cunning',
        'description': 'The messenger god, representing communication, intellect, reason, and the rational mind. Rules thought, speech, writing, and short journeys.'
    },
    {
        'name': 'Venus',
        'symbol': '♀',
        'day_of_week': 'Friday',
        'metal': 'Copper',
        'color': 'Green, Pink',
        'gemstone': 'Emerald, Rose Quartz, Jade',
        'sephiroth_number': 7,  # Netzach
        'rules_signs': json.dumps(['Taurus', 'Libra']),
        'exalted_in': 'Pisces',
        'detriment_in': 'Aries, Scorpio',
        'fall_in': 'Virgo',
        'quality': 'Cold, Moist',
        'tarot_association': 'The Empress (III)',
        'magical_powers': 'Love, beauty, harmony, attraction, pleasure, art, relationships, fertility',
        'description': 'The goddess of love and beauty, representing affection, harmony, values, and aesthetic sense. Rules love, pleasure, and the arts.'
    },
    {
        'name': 'Mars',
        'symbol': '♂',
        'day_of_week': 'Tuesday',
        'metal': 'Iron',
        'color': 'Red, Scarlet',
        'gemstone': 'Ruby, Garnet, Bloodstone',
        'sephiroth_number': 5,  # Geburah
        'rules_signs': json.dumps(['Aries', 'Scorpio']),
        'exalted_in': 'Capricorn',
        'detriment_in': 'Libra, Taurus',
        'fall_in': 'Cancer',
        'quality': 'Hot, Dry',
        'tarot_association': 'The Tower (XVI)',
        'magical_powers': 'Courage, strength, conflict, passion, aggression, war, energy, drive, protection',
        'description': 'The god of war, representing action, assertion, desire, and the will to conquer. Rules energy, passion, and physical strength.'
    },
    {
        'name': 'Jupiter',
        'symbol': '♃',
        'day_of_week': 'Thursday',
        'metal': 'Tin',
        'color': 'Blue, Purple',
        'gemstone': 'Sapphire, Amethyst, Lapis Lazuli',
        'sephiroth_number': 4,  # Chesed
        'rules_signs': json.dumps(['Sagittarius', 'Pisces']),
        'exalted_in': 'Cancer',
        'detriment_in': 'Gemini, Virgo',
        'fall_in': 'Capricorn',
        'quality': 'Hot, Moist',
        'tarot_association': 'Wheel of Fortune (X)',
        'magical_powers': 'Expansion, abundance, wisdom, prosperity, good fortune, justice, growth, optimism',
        'description': 'The king of gods, representing expansion, abundance, wisdom, and beneficence. Rules growth, optimism, and higher learning.'
    },
    {
        'name': 'Saturn',
        'symbol': '♄',
        'day_of_week': 'Saturday',
        'metal': 'Lead',
        'color': 'Black, Indigo',
        'gemstone': 'Onyx, Obsidian, Jet',
        'sephiroth_number': 3,  # Binah
        'rules_signs': json.dumps(['Capricorn', 'Aquarius']),
        'exalted_in': 'Libra',
        'detriment_in': 'Cancer, Leo',
        'fall_in': 'Aries',
        'quality': 'Cold, Dry',
        'tarot_association': 'The World (XXI)',
        'magical_powers': 'Limitation, discipline, structure, time, karma, boundaries, endings, wisdom through suffering',
        'description': 'The lord of time and limitation, representing structure, discipline, and the lessons of experience. Rules responsibility, karma, and maturity.'
    }
]

# The 12 Zodiac Signs
ZODIAC_SIGNS = [
    {
        'name': 'Aries',
        'symbol': '♈',
        'element': 'Fire',
        'modality': 'Cardinal',
        'ruling_planet': 'Mars',
        'exalted_planet': 'Sun',
        'detriment_planet': 'Venus',
        'fall_planet': 'Saturn',
        'polarity': 'Positive',
        'house_number': 1,
        'body_part': 'Head, Face',
        'tarot_association': 'The Emperor (IV)',
        'dates_start': '03-21',
        'dates_end': '04-19',
        'keywords': json.dumps(['Initiative', 'Courage', 'Leadership', 'Independence', 'Impulsiveness', 'Pioneering']),
        'description': 'The Ram. First sign of the zodiac, representing new beginnings, initiative, and the primal life force. Cardinal fire: the spark of creation.'
    },
    {
        'name': 'Taurus',
        'symbol': '♉',
        'element': 'Earth',
        'modality': 'Fixed',
        'ruling_planet': 'Venus',
        'exalted_planet': 'Moon',
        'detriment_planet': 'Mars',
        'fall_planet': None,
        'polarity': 'Negative',
        'house_number': 2,
        'body_part': 'Neck, Throat',
        'tarot_association': 'The Hierophant (V)',
        'dates_start': '04-20',
        'dates_end': '05-20',
        'keywords': json.dumps(['Stability', 'Patience', 'Sensuality', 'Determination', 'Possessiveness', 'Materialism']),
        'description': 'The Bull. Representing stability, material security, and the pleasures of the senses. Fixed earth: enduring substance.'
    },
    {
        'name': 'Gemini',
        'symbol': '♊',
        'element': 'Air',
        'modality': 'Mutable',
        'ruling_planet': 'Mercury',
        'exalted_planet': None,
        'detriment_planet': 'Jupiter',
        'fall_planet': None,
        'polarity': 'Positive',
        'house_number': 3,
        'body_part': 'Arms, Hands, Lungs',
        'tarot_association': 'The Lovers (VI)',
        'dates_start': '05-21',
        'dates_end': '06-20',
        'keywords': json.dumps(['Communication', 'Versatility', 'Curiosity', 'Duality', 'Adaptability', 'Restlessness']),
        'description': 'The Twins. Representing duality, communication, and mental agility. Mutable air: the changing winds of thought.'
    },
    {
        'name': 'Cancer',
        'symbol': '♋',
        'element': 'Water',
        'modality': 'Cardinal',
        'ruling_planet': 'Moon',
        'exalted_planet': 'Jupiter',
        'detriment_planet': 'Saturn',
        'fall_planet': 'Mars',
        'polarity': 'Negative',
        'house_number': 4,
        'body_part': 'Chest, Breasts, Stomach',
        'tarot_association': 'The Chariot (VII)',
        'dates_start': '06-21',
        'dates_end': '07-22',
        'keywords': json.dumps(['Nurturing', 'Emotion', 'Protection', 'Intuition', 'Sensitivity', 'Moodiness']),
        'description': 'The Crab. Representing emotion, nurturing, and the protective shell. Cardinal water: the source of emotional flow.'
    },
    {
        'name': 'Leo',
        'symbol': '♌',
        'element': 'Fire',
        'modality': 'Fixed',
        'ruling_planet': 'Sun',
        'exalted_planet': None,
        'detriment_planet': 'Saturn',
        'fall_planet': None,
        'polarity': 'Positive',
        'house_number': 5,
        'body_part': 'Heart, Upper Back',
        'tarot_association': 'Strength (VIII) / Lust',
        'dates_start': '07-23',
        'dates_end': '08-22',
        'keywords': json.dumps(['Creativity', 'Pride', 'Generosity', 'Leadership', 'Drama', 'Self-expression']),
        'description': 'The Lion. Representing creativity, self-expression, and royal dignity. Fixed fire: the sustained flame of the heart.'
    },
    {
        'name': 'Virgo',
        'symbol': '♍',
        'element': 'Earth',
        'modality': 'Mutable',
        'ruling_planet': 'Mercury',
        'exalted_planet': 'Mercury',
        'detriment_planet': 'Jupiter',
        'fall_planet': 'Venus',
        'polarity': 'Negative',
        'house_number': 6,
        'body_part': 'Digestive System, Intestines',
        'tarot_association': 'The Hermit (IX)',
        'dates_start': '08-23',
        'dates_end': '09-22',
        'keywords': json.dumps(['Analysis', 'Service', 'Perfectionism', 'Health', 'Detail', 'Criticism']),
        'description': 'The Virgin. Representing purity, discernment, and service. Mutable earth: the harvest and refinement.'
    },
    {
        'name': 'Libra',
        'symbol': '♎',
        'element': 'Air',
        'modality': 'Cardinal',
        'ruling_planet': 'Venus',
        'exalted_planet': 'Saturn',
        'detriment_planet': 'Mars',
        'fall_planet': 'Sun',
        'polarity': 'Positive',
        'house_number': 7,
        'body_part': 'Kidneys, Lower Back',
        'tarot_association': 'Justice (XI) / Adjustment',
        'dates_start': '09-23',
        'dates_end': '10-22',
        'keywords': json.dumps(['Balance', 'Harmony', 'Justice', 'Partnership', 'Indecision', 'Diplomacy']),
        'description': 'The Scales. Representing balance, justice, and relationship. Cardinal air: the breath of equilibrium.'
    },
    {
        'name': 'Scorpio',
        'symbol': '♏',
        'element': 'Water',
        'modality': 'Fixed',
        'ruling_planet': 'Mars',
        'exalted_planet': None,
        'detriment_planet': 'Venus',
        'fall_planet': 'Moon',
        'polarity': 'Negative',
        'house_number': 8,
        'body_part': 'Reproductive Organs',
        'tarot_association': 'Death (XIII)',
        'dates_start': '10-23',
        'dates_end': '11-21',
        'keywords': json.dumps(['Transformation', 'Intensity', 'Power', 'Depth', 'Passion', 'Mystery']),
        'description': 'The Scorpion (and Eagle, and Phoenix). Representing transformation, death, rebirth, and the mysteries. Fixed water: the depths of emotion.'
    },
    {
        'name': 'Sagittarius',
        'symbol': '♐',
        'element': 'Fire',
        'modality': 'Mutable',
        'ruling_planet': 'Jupiter',
        'exalted_planet': None,
        'detriment_planet': 'Mercury',
        'fall_planet': None,
        'polarity': 'Positive',
        'house_number': 9,
        'body_part': 'Hips, Thighs',
        'tarot_association': 'Temperance (XIV) / Art',
        'dates_start': '11-22',
        'dates_end': '12-21',
        'keywords': json.dumps(['Philosophy', 'Adventure', 'Optimism', 'Freedom', 'Exploration', 'Truth-seeking']),
        'description': 'The Archer. Representing quest for meaning, philosophy, and expansion. Mutable fire: the arrow of aspiration.'
    },
    {
        'name': 'Capricorn',
        'symbol': '♑',
        'element': 'Earth',
        'modality': 'Cardinal',
        'ruling_planet': 'Saturn',
        'exalted_planet': 'Mars',
        'detriment_planet': 'Moon',
        'fall_planet': 'Jupiter',
        'polarity': 'Negative',
        'house_number': 10,
        'body_part': 'Knees, Bones, Skin',
        'tarot_association': 'The Devil (XV)',
        'dates_start': '12-22',
        'dates_end': '01-19',
        'keywords': json.dumps(['Ambition', 'Discipline', 'Authority', 'Structure', 'Responsibility', 'Achievement']),
        'description': 'The Goat (Sea-Goat). Representing ambition, achievement, and mastery of the material world. Cardinal earth: the mountain peak.'
    },
    {
        'name': 'Aquarius',
        'symbol': '♒',
        'element': 'Air',
        'modality': 'Fixed',
        'ruling_planet': 'Saturn',
        'exalted_planet': None,
        'detriment_planet': 'Sun',
        'fall_planet': None,
        'polarity': 'Positive',
        'house_number': 11,
        'body_part': 'Ankles, Circulatory System',
        'tarot_association': 'The Star (XVII)',
        'dates_start': '01-20',
        'dates_end': '02-18',
        'keywords': json.dumps(['Innovation', 'Humanitarianism', 'Independence', 'Eccentricity', 'Progress', 'Detachment']),
        'description': 'The Water Bearer. Representing innovation, community, and higher consciousness. Fixed air: the sustained vision of the future.'
    },
    {
        'name': 'Pisces',
        'symbol': '♓',
        'element': 'Water',
        'modality': 'Mutable',
        'ruling_planet': 'Jupiter',
        'exalted_planet': 'Venus',
        'detriment_planet': 'Mercury',
        'fall_planet': 'Mercury',
        'polarity': 'Negative',
        'house_number': 12,
        'body_part': 'Feet, Lymphatic System',
        'tarot_association': 'The Moon (XVIII)',
        'dates_start': '02-19',
        'dates_end': '03-20',
        'keywords': json.dumps(['Compassion', 'Mysticism', 'Imagination', 'Spirituality', 'Escapism', 'Sensitivity']),
        'description': 'The Fishes. Representing dissolution, compassion, and union with the divine. Mutable water: the ocean of consciousness.'
    }
]


def seed_planets(cursor):
    """Insert all planets into the database"""
    print("\nSeeding Planets...")

    for planet in PLANETS:
        cursor.execute("""
            INSERT INTO planets (
                name, symbol, day_of_week, metal, color, gemstone,
                sephiroth_number, rules_signs, exalted_in, detriment_in, fall_in,
                quality, tarot_association, magical_powers, description
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            planet['name'], planet['symbol'], planet['day_of_week'],
            planet['metal'], planet['color'], planet['gemstone'],
            planet['sephiroth_number'], planet['rules_signs'],
            planet['exalted_in'], planet['detriment_in'], planet['fall_in'],
            planet['quality'], planet['tarot_association'],
            planet['magical_powers'], planet['description']
        ))

    print(f"  ✓ Inserted {len(PLANETS)} planets")


def seed_zodiac_signs(cursor):
    """Insert all zodiac signs into the database"""
    print("\nSeeding Zodiac Signs...")

    for sign in ZODIAC_SIGNS:
        cursor.execute("""
            INSERT INTO zodiac_signs (
                name, symbol, element, modality, ruling_planet,
                exalted_planet, detriment_planet, fall_planet, polarity,
                house_number, body_part, tarot_association,
                dates_start, dates_end, keywords, description
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            sign['name'], sign['symbol'], sign['element'], sign['modality'],
            sign['ruling_planet'], sign['exalted_planet'], sign['detriment_planet'],
            sign['fall_planet'], sign['polarity'], sign['house_number'],
            sign['body_part'], sign['tarot_association'], sign['dates_start'],
            sign['dates_end'], sign['keywords'], sign['description']
        ))

    print(f"  ✓ Inserted {len(ZODIAC_SIGNS)} zodiac signs")


if __name__ == '__main__':
    import sqlite3

    # Test the seeding functions
    conn = sqlite3.connect('esoteric_knowledge.db')
    cursor = conn.cursor()

    try:
        seed_planets(cursor)
        seed_zodiac_signs(cursor)
        conn.commit()
        print("\n✓ Astrology data seeded successfully!")
    except Exception as e:
        print(f"\n✗ Error seeding data: {e}")
        conn.rollback()
    finally:
        conn.close()

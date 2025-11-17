"""
Astrology Routes Blueprint
Endpoints for Planets and Zodiac Signs
"""

from flask import Blueprint, jsonify, request, current_app, g
import sqlite3
import json

astrology_bp = Blueprint('astrology', __name__, url_prefix='/api/astrology')


def get_db():
    """Get database connection from Flask g object"""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(current_app.config.get('DATABASE', 'esoteric_knowledge.db'))
        db.row_factory = sqlite3.Row
    return db


def dict_from_row(row):
    """Convert sqlite3.Row to dictionary"""
    if row is None:
        return None
    result = dict(zip(row.keys(), row))

    # Parse JSON fields
    if 'rules_signs' in result and result['rules_signs']:
        try:
            result['rules_signs'] = json.loads(result['rules_signs'])
        except:
            pass

    if 'keywords' in result and result['keywords']:
        try:
            result['keywords'] = json.loads(result['keywords'])
        except:
            pass

    return result


@astrology_bp.route('/planets', methods=['GET'])
def get_all_planets():
    """Get all planets (7 classical + Sun/Moon)"""
    db = get_db()

    planets = db.execute("""
        SELECT p.*, s.name as sephiroth_name
        FROM planets p
        LEFT JOIN sephiroth s ON p.sephiroth_number = s.number
        ORDER BY p.id
    """).fetchall()

    return jsonify({
        'count': len(planets),
        'planets': [dict_from_row(p) for p in planets]
    })


@astrology_bp.route('/planets/<name>', methods=['GET'])
def get_planet_by_name(name):
    """Get a specific planet by name (case-insensitive)"""
    db = get_db()

    planet = db.execute("""
        SELECT p.*, s.name as sephiroth_name
        FROM planets p
        LEFT JOIN sephiroth s ON p.sephiroth_number = s.number
        WHERE LOWER(p.name) = LOWER(?)
    """, (name,)).fetchone()

    if not planet:
        return jsonify({
            'error': f'Planet "{name}" not found',
            'suggestion': 'Valid planets: Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn'
        }), 404

    result = dict_from_row(planet)

    # Get zodiac signs ruled by this planet
    ruled_signs = db.execute("""
        SELECT * FROM zodiac_signs
        WHERE LOWER(ruling_planet) = LOWER(?)
        ORDER BY house_number
    """, (name,)).fetchall()

    if ruled_signs:
        result['rules_zodiac_signs'] = [dict_from_row(s) for s in ruled_signs]

    # Get signs where this planet is exalted
    exalted_signs = db.execute("""
        SELECT name, symbol FROM zodiac_signs
        WHERE LOWER(exalted_planet) = LOWER(?)
    """, (name,)).fetchall()

    if exalted_signs:
        result['exalted_in_signs'] = [dict_from_row(s) for s in exalted_signs]

    return jsonify(result)


@astrology_bp.route('/signs', methods=['GET'])
def get_all_signs():
    """Get all 12 zodiac signs"""
    db = get_db()

    # Optional filtering
    element = request.args.get('element')
    modality = request.args.get('modality')

    where_conditions = []
    params = []

    if element:
        where_conditions.append("LOWER(element) = LOWER(?)")
        params.append(element)

    if modality:
        where_conditions.append("LOWER(modality) = LOWER(?)")
        params.append(modality)

    where_clause = "WHERE " + " AND ".join(where_conditions) if where_conditions else ""

    query = f"""
        SELECT z.*, p.symbol as ruling_planet_symbol, p.day_of_week as ruling_day
        FROM zodiac_signs z
        LEFT JOIN planets p ON z.ruling_planet = p.name
        {where_clause}
        ORDER BY z.house_number
    """

    signs = db.execute(query, params).fetchall()

    return jsonify({
        'count': len(signs),
        'signs': [dict_from_row(s) for s in signs]
    })


@astrology_bp.route('/signs/<name>', methods=['GET'])
def get_sign_by_name(name):
    """Get a specific zodiac sign by name (case-insensitive)"""
    db = get_db()

    sign = db.execute("""
        SELECT z.*, p.symbol as ruling_planet_symbol, p.day_of_week as ruling_day
        FROM zodiac_signs z
        LEFT JOIN planets p ON z.ruling_planet = p.name
        WHERE LOWER(z.name) = LOWER(?)
    """, (name,)).fetchone()

    if not sign:
        return jsonify({
            'error': f'Zodiac sign "{name}" not found',
            'suggestion': 'Valid signs: Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces'
        }), 404

    result = dict_from_row(sign)

    # Get ruling planet details
    if result.get('ruling_planet'):
        planet = db.execute("""
            SELECT * FROM planets WHERE name = ?
        """, (result['ruling_planet'],)).fetchone()

        if planet:
            result['ruling_planet_details'] = dict_from_row(planet)

    # Get tarot card association
    if result.get('tarot_association'):
        # Try to extract card number from tarot_association string
        # e.g., "The Emperor (IV)" -> 4
        import re
        match = re.search(r'The ([A-Za-z\s]+)\s*\(([IVX]+)\)', result['tarot_association'])
        if match:
            card_name = match.group(1).strip()
            card = db.execute("""
                SELECT number, name FROM cards
                WHERE LOWER(name) LIKE LOWER(?)
            """, (f"%{card_name}%",)).fetchone()

            if card:
                result['tarot_card'] = dict_from_row(card)

    return jsonify(result)


@astrology_bp.route('/elements', methods=['GET'])
def get_elements():
    """Get information about the four elements with associated signs and planets"""
    db = get_db()

    elements = ['Fire', 'Earth', 'Air', 'Water']
    result = []

    for element in elements:
        # Get zodiac signs for this element
        signs = db.execute("""
            SELECT name, symbol, modality FROM zodiac_signs
            WHERE element = ?
            ORDER BY house_number
        """, (element,)).fetchall()

        element_data = {
            'element': element,
            'zodiac_signs': [dict_from_row(s) for s in signs],
            'qualities': {
                'Fire': 'Hot, Dry - Active, energetic, passionate',
                'Earth': 'Cold, Dry - Stable, practical, material',
                'Air': 'Hot, Moist - Intellectual, communicative, social',
                'Water': 'Cold, Moist - Emotional, intuitive, receptive'
            }.get(element),
            'tarot_suit': {
                'Fire': 'Wands',
                'Water': 'Cups',
                'Air': 'Swords',
                'Earth': 'Pentacles'
            }.get(element)
        }

        result.append(element_data)

    return jsonify({
        'count': len(result),
        'elements': result
    })


@astrology_bp.route('/modalities', methods=['GET'])
def get_modalities():
    """Get information about the three modalities (Cardinal, Fixed, Mutable)"""
    db = get_db()

    modalities = ['Cardinal', 'Fixed', 'Mutable']
    result = []

    for modality in modalities:
        signs = db.execute("""
            SELECT name, symbol, element FROM zodiac_signs
            WHERE modality = ?
            ORDER BY house_number
        """, (modality,)).fetchall()

        modality_data = {
            'modality': modality,
            'description': {
                'Cardinal': 'Initiating, action-oriented, beginning new cycles',
                'Fixed': 'Sustaining, stable, maintaining and concentrating energy',
                'Mutable': 'Adapting, flexible, transitioning between cycles'
            }.get(modality),
            'zodiac_signs': [dict_from_row(s) for s in signs]
        }

        result.append(modality_data)

    return jsonify({
        'count': len(result),
        'modalities': result
    })


@astrology_bp.route('/planetary-hours', methods=['GET'])
def get_planetary_hours():
    """Get information about planetary hours and days"""
    db = get_db()

    planets = db.execute("""
        SELECT name, symbol, day_of_week, metal, color, magical_powers
        FROM planets
        ORDER BY CASE name
            WHEN 'Sun' THEN 1
            WHEN 'Moon' THEN 2
            WHEN 'Mars' THEN 3
            WHEN 'Mercury' THEN 4
            WHEN 'Jupiter' THEN 5
            WHEN 'Venus' THEN 6
            WHEN 'Saturn' THEN 7
        END
    """).fetchall()

    return jsonify({
        'description': 'Each day is ruled by a planet, and each hour of the day/night cycles through the planetary rulers',
        'note': 'Planetary hours begin at sunrise and sunset, with day and night divided into 12 hours each',
        'planets': [dict_from_row(p) for p in planets],
        'usage': 'Use planetary hours for timing magical operations according to the planet\'s nature'
    })


@astrology_bp.route('/correspondences', methods=['GET'])
def get_astrological_correspondences():
    """Get a summary of all astrological correspondences"""
    db = get_db()

    # Get planets with sephiroth
    planets = db.execute("""
        SELECT p.name, p.symbol, p.day_of_week, s.name as sephiroth
        FROM planets p
        LEFT JOIN sephiroth s ON p.sephiroth_number = s.number
        ORDER BY p.id
    """).fetchall()

    # Get signs with elements and modalities
    signs = db.execute("""
        SELECT name, symbol, element, modality, ruling_planet
        FROM zodiac_signs
        ORDER BY house_number
    """).fetchall()

    return jsonify({
        'planets': {
            'count': len(planets),
            'data': [dict_from_row(p) for p in planets]
        },
        'zodiac_signs': {
            'count': len(signs),
            'data': [dict_from_row(s) for s in signs]
        },
        'elements': ['Fire', 'Earth', 'Air', 'Water'],
        'modalities': ['Cardinal', 'Fixed', 'Mutable'],
        'structure': {
            'planets': 7,
            'signs': 12,
            'elements': 4,
            'modalities': 3,
            'houses': 12
        }
    })

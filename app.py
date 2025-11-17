#!/usr/bin/env python3
"""
Esoteric Knowledge API - A comprehensive REST API for esoteric studies
Includes Tarot, Qabalah, Astrology, and Ritual practices
"""

from flask import Flask, jsonify, request, g
import sqlite3
import os
import random

# Import blueprints
from routes.qabalah import qabalah_bp
from routes.astrology import astrology_bp
from routes.rituals import rituals_bp

app = Flask(__name__)

# Database configuration
DATABASE = 'esoteric_knowledge.db'
app.config['DATABASE'] = DATABASE


def get_db():
    """Get database connection, create if doesn't exist in g"""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  # Enable column access by name
    return db


@app.teardown_appcontext
def close_connection(exception):
    """Close database connection at end of request"""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def dict_from_row(row):
    """Convert sqlite3.Row to dictionary"""
    if row is None:
        return None
    return dict(zip(row.keys(), row))


# Register blueprints
app.register_blueprint(qabalah_bp)
app.register_blueprint(astrology_bp)
app.register_blueprint(rituals_bp)


def get_card_with_details(card_id=None, card_number=None, card_name=None, include_systems=True):
    """
    Get a complete card with all details including keywords and system descriptions

    Args:
        card_id: Internal database ID
        card_number: Card number (0-77)
        card_name: Card name
        include_systems: Whether to include system-specific descriptions
    """
    db = get_db()

    # Build WHERE clause
    where_clause = ""
    params = []
    if card_id is not None:
        where_clause = "WHERE c.id = ?"
        params.append(card_id)
    elif card_number is not None:
        where_clause = "WHERE c.number = ?"
        params.append(card_number)
    elif card_name is not None:
        where_clause = "WHERE LOWER(c.name) = LOWER(?)"
        params.append(card_name)

    # Get card data
    query = f"""
        SELECT c.* FROM cards c {where_clause}
    """
    card_row = db.execute(query, params).fetchone()

    if not card_row:
        return None

    card = dict_from_row(card_row)
    card_id = card['id']

    # Get keywords
    keywords = db.execute(
        "SELECT keyword FROM keywords WHERE card_id = ? ORDER BY keyword",
        (card_id,)
    ).fetchall()
    card['keywords'] = [k['keyword'] for k in keywords]

    # Get system descriptions if requested
    if include_systems:
        systems_query = """
            SELECT system_name, description, upright_meaning, reversed_meaning,
                   key_imagery, divinatory_meaning, esoteric_meaning
            FROM system_descriptions
            WHERE card_id = ?
        """
        system_rows = db.execute(systems_query, (card_id,)).fetchall()
        card['system_descriptions'] = {
            row['system_name']: {
                'description': row['description'],
                'upright_meaning': row['upright_meaning'],
                'reversed_meaning': row['reversed_meaning'],
                'key_imagery': row['key_imagery'],
                'divinatory_meaning': row['divinatory_meaning'],
                'esoteric_meaning': row['esoteric_meaning']
            }
            for row in system_rows
        }

    # Remove internal id from response
    del card['id']
    del card['created_at']
    del card['updated_at']

    return card


@app.route('/', methods=['GET'])
def home():
    """Home endpoint with API documentation"""
    return jsonify({
        'message': 'Welcome to the Esoteric Knowledge API',
        'description': 'A comprehensive REST API for esoteric studies including Tarot, Qabalah, Astrology, and Ritual practices',
        'version': '3.0.0',
        'features': [
            'Complete 78-card tarot deck with multiple system descriptions',
            'Tree of Life: 10 Sephiroth and 22 Paths',
            'Astrological correspondences: Planets and Zodiac Signs',
            'Esoteric rituals from Golden Dawn and Hermetic traditions',
            'Cross-referenced correspondences between all systems',
            'Comprehensive filtering and search capabilities'
        ],
        'endpoints': {
            'tarot': {
                '/cards': 'Get all tarot cards',
                '/cards/<number>': 'Get card by number (0-77)',
                '/cards/name/<name>': 'Get card by name',
                '/cards/random': 'Get random card',
                '/cards/search?q=<query>': 'Search cards',
                '/cards/<number>/correspondences': 'Get card with full qabalah & astrology links',
                '/systems': 'List tarot systems'
            },
            'qabalah': {
                '/api/qabalah/sephiroth': 'Get all 10 Sephiroth',
                '/api/qabalah/sephiroth/<number>': 'Get Sephirah by number (1-10)',
                '/api/qabalah/sephiroth/name/<name>': 'Get Sephirah by name',
                '/api/qabalah/paths': 'Get all 22 Paths',
                '/api/qabalah/paths/<number>': 'Get Path by number (11-32)',
                '/api/qabalah/paths/<number>/card': 'Get Path with full tarot card data',
                '/api/qabalah/tree': 'Get complete Tree of Life structure'
            },
            'astrology': {
                '/api/astrology/planets': 'Get all planets',
                '/api/astrology/planets/<name>': 'Get planet by name',
                '/api/astrology/signs': 'Get all zodiac signs',
                '/api/astrology/signs/<name>': 'Get sign by name',
                '/api/astrology/elements': 'Get elemental correspondences',
                '/api/astrology/modalities': 'Get modality information',
                '/api/astrology/correspondences': 'Get all astrological correspondences'
            },
            'rituals': {
                '/api/rituals': 'Get all rituals',
                '/api/rituals/<id>': 'Get ritual by ID',
                '/api/rituals/name/<name>': 'Get ritual by name or abbreviation',
                '/api/rituals/beginner': 'Get beginner-friendly rituals',
                '/api/rituals/daily': 'Get daily practice rituals',
                '/api/rituals/search?q=<query>': 'Search rituals',
                '/api/rituals/practice-guide': 'Get practice progression guide'
            }
        },
        'examples': [
            '/cards/0/correspondences',
            '/api/qabalah/tree',
            '/api/qabalah/paths/11/card',
            '/api/astrology/planets/Venus',
            '/api/astrology/signs/Leo',
            '/api/rituals/name/LBRP',
            '/api/rituals?difficulty=Beginner'
        ]
    })


@app.route('/systems', methods=['GET'])
def get_systems():
    """Get list of available tarot systems"""
    db = get_db()
    systems = db.execute("""
        SELECT DISTINCT system_name,
               COUNT(*) as card_count
        FROM system_descriptions
        GROUP BY system_name
        ORDER BY system_name
    """).fetchall()

    return jsonify({
        'systems': [
            {
                'name': s['system_name'],
                'card_count': s['card_count'],
                'full_name': {
                    'RWS': 'Rider-Waite-Smith',
                    'Thoth': 'Thoth (Crowley-Harris)',
                    'Golden Dawn': 'Hermetic Order of the Golden Dawn',
                    'Marseille': 'Tarot de Marseille'
                }.get(s['system_name'], s['system_name'])
            }
            for s in systems
        ]
    })


@app.route('/cards', methods=['GET'])
def get_all_cards():
    """Get all tarot cards with optional filtering"""
    db = get_db()

    # Get filter parameters
    arcana = request.args.get('arcana')
    suit = request.args.get('suit')
    element = request.args.get('element')
    include_systems = request.args.get('systems', 'true').lower() == 'true'

    # Build WHERE clause
    where_conditions = []
    params = []

    if arcana:
        where_conditions.append("c.arcana = ?")
        params.append(arcana)

    if suit:
        where_conditions.append("LOWER(c.suit) = LOWER(?)")
        params.append(suit)

    if element:
        where_conditions.append("LOWER(c.element) = LOWER(?)")
        params.append(element)

    where_clause = "WHERE " + " AND ".join(where_conditions) if where_conditions else ""

    # Get cards
    query = f"""
        SELECT c.id, c.number
        FROM cards c
        {where_clause}
        ORDER BY c.number
    """
    card_rows = db.execute(query, params).fetchall()

    # Get full details for each card
    cards = []
    for row in card_rows:
        card = get_card_with_details(card_id=row['id'], include_systems=include_systems)
        if card:
            cards.append(card)

    return jsonify({
        'count': len(cards),
        'cards': cards
    })


@app.route('/cards/<int:number>', methods=['GET'])
def get_card_by_number(number):
    """Get a specific card by its number (0-77)"""
    include_systems = request.args.get('systems', 'true').lower() == 'true'

    card = get_card_with_details(card_number=number, include_systems=include_systems)

    if not card:
        return jsonify({
            'error': f'Card number must be between 0 and 77'
        }), 404

    return jsonify(card)


@app.route('/cards/name/<card_name>', methods=['GET'])
def get_card_by_name(card_name):
    """Get a specific card by its name (case-insensitive)"""
    include_systems = request.args.get('systems', 'true').lower() == 'true'

    card = get_card_with_details(card_name=card_name, include_systems=include_systems)

    if not card:
        return jsonify({
            'error': f'Card "{card_name}" not found',
            'suggestion': 'Try using the exact card name or use /cards/search?q=<query> to search'
        }), 404

    return jsonify(card)


@app.route('/cards/<int:number>/system/<system_name>', methods=['GET'])
def get_card_system_description(number, system_name):
    """Get a specific card's description from a specific tarot system"""
    db = get_db()

    # Validate system name
    valid_systems = ['RWS', 'Thoth', 'Golden Dawn', 'Marseille']
    if system_name not in valid_systems:
        return jsonify({
            'error': f'Invalid system name. Valid systems: {", ".join(valid_systems)}'
        }), 400

    # Get card and system description
    query = """
        SELECT c.number, c.name, sd.*
        FROM cards c
        LEFT JOIN system_descriptions sd ON c.id = sd.card_id AND sd.system_name = ?
        WHERE c.number = ?
    """
    row = db.execute(query, (system_name, number)).fetchone()

    if not row:
        return jsonify({
            'error': f'Card number {number} not found'
        }), 404

    result = {
        'number': row['number'],
        'name': row['name'],
        'system': system_name
    }

    if row['description']:
        result.update({
            'description': row['description'],
            'upright_meaning': row['upright_meaning'],
            'reversed_meaning': row['reversed_meaning'],
            'key_imagery': row['key_imagery'],
            'divinatory_meaning': row['divinatory_meaning'],
            'esoteric_meaning': row['esoteric_meaning']
        })
    else:
        result['message'] = f'No {system_name} description available for this card yet'

    return jsonify(result)


@app.route('/cards/random', methods=['GET'])
def get_random_card():
    """Get a random tarot card"""
    include_systems = request.args.get('systems', 'true').lower() == 'true'

    # Get random card number
    card_number = random.randint(0, 77)
    card = get_card_with_details(card_number=card_number, include_systems=include_systems)

    return jsonify(card)


@app.route('/cards/search', methods=['GET'])
def search_cards():
    """Search cards by keyword in name, keywords, meanings, or correspondences"""
    db = get_db()
    query = request.args.get('q', '').lower()
    include_systems = request.args.get('systems', 'true').lower() == 'true'

    if not query:
        return jsonify({
            'error': 'Please provide a search query using ?q=<query>'
        }), 400

    # Search in multiple fields
    search_query = """
        SELECT DISTINCT c.id
        FROM cards c
        LEFT JOIN keywords k ON c.id = k.card_id
        WHERE
            LOWER(c.name) LIKE ?
            OR LOWER(c.upright_meaning) LIKE ?
            OR LOWER(c.reversed_meaning) LIKE ?
            OR LOWER(c.description) LIKE ?
            OR LOWER(k.keyword) LIKE ?
            OR LOWER(c.element) LIKE ?
            OR LOWER(c.hebrew_letter) LIKE ?
            OR LOWER(c.color_primary) LIKE ?
            OR LOWER(c.gemstone) LIKE ?
        ORDER BY c.number
    """

    search_pattern = f"%{query}%"
    params = [search_pattern] * 9

    card_rows = db.execute(search_query, params).fetchall()

    # Get full details for each card
    results = []
    for row in card_rows:
        card = get_card_with_details(card_id=row['id'], include_systems=include_systems)
        if card:
            results.append(card)

    return jsonify({
        'query': query,
        'count': len(results),
        'results': results
    })


@app.route('/cards/<int:number>/correspondences', methods=['GET'])
def get_card_correspondences(number):
    """Get a tarot card with full qabalah and astrological correspondences"""
    db = get_db()

    # Get the card
    card = get_card_with_details(card_number=number, include_systems=False)

    if not card:
        return jsonify({
            'error': f'Card number {number} not found'
        }), 404

    result = {'card': card}

    # For Major Arcana, get the Path correspondence
    if card['arcana'] == 'Major Arcana':
        # Get path that corresponds to this card
        path_query = """
            SELECT p.*, s1.name as from_sephirah_name, s2.name as to_sephirah_name
            FROM paths p
            LEFT JOIN cards c ON p.tarot_card_id = c.id
            LEFT JOIN sephiroth s1 ON p.connects_from = s1.number
            LEFT JOIN sephiroth s2 ON p.connects_to = s2.number
            WHERE c.number = ?
        """
        path = db.execute(path_query, (number,)).fetchone()

        if path:
            path_dict = dict_from_row(path)
            # Remove internal IDs
            if 'id' in path_dict:
                del path_dict['id']
            if 'tarot_card_id' in path_dict:
                del path_dict['tarot_card_id']
            result['qabalah_path'] = path_dict

            # Get the connected sephiroth details
            seph_from = db.execute("""
                SELECT * FROM sephiroth WHERE number = ?
            """, (path['connects_from'],)).fetchone()

            seph_to = db.execute("""
                SELECT * FROM sephiroth WHERE number = ?
            """, (path['connects_to'],)).fetchone()

            result['connected_sephiroth'] = {
                'from': dict_from_row(seph_from),
                'to': dict_from_row(seph_to)
            }

    # Get astrological correspondences
    astrology_data = {}

    # Check for planetary association
    if card.get('astrology'):
        # Try to find matching planet
        planet = db.execute("""
            SELECT * FROM planets
            WHERE LOWER(name) = LOWER(?)
        """, (card['astrology'],)).fetchone()

        if planet:
            astrology_data['planet'] = dict_from_row(planet)

    # For cards with zodiac associations, find the sign
    if card.get('astrology'):
        sign = db.execute("""
            SELECT * FROM zodiac_signs
            WHERE LOWER(name) = LOWER(?)
        """, (card['astrology'],)).fetchone()

        if sign:
            sign_dict = dict_from_row(sign)
            astrology_data['zodiac_sign'] = sign_dict

            # Get ruling planet of the sign
            if sign['ruling_planet']:
                ruling_planet = db.execute("""
                    SELECT * FROM planets WHERE name = ?
                """, (sign['ruling_planet'],)).fetchone()

                if ruling_planet:
                    astrology_data['ruling_planet'] = dict_from_row(ruling_planet)

    if astrology_data:
        result['astrology'] = astrology_data

    # Add element correspondences
    if card.get('element'):
        # Get all signs of this element
        element_signs = db.execute("""
            SELECT name, symbol, modality FROM zodiac_signs
            WHERE LOWER(element) = LOWER(?)
            ORDER BY house_number
        """, (card['element'],)).fetchall()

        if element_signs:
            result['elemental_zodiac'] = [dict_from_row(s) for s in element_signs]

    return jsonify(result)


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found',
        'message': 'Visit / for API documentation'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error',
        'message': str(error)
    }), 500


if __name__ == '__main__':
    # Check if database exists
    if not os.path.exists(DATABASE):
        print(f"ERROR: Database file '{DATABASE}' not found!")
        print("Please run 'python3 migrate_to_sqlite.py' first to create the database.")
        exit(1)

    # Run the Flask development server
    print("="*60)
    print("Esoteric Knowledge API v3.0")
    print("="*60)
    print(f"Database: {DATABASE}")
    print("Server starting on http://0.0.0.0:5000")
    print("Visit http://0.0.0.0:5000 for API documentation")
    print("="*60)
    app.run(host='0.0.0.0', port=5000, debug=True)

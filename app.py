#!/usr/bin/env python3
"""
TarotAPI - A comprehensive REST API for fetching tarot cards
Now with SQLite database, esoteric correspondences, and multi-system descriptions
"""

from flask import Flask, jsonify, request, g
import sqlite3
import os
import random

app = Flask(__name__)

# Database configuration
DATABASE = 'tarot.db'


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
        'message': 'Welcome to TarotAPI',
        'description': 'A comprehensive API for fetching tarot cards with esoteric correspondences and multi-system descriptions',
        'version': '2.0.0',
        'features': [
            'Complete 78-card tarot deck',
            'Qabbalah correspondences (Tree of Life, Hebrew letters, Sephiroth)',
            'Esoteric associations (musical notes, colors, gemstones, herbs)',
            'Descriptions from 4 major systems: RWS, Thoth, Golden Dawn, Marseille',
            'Flexible filtering and search'
        ],
        'endpoints': {
            '/': 'API documentation (this page)',
            '/cards': 'Get all tarot cards (supports filtering)',
            '/cards/<number>': 'Get a specific card by number (0-77)',
            '/cards/name/<card_name>': 'Get a specific card by name',
            '/cards/random': 'Get a random card',
            '/cards/search?q=<query>': 'Search cards by keyword',
            '/systems': 'List available tarot systems',
            '/cards/<number>/system/<system_name>': 'Get system-specific description'
        },
        'filters': {
            '/cards': [
                'arcana=Major Arcana|Minor Arcana',
                'suit=Wands|Cups|Swords|Pentacles',
                'element=Fire|Water|Air|Earth',
                'systems=true|false (include system descriptions, default: true)'
            ]
        },
        'examples': [
            '/cards/0',
            '/cards/name/The Fool',
            '/cards/name/ace of cups',
            '/cards?arcana=Major Arcana',
            '/cards?suit=Cups&element=Water',
            '/cards/random',
            '/cards/search?q=love',
            '/cards/0/system/Thoth',
            '/systems'
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
    print("TarotAPI v2.0 - SQLite Edition")
    print("="*60)
    print(f"Database: {DATABASE}")
    print("Server starting on http://0.0.0.0:5000")
    print("Visit http://0.0.0.0:5000 for API documentation")
    print("="*60)
    app.run(host='0.0.0.0', port=5000, debug=True)

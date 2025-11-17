#!/usr/bin/env python3
"""
TarotAPI - A simple REST API for fetching tarot cards
"""

from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Load tarot card data
def load_tarot_data():
    """Load tarot card data from JSON file"""
    data_file = os.path.join(os.path.dirname(__file__), 'tarot_data.json')
    with open(data_file, 'r') as f:
        return json.load(f)

# Load data once at startup
TAROT_DATA = load_tarot_data()
CARDS = TAROT_DATA['cards']

# Create a mapping of card names to card data for faster lookup
CARD_NAME_MAP = {card['name'].lower(): card for card in CARDS}


@app.route('/', methods=['GET'])
def home():
    """Home endpoint with API documentation"""
    return jsonify({
        'message': 'Welcome to TarotAPI',
        'description': 'A simple API for fetching tarot cards with correspondences',
        'version': '1.0.0',
        'endpoints': {
            '/': 'API documentation (this page)',
            '/cards': 'Get all tarot cards',
            '/cards/<number>': 'Get a specific card by number (0-77)',
            '/cards/name/<card_name>': 'Get a specific card by name',
            '/cards/random': 'Get a random card',
            '/cards/search?q=<query>': 'Search cards by keyword'
        },
        'examples': [
            '/cards/0',
            '/cards/name/The Fool',
            '/cards/name/ace of cups',
            '/cards/random',
            '/cards/search?q=love'
        ]
    })


@app.route('/cards', methods=['GET'])
def get_all_cards():
    """Get all tarot cards"""
    # Optional filters
    arcana = request.args.get('arcana')
    suit = request.args.get('suit')
    element = request.args.get('element')

    filtered_cards = CARDS

    if arcana:
        filtered_cards = [c for c in filtered_cards if c['arcana'].lower() == arcana.lower()]

    if suit:
        filtered_cards = [c for c in filtered_cards if c.get('suit') and c['suit'].lower() == suit.lower()]

    if element:
        filtered_cards = [c for c in filtered_cards if c.get('element') and c['element'].lower() == element.lower()]

    return jsonify({
        'count': len(filtered_cards),
        'cards': filtered_cards
    })


@app.route('/cards/<int:number>', methods=['GET'])
def get_card_by_number(number):
    """Get a specific card by its number (0-77)"""
    if number < 0 or number >= len(CARDS):
        return jsonify({
            'error': f'Card number must be between 0 and {len(CARDS)-1}'
        }), 404

    card = CARDS[number]
    return jsonify(card)


@app.route('/cards/name/<card_name>', methods=['GET'])
def get_card_by_name(card_name):
    """Get a specific card by its name (case-insensitive)"""
    card_name_lower = card_name.lower()

    if card_name_lower in CARD_NAME_MAP:
        return jsonify(CARD_NAME_MAP[card_name_lower])

    return jsonify({
        'error': f'Card "{card_name}" not found',
        'suggestion': 'Try using the exact card name or use /cards/search?q=<query> to search'
    }), 404


@app.route('/cards/random', methods=['GET'])
def get_random_card():
    """Get a random tarot card"""
    import random
    card = random.choice(CARDS)
    return jsonify(card)


@app.route('/cards/search', methods=['GET'])
def search_cards():
    """Search cards by keyword in name, keywords, or meanings"""
    query = request.args.get('q', '').lower()

    if not query:
        return jsonify({
            'error': 'Please provide a search query using ?q=<query>'
        }), 400

    results = []
    for card in CARDS:
        # Search in name
        if query in card['name'].lower():
            results.append(card)
            continue

        # Search in keywords
        if any(query in keyword.lower() for keyword in card['keywords']):
            results.append(card)
            continue

        # Search in meanings
        if (query in card['upright_meaning'].lower() or
            query in card['reversed_meaning'].lower() or
            query in card['description'].lower()):
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
    # Run the Flask development server
    app.run(host='0.0.0.0', port=5000, debug=True)

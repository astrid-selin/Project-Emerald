"""
Qabalah Routes Blueprint
Endpoints for the Tree of Life: Sephiroth and Paths
"""

from flask import Blueprint, jsonify, request, current_app, g
import sqlite3

qabalah_bp = Blueprint('qabalah', __name__, url_prefix='/api/qabalah')


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
    return dict(zip(row.keys(), row))


@qabalah_bp.route('/sephiroth', methods=['GET'])
def get_all_sephiroth():
    """Get all 10 Sephiroth on the Tree of Life"""
    db = get_db()

    sephiroth = db.execute("""
        SELECT * FROM sephiroth
        ORDER BY number
    """).fetchall()

    return jsonify({
        'count': len(sephiroth),
        'sephiroth': [dict_from_row(s) for s in sephiroth]
    })


@qabalah_bp.route('/sephiroth/<int:number>', methods=['GET'])
def get_sephirah_by_number(number):
    """Get a specific Sephirah by its number (1-10)"""
    db = get_db()

    if number < 1 or number > 10:
        return jsonify({
            'error': 'Sephirah number must be between 1 and 10'
        }), 400

    sephirah = db.execute("""
        SELECT * FROM sephiroth WHERE number = ?
    """, (number,)).fetchone()

    if not sephirah:
        return jsonify({
            'error': f'Sephirah {number} not found'
        }), 404

    # Get paths connected to this sephirah
    paths_from = db.execute("""
        SELECT p.*, c.number as card_number, c.name as card_name
        FROM paths p
        LEFT JOIN cards c ON p.tarot_card_id = c.id
        WHERE p.connects_from = ?
        ORDER BY p.number
    """, (number,)).fetchall()

    paths_to = db.execute("""
        SELECT p.*, c.number as card_number, c.name as card_name
        FROM paths p
        LEFT JOIN cards c ON p.tarot_card_id = c.id
        WHERE p.connects_to = ?
        ORDER BY p.number
    """, (number,)).fetchall()

    result = dict_from_row(sephirah)
    result['paths_emanating'] = [dict_from_row(p) for p in paths_from]
    result['paths_receiving'] = [dict_from_row(p) for p in paths_to]

    return jsonify(result)


@qabalah_bp.route('/paths', methods=['GET'])
def get_all_paths():
    """Get all 22 Paths connecting the Sephiroth"""
    db = get_db()

    paths = db.execute("""
        SELECT p.*, c.number as card_number, c.name as card_name,
               s1.name as from_sephirah_name, s2.name as to_sephirah_name
        FROM paths p
        LEFT JOIN cards c ON p.tarot_card_id = c.id
        LEFT JOIN sephiroth s1 ON p.connects_from = s1.number
        LEFT JOIN sephiroth s2 ON p.connects_to = s2.number
        ORDER BY p.number
    """).fetchall()

    return jsonify({
        'count': len(paths),
        'paths': [dict_from_row(p) for p in paths]
    })


@qabalah_bp.route('/paths/<int:number>', methods=['GET'])
def get_path_by_number(number):
    """Get a specific Path by its number (11-32)"""
    db = get_db()

    if number < 11 or number > 32:
        return jsonify({
            'error': 'Path number must be between 11 and 32'
        }), 400

    path = db.execute("""
        SELECT p.*, c.number as card_number, c.name as card_name,
               s1.name as from_sephirah_name, s2.name as to_sephirah_name
        FROM paths p
        LEFT JOIN cards c ON p.tarot_card_id = c.id
        LEFT JOIN sephiroth s1 ON p.connects_from = s1.number
        LEFT JOIN sephiroth s2 ON p.connects_to = s2.number
        WHERE p.number = ?
    """, (number,)).fetchone()

    if not path:
        return jsonify({
            'error': f'Path {number} not found'
        }), 404

    return jsonify(dict_from_row(path))


@qabalah_bp.route('/paths/<int:number>/card', methods=['GET'])
def get_path_with_card(number):
    """Get a Path with full tarot card details"""
    db = get_db()

    if number < 11 or number > 32:
        return jsonify({
            'error': 'Path number must be between 11 and 32'
        }), 400

    path = db.execute("""
        SELECT p.*, s1.name as from_sephirah_name, s2.name as to_sephirah_name
        FROM paths p
        LEFT JOIN sephiroth s1 ON p.connects_from = s1.number
        LEFT JOIN sephiroth s2 ON p.connects_to = s2.number
        WHERE p.number = ?
    """, (number,)).fetchone()

    if not path:
        return jsonify({
            'error': f'Path {number} not found'
        }), 404

    result = dict_from_row(path)

    # Get full tarot card details if available
    if path['tarot_card_id']:
        card = db.execute("""
            SELECT * FROM cards WHERE id = ?
        """, (path['tarot_card_id'],)).fetchone()

        if card:
            card_dict = dict_from_row(card)

            # Get keywords
            keywords = db.execute("""
                SELECT keyword FROM keywords WHERE card_id = ?
            """, (path['tarot_card_id'],)).fetchall()
            card_dict['keywords'] = [k['keyword'] for k in keywords]

            # Remove internal fields
            del card_dict['id']
            if 'created_at' in card_dict:
                del card_dict['created_at']
            if 'updated_at' in card_dict:
                del card_dict['updated_at']

            result['tarot_card'] = card_dict

    # Remove the internal ID from path
    if 'id' in result:
        del result['id']
    if 'tarot_card_id' in result:
        del result['tarot_card_id']

    return jsonify(result)


@qabalah_bp.route('/tree', methods=['GET'])
def get_tree_of_life():
    """Get the complete Tree of Life structure with all Sephiroth and Paths"""
    db = get_db()

    # Get all sephiroth
    sephiroth = db.execute("""
        SELECT * FROM sephiroth ORDER BY number
    """).fetchall()

    # Get all paths with connections
    paths = db.execute("""
        SELECT p.*, c.number as card_number, c.name as card_name,
               s1.name as from_sephirah_name, s2.name as to_sephirah_name
        FROM paths p
        LEFT JOIN cards c ON p.tarot_card_id = c.id
        LEFT JOIN sephiroth s1 ON p.connects_from = s1.number
        LEFT JOIN sephiroth s2 ON p.connects_to = s2.number
        ORDER BY p.number
    """).fetchall()

    return jsonify({
        'name': 'Tree of Life',
        'description': 'The Qabalistic Tree of Life: 10 Sephiroth connected by 22 Paths corresponding to the Major Arcana',
        'sephiroth': {
            'count': len(sephiroth),
            'spheres': [dict_from_row(s) for s in sephiroth]
        },
        'paths': {
            'count': len(paths),
            'connections': [dict_from_row(p) for p in paths]
        }
    })


@qabalah_bp.route('/sephiroth/name/<name>', methods=['GET'])
def get_sephirah_by_name(name):
    """Get a Sephirah by its name (case-insensitive)"""
    db = get_db()

    sephirah = db.execute("""
        SELECT * FROM sephiroth WHERE LOWER(name) = LOWER(?)
    """, (name,)).fetchone()

    if not sephirah:
        return jsonify({
            'error': f'Sephirah "{name}" not found',
            'suggestion': 'Valid names: Kether, Chokmah, Binah, Chesed, Geburah, Tiphareth, Netzach, Hod, Yesod, Malkuth'
        }), 404

    result = dict_from_row(sephirah)
    seph_number = result['number']

    # Get connected paths
    paths_from = db.execute("""
        SELECT p.*, c.number as card_number, c.name as card_name
        FROM paths p
        LEFT JOIN cards c ON p.tarot_card_id = c.id
        WHERE p.connects_from = ?
    """, (seph_number,)).fetchall()

    paths_to = db.execute("""
        SELECT p.*, c.number as card_number, c.name as card_name
        FROM paths p
        LEFT JOIN cards c ON p.tarot_card_id = c.id
        WHERE p.connects_to = ?
    """, (seph_number,)).fetchall()

    result['paths_emanating'] = [dict_from_row(p) for p in paths_from]
    result['paths_receiving'] = [dict_from_row(p) for p in paths_to]

    return jsonify(result)

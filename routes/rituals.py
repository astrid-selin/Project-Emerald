"""
Rituals Routes Blueprint
Endpoints for Esoteric Rituals and Practices
"""

from flask import Blueprint, jsonify, request, current_app, g
import sqlite3
import json

rituals_bp = Blueprint('rituals', __name__, url_prefix='/api/rituals')


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
    if 'requires_tools' in result and result['requires_tools']:
        try:
            result['requires_tools'] = json.loads(result['requires_tools'])
        except:
            pass

    return result


@rituals_bp.route('', methods=['GET'])
def get_all_rituals():
    """Get all rituals with optional filtering"""
    db = get_db()

    # Optional filtering
    tradition = request.args.get('tradition')
    category = request.args.get('category')
    difficulty = request.args.get('difficulty')
    include_instructions = request.args.get('instructions', 'true').lower() == 'true'

    where_conditions = []
    params = []

    if tradition:
        where_conditions.append("LOWER(tradition) = LOWER(?)")
        params.append(tradition)

    if category:
        where_conditions.append("LOWER(category) = LOWER(?)")
        params.append(category)

    if difficulty:
        where_conditions.append("LOWER(difficulty) = LOWER(?)")
        params.append(difficulty)

    where_clause = "WHERE " + " AND ".join(where_conditions) if where_conditions else ""

    # Select fields based on whether full instructions are requested
    if include_instructions:
        fields = "*"
    else:
        fields = """id, name, abbreviation, tradition, category, purpose,
                    difficulty, duration_minutes, elemental_focus, sephiroth_focus,
                    planetary_focus, timing_notes, benefits, warnings, source, description"""

    query = f"""
        SELECT {fields} FROM rituals
        {where_clause}
        ORDER BY
            CASE difficulty
                WHEN 'Beginner' THEN 1
                WHEN 'Intermediate' THEN 2
                WHEN 'Advanced' THEN 3
                WHEN 'Expert' THEN 4
            END,
            name
    """

    rituals = db.execute(query, params).fetchall()

    return jsonify({
        'count': len(rituals),
        'rituals': [dict_from_row(r) for r in rituals]
    })


@rituals_bp.route('/<int:ritual_id>', methods=['GET'])
def get_ritual_by_id(ritual_id):
    """Get a specific ritual by ID with full details"""
    db = get_db()

    ritual = db.execute("""
        SELECT * FROM rituals WHERE id = ?
    """, (ritual_id,)).fetchone()

    if not ritual:
        return jsonify({
            'error': f'Ritual {ritual_id} not found'
        }), 404

    return jsonify(dict_from_row(ritual))


@rituals_bp.route('/name/<name>', methods=['GET'])
def get_ritual_by_name(name):
    """Get a ritual by name or abbreviation (case-insensitive)"""
    db = get_db()

    ritual = db.execute("""
        SELECT * FROM rituals
        WHERE LOWER(name) = LOWER(?) OR LOWER(abbreviation) = LOWER(?)
    """, (name, name)).fetchone()

    if not ritual:
        return jsonify({
            'error': f'Ritual "{name}" not found',
            'suggestion': 'Try searching by abbreviation (e.g., LBRP, MPR, BRH) or use /api/rituals to see all available rituals'
        }), 404

    return jsonify(dict_from_row(ritual))


@rituals_bp.route('/traditions', methods=['GET'])
def get_traditions():
    """Get list of all ritual traditions"""
    db = get_db()

    traditions = db.execute("""
        SELECT DISTINCT tradition, COUNT(*) as ritual_count
        FROM rituals
        GROUP BY tradition
        ORDER BY tradition
    """).fetchall()

    return jsonify({
        'count': len(traditions),
        'traditions': [dict_from_row(t) for t in traditions]
    })


@rituals_bp.route('/categories', methods=['GET'])
def get_categories():
    """Get list of all ritual categories"""
    db = get_db()

    categories = db.execute("""
        SELECT DISTINCT category, COUNT(*) as ritual_count
        FROM rituals
        GROUP BY category
        ORDER BY category
    """).fetchall()

    return jsonify({
        'count': len(categories),
        'categories': [dict_from_row(c) for c in categories]
    })


@rituals_bp.route('/beginner', methods=['GET'])
def get_beginner_rituals():
    """Get all beginner-friendly rituals"""
    db = get_db()

    rituals = db.execute("""
        SELECT * FROM rituals
        WHERE difficulty = 'Beginner'
        ORDER BY duration_minutes
    """).fetchall()

    return jsonify({
        'count': len(rituals),
        'message': 'Beginner-friendly rituals safe for daily practice',
        'rituals': [dict_from_row(r) for r in rituals]
    })


@rituals_bp.route('/daily', methods=['GET'])
def get_daily_practices():
    """Get rituals suitable for daily practice"""
    db = get_db()

    rituals = db.execute("""
        SELECT * FROM rituals
        WHERE difficulty IN ('Beginner', 'Intermediate')
        AND duration_minutes <= 25
        ORDER BY difficulty, duration_minutes
    """).fetchall()

    return jsonify({
        'count': len(rituals),
        'message': 'Rituals suitable for daily practice (under 25 minutes)',
        'suggestion': 'Start with LBRP, then add Middle Pillar as you progress',
        'rituals': [dict_from_row(r) for r in rituals]
    })


@rituals_bp.route('/search', methods=['GET'])
def search_rituals():
    """Search rituals by keyword in name, purpose, or description"""
    db = get_db()

    query = request.args.get('q', '').lower()

    if not query:
        return jsonify({
            'error': 'Please provide a search query using ?q=<query>'
        }), 400

    search_pattern = f"%{query}%"

    rituals = db.execute("""
        SELECT * FROM rituals
        WHERE LOWER(name) LIKE ?
        OR LOWER(abbreviation) LIKE ?
        OR LOWER(purpose) LIKE ?
        OR LOWER(description) LIKE ?
        OR LOWER(category) LIKE ?
        OR LOWER(benefits) LIKE ?
        ORDER BY
            CASE difficulty
                WHEN 'Beginner' THEN 1
                WHEN 'Intermediate' THEN 2
                WHEN 'Advanced' THEN 3
                WHEN 'Expert' THEN 4
            END
    """, (search_pattern, search_pattern, search_pattern,
          search_pattern, search_pattern, search_pattern)).fetchall()

    return jsonify({
        'query': query,
        'count': len(rituals),
        'rituals': [dict_from_row(r) for r in rituals]
    })


@rituals_bp.route('/by-planet/<planet>', methods=['GET'])
def get_rituals_by_planet(planet):
    """Get rituals associated with a specific planet"""
    db = get_db()

    rituals = db.execute("""
        SELECT * FROM rituals
        WHERE LOWER(planetary_focus) LIKE LOWER(?)
        ORDER BY difficulty
    """, (f"%{planet}%",)).fetchall()

    if not rituals:
        return jsonify({
            'planet': planet,
            'count': 0,
            'message': f'No rituals specifically focused on {planet}',
            'rituals': []
        })

    return jsonify({
        'planet': planet,
        'count': len(rituals),
        'rituals': [dict_from_row(r) for r in rituals]
    })


@rituals_bp.route('/by-element/<element>', methods=['GET'])
def get_rituals_by_element(element):
    """Get rituals associated with a specific element"""
    db = get_db()

    rituals = db.execute("""
        SELECT * FROM rituals
        WHERE LOWER(elemental_focus) = LOWER(?)
        ORDER BY difficulty
    """, (element,)).fetchall()

    if not rituals:
        return jsonify({
            'element': element,
            'count': 0,
            'message': f'No rituals specifically focused on {element}',
            'rituals': []
        })

    return jsonify({
        'element': element,
        'count': len(rituals),
        'rituals': [dict_from_row(r) for r in rituals]
    })


@rituals_bp.route('/practice-guide', methods=['GET'])
def get_practice_guide():
    """Get a suggested practice progression guide"""
    db = get_db()

    # Get foundational rituals
    foundation = db.execute("""
        SELECT id, name, abbreviation, difficulty, duration_minutes, purpose
        FROM rituals
        WHERE abbreviation IN ('LBRP', 'LIRP')
        ORDER BY name
    """).fetchall()

    intermediate = db.execute("""
        SELECT id, name, abbreviation, difficulty, duration_minutes, purpose
        FROM rituals
        WHERE difficulty = 'Intermediate'
        ORDER BY name
    """).fetchall()

    advanced = db.execute("""
        SELECT id, name, abbreviation, difficulty, duration_minutes, purpose
        FROM rituals
        WHERE difficulty IN ('Advanced', 'Expert')
        ORDER BY difficulty, name
    """).fetchall()

    return jsonify({
        'title': 'Suggested Practice Progression',
        'stages': {
            'foundation': {
                'description': 'Master these first - the cornerstone practices',
                'duration': '1-3 months of daily practice',
                'rituals': [dict_from_row(r) for r in foundation]
            },
            'intermediate': {
                'description': 'Build on the foundation with these practices',
                'duration': '3-12 months of regular practice',
                'rituals': [dict_from_row(r) for r in intermediate]
            },
            'advanced': {
                'description': 'Advanced practices requiring extensive preparation',
                'duration': 'After solid foundation in earlier practices',
                'rituals': [dict_from_row(r) for r in advanced]
            }
        },
        'notes': [
            'Daily LBRP practice is recommended for all levels',
            'Always learn from a qualified teacher for advanced practices',
            'Keep a magical diary to track your progress',
            'Consistency is more important than complexity'
        ]
    })

# TarotAPI v2.0

A comprehensive REST API for fetching tarot cards with extensive esoteric correspondences and multi-system descriptions. Built with Python, Flask, and SQLite.

## Features

### Complete Tarot Deck
- Full deck of 78 tarot cards (22 Major Arcana + 56 Minor Arcana)
- SQLite database for efficient querying and filtering

### Rich Card Data
Each card includes:
- **Basic Information**: Name, number, arcana type, suit
- **Traditional Correspondences**: Element, astrological associations, astrological decans
- **Qabbalah**: Hebrew letters, Tree of Life paths, Sephiroth
- **Esoteric Associations**: Musical notes, colors (primary & secondary), gemstones, herbs
- **Symbolism**: Key symbols and imagery
- **Meanings**: Keywords, upright meanings, reversed meanings, descriptions

### Multi-System Descriptions
Descriptions from four major tarot traditions:
- **Rider-Waite-Smith (RWS)**: The most popular modern tarot system (1909)
- **Thoth**: Aleister Crowley & Lady Frieda Harris's esoteric deck (1969)
- **Golden Dawn**: Hermetic Order of the Golden Dawn's ceremonial system
- **Marseille**: Traditional European tarot (pre-1700s)

Each system provides:
- Specific card descriptions
- Upright and reversed meanings
- Key imagery
- Divinatory meanings
- Esoteric interpretations

### Flexible API
- Multiple query methods (by number, name, random)
- Advanced filtering (arcana, suit, element)
- Full-text search across all fields
- Optional inclusion/exclusion of system descriptions
- System-specific endpoint for focused queries

## Installation

1. Clone this repository:
```bash
git clone https://github.com/astrid-selin/TarotAPI.git
cd TarotAPI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create the database:
```bash
python3 migrate_to_sqlite.py
```

This will create `tarot.db` with all card data and correspondences.

## Usage

Start the API server:
```bash
python3 app.py
```

The API will be available at `http://localhost:5000`

Visit `http://localhost:5000/` in your browser for interactive API documentation.

## API Endpoints

### Get API Documentation
```
GET /
```
Returns comprehensive API information and available endpoints.

### Get All Cards
```
GET /cards
```
Returns all 78 tarot cards.

**Query Parameters:**
- `arcana` - Filter by "Major Arcana" or "Minor Arcana"
- `suit` - Filter by suit: "Wands", "Cups", "Swords", or "Pentacles"
- `element` - Filter by element: "Fire", "Water", "Air", or "Earth"
- `systems` - Include system descriptions: "true" (default) or "false"

**Examples:**
```bash
GET /cards?arcana=Major Arcana
GET /cards?suit=Cups
GET /cards?element=Fire
GET /cards?suit=Cups&element=Water
GET /cards?systems=false  # Exclude system descriptions for smaller payload
```

### Get Card by Number
```
GET /cards/<number>
```
Returns a specific card by its number (0-77).

**Query Parameters:**
- `systems` - Include system descriptions: "true" (default) or "false"

**Examples:**
```bash
GET /cards/0           # The Fool
GET /cards/13          # Death
GET /cards/36          # Ace of Cups
GET /cards/0?systems=false
```

### Get Card by Name
```
GET /cards/name/<card_name>
```
Returns a specific card by its name (case-insensitive).

**Query Parameters:**
- `systems` - Include system descriptions: "true" (default) or "false"

**Examples:**
```bash
GET /cards/name/The Fool
GET /cards/name/the fool
GET /cards/name/Ace of Cups
GET /cards/name/queen of swords
```

### Get Random Card
```
GET /cards/random
```
Returns a random tarot card.

**Query Parameters:**
- `systems` - Include system descriptions: "true" (default) or "false"

### Search Cards
```
GET /cards/search?q=<query>
```
Search cards across multiple fields including name, keywords, meanings, correspondences (elements, Hebrew letters, colors, gemstones, etc.).

**Query Parameters:**
- `q` - Search query (required)
- `systems` - Include system descriptions: "true" (default) or "false"

**Examples:**
```bash
GET /cards/search?q=love
GET /cards/search?q=aleph          # Search by Hebrew letter
GET /cards/search?q=topaz          # Search by gemstone
GET /cards/search?q=mercury        # Search by astrological association
```

### List Available Systems
```
GET /systems
```
Returns a list of all available tarot systems with card counts.

### Get System-Specific Description
```
GET /cards/<number>/system/<system_name>
```
Returns a specific card's description from a particular tarot system.

**Valid system names:** `RWS`, `Thoth`, `Golden Dawn`, `Marseille`

**Examples:**
```bash
GET /cards/0/system/Thoth
GET /cards/0/system/RWS
GET /cards/13/system/Golden Dawn
```

## Example Responses

### Full Card Response (with all systems)
```json
{
  "number": 0,
  "name": "The Fool",
  "arcana": "Major Arcana",
  "suit": null,
  "element": "Air",
  "astrology": "Uranus",
  "hebrew_letter": "Aleph",
  "tree_of_life_path": "11 (Kether to Chokmah)",
  "musical_note": "E",
  "color_primary": "Bright pale yellow",
  "color_secondary": "Sky blue",
  "gemstone": "Topaz",
  "herb": "Aspen, Ginseng",
  "key_symbols": "Dog, white rose, cliff, sun, mountains, bundle",
  "keywords": ["beginnings", "innocence", "spontaneity", "free spirit", "adventure"],
  "upright_meaning": "New beginnings, innocence, spontaneity, a free spirit, taking a leap of faith",
  "reversed_meaning": "Recklessness, taking risks, lack of direction, naivety, poor judgment",
  "description": "The Fool represents new beginnings and adventures...",
  "system_descriptions": {
    "RWS": {
      "description": "A young man in colorful garments stands at the edge of a precipice...",
      "upright_meaning": "New beginnings, adventure, innocence...",
      "reversed_meaning": "Naivety, foolishness, recklessness...",
      "key_imagery": "White rose (purity), precipice (unknown)...",
      "divinatory_meaning": "Folly, mania, extravagance...",
      "esoteric_meaning": "The spirit in search of experience..."
    },
    "Thoth": { ... },
    "Golden Dawn": { ... },
    "Marseille": { ... }
  }
}
```

### Compact Response (systems=false)
```json
{
  "number": 0,
  "name": "The Fool",
  "arcana": "Major Arcana",
  "element": "Air",
  "astrology": "Uranus",
  "hebrew_letter": "Aleph",
  "tree_of_life_path": "11 (Kether to Chokmah)",
  "musical_note": "E",
  "color_primary": "Bright pale yellow",
  "gemstone": "Topaz",
  "keywords": ["beginnings", "innocence", "spontaneity"],
  "upright_meaning": "New beginnings, innocence, spontaneity...",
  "reversed_meaning": "Recklessness, taking risks..."
}
```

## Testing the API

Using curl:

```bash
# Get API documentation
curl http://localhost:5000/

# Get all cards (without system descriptions for faster response)
curl http://localhost:5000/cards?systems=false

# Get The Fool with all system descriptions
curl http://localhost:5000/cards/0

# Get The Fool with only Thoth description
curl http://localhost:5000/cards/0/system/Thoth

# Get a random card
curl http://localhost:5000/cards/random

# Search by esoteric correspondence
curl http://localhost:5000/cards/search?q=aleph
curl http://localhost:5000/cards/search?q=topaz

# Filter Major Arcana
curl http://localhost:5000/cards?arcana=Major%20Arcana

# List available systems
curl http://localhost:5000/systems
```

## Database Schema

The SQLite database consists of three main tables:

### cards
Stores all card information including base data and esoteric correspondences.

### keywords
Many-to-many relationship storing keywords for each card.

### system_descriptions
Stores system-specific descriptions from RWS, Thoth, Golden Dawn, and Marseille.

To rebuild the database from scratch:
```bash
python3 migrate_to_sqlite.py
```

## Project Structure

```
TarotAPI/
├── app.py                      # Flask REST API application
├── tarot_data.json             # Original JSON card data
├── tarot.db                    # SQLite database (created by migration)
├── schema.sql                  # Database schema definition
├── migrate_to_sqlite.py        # Migration script
├── card_correspondences.py     # Esoteric correspondences data
├── system_descriptions.py      # Multi-system descriptions data
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Data Sources & Attributions

The tarot correspondences and system descriptions are based on traditional esoteric sources:

- **Qabbalah Correspondences**: Based on Golden Dawn and Hermetic Qabalah traditions
- **RWS Descriptions**: Based on Arthur Edward Waite's "The Pictorial Key to the Tarot" (1910)
- **Thoth Descriptions**: Based on Aleister Crowley's "The Book of Thoth" (1944)
- **Golden Dawn**: Based on the Hermetic Order of the Golden Dawn's teachings
- **Marseille**: Based on traditional Tarot de Marseille interpretations

## Frontend Integration

The API is designed to be easily consumed by frontend applications. The `systems` parameter allows you to control payload size:

- Use `systems=true` for detailed study applications showing multiple interpretations
- Use `systems=false` for quick reference or mobile applications
- Use the `/cards/<number>/system/<system_name>` endpoint for system-specific views

## Future Enhancements

Potential future additions:
- Complete system descriptions for all 78 cards (currently 5 Major Arcana per system)
- Additional tarot systems (Visconti-Sforza, Egyptian, etc.)
- Spread endpoints for multi-card readings
- Card relationships and dignities
- Numerology correspondences
- Historical notes and variations

## Contributing

Contributions are welcome! Areas where help is particularly appreciated:
- Completing system descriptions for all 78 cards
- Adding descriptions from additional tarot systems
- Improving esoteric correspondences accuracy
- Additional API endpoints

## License

MIT

## Version History

### v2.0.0 (Current)
- Migrated from JSON to SQLite database
- Added comprehensive Qabbalah correspondences
- Added esoteric associations (musical notes, colors, gemstones, herbs)
- Added multi-system descriptions (RWS, Thoth, Golden Dawn, Marseille)
- New endpoints: `/systems`, `/cards/<number>/system/<system_name>`
- Enhanced search across all fields including correspondences
- Optional system descriptions via `systems` parameter

### v1.0.0
- Initial release with JSON-based data
- Basic card information and meanings
- Simple REST endpoints

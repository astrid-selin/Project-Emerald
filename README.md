# Esoteric Knowledge API v3.0

A comprehensive REST API for esoteric studies including Tarot, Qabalah, Astrology, and Ritual practices. Built with Python, Flask, and SQLite.

## Features

### Complete Tarot Deck
- Full deck of 78 tarot cards (22 Major Arcana + 56 Minor Arcana)
- Multi-system descriptions (RWS, Thoth, Golden Dawn, Marseille)
- Rich esoteric correspondences (Qabalah, astrology, elements, colors, gemstones, herbs)

### Hermetic Qabalah
- **10 Sephiroth** on the Tree of Life with complete correspondences
  - Divine names, archangels, angelic orders
  - Four-world color scales (Atziluth, Briah, Yetzirah, Assiah)
  - Virtues, vices, spiritual experiences
- **22 Paths** connecting the Sephiroth
  - Hebrew letters and their meanings
  - Direct links to Major Arcana cards
  - Elemental, planetary, and zodiacal associations

### Western Astrology
- **7 Classical Planets** (Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn)
  - Planetary rulerships, exaltations, detriments, and falls
  - Sephirothic correspondences
  - Metals, colors, gemstones, magical powers
- **12 Zodiac Signs**
  - Elements (Fire, Earth, Air, Water) and modalities (Cardinal, Fixed, Mutable)
  - Planetary rulerships and dignities
  - Tarot correspondences

### Esoteric Rituals
- **7 Golden Dawn Rituals** from beginner to expert level
  - Lesser Banishing Ritual of the Pentagram (LBRP)
  - Middle Pillar Ritual (MPR)
  - Banishing/Invoking Rituals of the Hexagram (BRH/IRH)
  - Rose Cross Ritual (RC)
  - Opening by Watchtower (OWT)
- Complete instructions, visualizations, and words of power
- Difficulty ratings and practice progression guidance

### Cross-Referenced System
All correspondences are interconnected:
- Major Arcana cards linked to Tree of Life paths
- Paths connected to Sephiroth
- Sephiroth associated with planets
- Planets ruling zodiac signs
- Signs corresponding to tarot cards

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

This will create `esoteric_knowledge.db` with:
- 78 tarot cards with system descriptions
- 10 Sephiroth
- 22 Paths
- 7 Planets
- 12 Zodiac Signs
- 7 Rituals

## Usage

Start the API server:
```bash
python3 app.py
```

The API will be available at `http://localhost:5000`

Visit `http://localhost:5000/` for interactive API documentation.

## API Endpoints

### Tarot Cards

#### Get All Cards
```
GET /cards
```
**Query Parameters:**
- `arcana` - Filter by "Major Arcana" or "Minor Arcana"
- `suit` - Filter by "Wands", "Cups", "Swords", "Pentacles"
- `element` - Filter by "Fire", "Water", "Air", "Earth"
- `systems` - Include system descriptions: "true" (default) or "false"

**Examples:**
```bash
GET /cards?arcana=Major Arcana
GET /cards?suit=Cups&element=Water
GET /cards?systems=false
```

#### Get Card by Number
```
GET /cards/<number>
```
Returns a specific card by number (0-77).

**Examples:**
```bash
GET /cards/0           # The Fool
GET /cards/13          # Death
```

#### Get Card by Name
```
GET /cards/name/<card_name>
```
Case-insensitive card lookup.

**Examples:**
```bash
GET /cards/name/The Fool
GET /cards/name/ace of cups
```

#### Get Card with Full Correspondences
```
GET /cards/<number>/correspondences
```
Returns card with complete Qabalah and astrological cross-references.

**Example Response for The Fool:**
```json
{
  "card": { ... },
  "qabalah_path": {
    "number": 11,
    "hebrew_letter": "Aleph",
    "from_sephirah_name": "Kether",
    "to_sephirah_name": "Chokmah",
    ...
  },
  "connected_sephiroth": {
    "from": { "name": "Kether", ... },
    "to": { "name": "Chokmah", ... }
  },
  "astrology": { ... }
}
```

#### Search Cards
```
GET /cards/search?q=<query>
```
Search across all card fields.

**Examples:**
```bash
GET /cards/search?q=love
GET /cards/search?q=aleph
GET /cards/search?q=mars
```

#### Other Card Endpoints
```
GET /cards/random              # Random card
GET /systems                   # List tarot systems
GET /cards/<number>/system/<name>  # System-specific description
```

### Qabalah

#### Sephiroth Endpoints
```
GET /api/qabalah/sephiroth              # All 10 Sephiroth
GET /api/qabalah/sephiroth/<number>     # Sephirah by number (1-10)
GET /api/qabalah/sephiroth/name/<name>  # Sephirah by name
```

**Examples:**
```bash
GET /api/qabalah/sephiroth/1                # Kether
GET /api/qabalah/sephiroth/name/Tiphareth   # Tiphareth (Beauty)
```

#### Paths Endpoints
```
GET /api/qabalah/paths                  # All 22 Paths
GET /api/qabalah/paths/<number>         # Path by number (11-32)
GET /api/qabalah/paths/<number>/card    # Path with full tarot card
```

**Examples:**
```bash
GET /api/qabalah/paths/11              # Path of Aleph (The Fool)
GET /api/qabalah/paths/11/card         # Path with complete Fool card data
```

#### Tree of Life
```
GET /api/qabalah/tree
```
Returns complete Tree of Life structure with all Sephiroth and Paths.

### Astrology

#### Planets
```
GET /api/astrology/planets              # All planets
GET /api/astrology/planets/<name>       # Specific planet
```

**Examples:**
```bash
GET /api/astrology/planets
GET /api/astrology/planets/Venus
GET /api/astrology/planets/Jupiter
```

#### Zodiac Signs
```
GET /api/astrology/signs                # All 12 signs
GET /api/astrology/signs/<name>         # Specific sign
```

**Query Parameters for /signs:**
- `element` - Filter by "Fire", "Earth", "Air", "Water"
- `modality` - Filter by "Cardinal", "Fixed", "Mutable"

**Examples:**
```bash
GET /api/astrology/signs
GET /api/astrology/signs/Leo
GET /api/astrology/signs?element=Fire
GET /api/astrology/signs?modality=Cardinal
```

#### Astrological Correspondences
```
GET /api/astrology/elements             # Four elements with signs
GET /api/astrology/modalities           # Three modalities
GET /api/astrology/correspondences      # Complete summary
GET /api/astrology/planetary-hours      # Planetary hours info
```

### Rituals

#### Get Rituals
```
GET /api/rituals                        # All rituals
GET /api/rituals/<id>                   # Ritual by ID
GET /api/rituals/name/<name>            # By name or abbreviation
```

**Query Parameters for /api/rituals:**
- `tradition` - Filter by tradition (e.g., "Golden Dawn")
- `category` - Filter by category (e.g., "Banishing", "Invoking")
- `difficulty` - Filter by "Beginner", "Intermediate", "Advanced", "Expert"
- `instructions` - Include full instructions: "true" (default) or "false"

**Examples:**
```bash
GET /api/rituals?difficulty=Beginner
GET /api/rituals?category=Banishing
GET /api/rituals/name/LBRP             # Lesser Banishing Ritual of the Pentagram
GET /api/rituals/name/Middle Pillar
```

#### Ritual Categories & Guides
```
GET /api/rituals/traditions             # List all traditions
GET /api/rituals/categories             # List all categories
GET /api/rituals/beginner               # Beginner-friendly rituals
GET /api/rituals/daily                  # Daily practice rituals
GET /api/rituals/practice-guide         # Suggested progression
```

#### Search Rituals
```
GET /api/rituals/search?q=<query>
GET /api/rituals/by-planet/<planet>
GET /api/rituals/by-element/<element>
```

**Examples:**
```bash
GET /api/rituals/search?q=banishing
GET /api/rituals/by-element/Fire
```

## Example Use Cases

### 1. Study a Major Arcana Card with Full Context
```bash
# Get The Emperor with all correspondences
curl http://localhost:5000/cards/4/correspondences
```

This returns:
- Full card details
- Qabalah path (Path of Heh, connecting Chokmah to Tiphareth)
- Connected Sephiroth (Wisdom and Beauty)
- Astrological association (Aries)
- Ruling planet (Mars)
- Elemental correspondences

### 2. Explore the Tree of Life
```bash
# Get complete Tree structure
curl http://localhost:5000/api/qabalah/tree

# Deep dive into a specific Sephirah
curl http://localhost:5000/api/qabalah/sephiroth/6  # Tiphareth

# Study a Path and its tarot card
curl http://localhost:5000/api/qabalah/paths/15/card  # The Emperor
```

### 3. Plan Astrological Magic
```bash
# Get Venus correspondences for love magic
curl http://localhost:5000/api/astrology/planets/Venus

# Find all Fire signs for energy work
curl http://localhost:5000/api/astrology/signs?element=Fire

# Get planetary hours information
curl http://localhost:5000/api/astrology/planetary-hours
```

### 4. Build a Daily Practice
```bash
# Get beginner rituals to start with
curl http://localhost:5000/api/rituals/beginner

# Get the LBRP with full instructions
curl http://localhost:5000/api/rituals/name/LBRP

# Get practice progression guide
curl http://localhost:5000/api/rituals/practice-guide

# Find daily practice rituals under 25 minutes
curl http://localhost:5000/api/rituals/daily
```

### 5. Cross-Reference Systems
```bash
# Find which zodiac sign corresponds to The Emperor
curl http://localhost:5000/cards/4/correspondences

# Find all tarot cards associated with Venus
curl http://localhost:5000/cards/search?q=Venus

# See which Sephirah corresponds to the Sun
curl http://localhost:5000/api/astrology/planets/Sun
```

## Database Schema

The SQLite database (`esoteric_knowledge.db`) contains:

### Tarot Tables
- **cards** - All 78 tarot cards with esoteric correspondences
- **keywords** - Card keywords (many-to-many)
- **system_descriptions** - Multi-system interpretations

### Qabalah Tables
- **sephiroth** - 10 Sephiroth on the Tree of Life
- **paths** - 22 Paths with Hebrew letters and tarot links

### Astrology Tables
- **planets** - 7 classical planets with correspondences
- **zodiac_signs** - 12 signs with elements and modalities
- **lunar_mansions** - 28 lunar stations (schema ready, data pending)

### Rituals Table
- **rituals** - Esoteric rituals with full instructions

## Project Structure

```
TarotAPI/
├── app.py                      # Main Flask application
├── routes/                     # API route blueprints
│   ├── __init__.py
│   ├── qabalah.py             # Qabalah endpoints
│   ├── astrology.py           # Astrology endpoints
│   └── rituals.py             # Rituals endpoints
├── esoteric_knowledge.db       # SQLite database
├── schema.sql                  # Database schema
├── migrate_to_sqlite.py        # Database migration script
├── seed_qabalah.py            # Qabalah seed data
├── seed_astrology.py          # Astrology seed data
├── seed_rituals.py            # Rituals seed data
├── card_correspondences.py     # Tarot correspondences
├── system_descriptions.py      # Multi-system descriptions
├── tarot_data.json            # Original card data
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Data Sources & Attributions

### Tarot
- **RWS**: Arthur Edward Waite's "The Pictorial Key to the Tarot" (1910)
- **Thoth**: Aleister Crowley's "The Book of Thoth" (1944)
- **Golden Dawn**: Hermetic Order of the Golden Dawn teachings
- **Marseille**: Traditional Tarot de Marseille

### Qabalah
- Based on Golden Dawn and traditional Hermetic Qabalah
- Sephiroth correspondences from "777" by Aleister Crowley
- Path attributions following Golden Dawn system

### Astrology
- Traditional Western/Hermetic astrology
- Planetary dignities and correspondences
- Integration with Qabalah via Sephirothic associations

### Rituals
- Golden Dawn ritual corpus
- Based on Israel Regardie's "The Golden Dawn" (1937)
- Ceremonial magic practices from Hermetic tradition

## Contributing

Contributions welcome! Priority areas:
- Complete system descriptions for all 78 cards
- Additional ritual traditions (Thelema, Chaos Magic, etc.)
- Lunar mansions data
- Enhanced cross-reference queries
- Frontend examples

## License

MIT

## Version History

### v3.0.0 (Current)
- **MAJOR EXPANSION**: Renamed to Esoteric Knowledge API
- Added complete Hermetic Qabalah system (10 Sephiroth, 22 Paths)
- Added Western Astrology (7 Planets, 12 Zodiac Signs)
- Added 7 Golden Dawn rituals with full instructions
- New blueprint-based architecture for routes
- Cross-reference endpoint linking all systems
- Renamed database from `tarot.db` to `esoteric_knowledge.db`
- 30+ new API endpoints across Qabalah, Astrology, and Rituals

### v2.0.0
- Migrated from JSON to SQLite database
- Added comprehensive Qabalah correspondences to cards
- Added multi-system descriptions (RWS, Thoth, Golden Dawn, Marseille)
- Enhanced search and filtering

### v1.0.0
- Initial release with JSON-based tarot data
- Basic REST endpoints for cards

---

**Note**: This is a living API focused on traditional Western esoteric systems. While rooted in historical sources, it's designed for study, education, and practical application in modern esoteric practice.

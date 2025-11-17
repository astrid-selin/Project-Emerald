# Project Emerald

A comprehensive platform for exploring the Western Hermetic Tradition, including Tarot, Qabalah, Astrology, and ceremonial ritual practices. Project Emerald provides both a REST API and interactive web interface for studying the interconnected correspondences of esoteric wisdom.

Built with Python, Flask, SQLite, and SvelteKit.

## Overview

Project Emerald is an educational platform dedicated to the study and practice of Western Hermetic traditions. It integrates multiple systems of esoteric knowledge into a unified, cross-referenced framework for serious students of the mysteries.

### What is the Hermetic Tradition?

The Western Hermetic Tradition encompasses the spiritual, philosophical, and magical teachings rooted in ancient Greco-Egyptian wisdom, refined through medieval alchemy, Renaissance magic, and modern ceremonial practice. It synthesizes:

- **Tarot**: The pictorial book of 78 archetypal keys
- **Qabalah**: The Tree of Life and its ten emanations
- **Astrology**: Celestial correspondences and planetary influences
- **Ritual Magic**: Ceremonial practices for spiritual development
- **Alchemy**: The transformation of consciousness
- **Sacred Geometry**: The mathematical structure of creation

## Features

### 🃏 Complete Tarot System
- Full deck of 78 cards (22 Major Arcana + 56 Minor Arcana)
- Multi-system interpretations (Rider-Waite-Smith, Thoth, Golden Dawn, Marseille)
- Deep esoteric correspondences (Qabalah, astrology, elements, colors, gemstones, herbs)
- Interactive card exploration with full cross-references

### 🌳 Hermetic Qabalah
- **10 Sephiroth** on the Tree of Life with complete attributions
  - Divine names, archangels, and angelic orders
  - Four-world color scales (Atziluth, Briah, Yetzirah, Assiah)
  - Virtues, vices, and spiritual experiences
  - Planetary and elemental associations
- **22 Paths** connecting the Sephiroth
  - Hebrew letters and their meanings
  - Direct links to Major Arcana cards
  - Elemental, planetary, and zodiacal attributions

### ✨ Western Astrology
- **7 Classical Planets** (Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn)
  - Planetary rulerships, exaltations, detriments, and falls
  - Sephirothic correspondences
  - Traditional metals, colors, gemstones, and magical powers
- **12 Zodiac Signs**
  - Elements (Fire, Earth, Air, Water) and modalities (Cardinal, Fixed, Mutable)
  - Planetary rulerships and essential dignities
  - Tarot and Tree of Life correspondences

### 🕯️ Ceremonial Rituals
- **7 Golden Dawn Rituals** from beginner to advanced practice
  - Lesser Banishing Ritual of the Pentagram (LBRP)
  - Middle Pillar Ritual (MPR)
  - Banishing/Invoking Rituals of the Hexagram (BRH/IRH)
  - Rose Cross Ritual (RC)
  - Opening by Watchtower (OWT)
- Complete step-by-step instructions with visualizations
- Words of power and ritual gestures
- Difficulty ratings and suggested practice progression

### 🔗 Unified Correspondence System
All systems are deeply interconnected:
- Major Arcana cards mapped to Tree of Life paths
- Paths connecting Sephiroth on the Tree
- Sephiroth linked to planetary spheres
- Planets ruling zodiac signs and elements
- Complete cross-referencing across all systems

## Installation

### Prerequisites

- Python 3.8+
- Node.js 18+ (for frontend)
- Git

### Backend Setup

1. Clone this repository:
```bash
git clone https://github.com/astrid-selin/Project-Emerald.git
cd Project-Emerald
```

2. Install Python dependencies:
```bash
pip install -r backend/requirements.txt
```

3. Create the database:
```bash
python3 scripts/migrate_to_sqlite.py
```

This will create `esoteric_knowledge.db` with:
- 78 tarot cards with multi-system descriptions
- 10 Sephiroth on the Tree of Life
- 22 Paths with Hebrew letter attributions
- 7 Classical planets with correspondences
- 12 Zodiac signs with dignities
- 7 Golden Dawn rituals

4. Start the API server:
```bash
python3 backend/app.py
```

The API will be available at `http://localhost:5000`

Visit `http://localhost:5000/` for the API documentation endpoint.

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

See `frontend/README.md` for detailed frontend documentation.

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
Project-Emerald/
├── backend/                    # Flask REST API
│   ├── app.py                 # Main application entry point
│   ├── routes/                # API route blueprints
│   │   ├── qabalah.py        # Qabalah endpoints
│   │   ├── astrology.py      # Astrology endpoints
│   │   └── rituals.py        # Rituals endpoints
│   ├── schema.sql            # Database schema
│   └── requirements.txt      # Python dependencies
├── data/                      # Seed data and correspondences
│   ├── seed_qabalah.py       # Tree of Life data
│   ├── seed_astrology.py     # Planets and zodiac data
│   ├── seed_rituals.py       # Ritual instructions
│   ├── card_correspondences.py # Tarot correspondences
│   ├── system_descriptions.py  # Multi-system interpretations
│   └── tarot_data.json       # Base tarot card data
├── scripts/                   # Utility scripts
│   └── migrate_to_sqlite.py  # Database initialization
├── frontend/                  # SvelteKit web interface
│   ├── src/
│   │   ├── routes/           # Page components
│   │   ├── lib/              # Shared utilities and components
│   │   └── app.css           # Global styles
│   └── package.json
├── esoteric_knowledge.db      # SQLite database
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

Contributions welcome! We're building a comprehensive resource for students of the Western Hermetic Tradition.

### Priority Areas:
- Complete system descriptions for all 78 tarot cards
- Additional ritual traditions (Thelema, Enochian, Elemental Magic)
- Lunar mansions (28 mansions) data and correspondences
- Enhanced cross-reference queries and API endpoints
- Educational content and lesson modules
- Interactive visualizations (Tree of Life, astrological charts)
- Mobile-responsive UI improvements

### Guidelines:
- Maintain historical accuracy and cite traditional sources
- Follow the existing code structure and patterns
- Include comprehensive documentation
- Test API endpoints thoroughly
- Ensure frontend changes are responsive across devices

## License

MIT

## Version History

### v3.1.0 (Current) - Project Emerald
- **REBRANDING**: Renamed from TarotAPI to Project Emerald to reflect expanded scope
- **RESTRUCTURED**: Improved separation of concerns
  - `backend/` - Flask API and routes
  - `data/` - Seed files and correspondences
  - `scripts/` - Utility scripts
  - `frontend/` - SvelteKit web interface
- **ENHANCED**: Updated documentation to emphasize Hermetic tradition context
- Interactive lesson system for structured learning
- Visual Tree of Life representation
- Expanded hermetic philosophy overview

### v3.0.0
- **MAJOR EXPANSION**: Grew beyond tarot to full esoteric knowledge system
- Added complete Hermetic Qabalah (10 Sephiroth, 22 Paths)
- Added Western Astrology (7 Planets, 12 Zodiac Signs)
- Added 7 Golden Dawn rituals with complete instructions
- New blueprint-based architecture for routes
- Cross-reference endpoints linking all systems
- Renamed database from `tarot.db` to `esoteric_knowledge.db`
- 30+ new API endpoints across Qabalah, Astrology, and Rituals

### v2.0.0
- Migrated from JSON to SQLite database
- Added comprehensive Qabalah correspondences to tarot cards
- Added multi-system descriptions (RWS, Thoth, Golden Dawn, Marseille)
- Enhanced search and filtering capabilities

### v1.0.0
- Initial release as TarotAPI
- JSON-based tarot card data
- Basic REST endpoints for card queries

---

## Philosophy

Project Emerald is designed as a living educational resource for the Western Hermetic Tradition. While deeply rooted in historical sources and traditional teachings, it serves modern students seeking to understand the interconnected nature of esoteric correspondences. This is not merely an API—it's a gateway to the mysteries, presented with academic rigor and practical applicability.

**"As above, so below; as within, so without."** — The Emerald Tablet

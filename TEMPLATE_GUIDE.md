# Tarot Card Template Guide

This guide explains the template structure for creating a comprehensive tarot card database.

## Overview

A standard tarot deck consists of 78 cards:
- **Major Arcana**: 22 cards (numbered 0-21)
- **Minor Arcana**: 56 cards (4 suits × 14 cards each)

## File Structure

```
TarotAPI/
├── schema.json                          # JSON Schema validation
├── templates/
│   ├── major_arcana_template.json      # Template for major arcana cards
│   └── minor_arcana_template.json      # Template for minor arcana cards
└── examples/
    ├── major_arcana_example.json       # Example: The Fool
    └── minor_arcana_example.json       # Example: Ace of Wands
```

## Template Fields

### Common Fields (Both Arcana Types)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes | Unique identifier (lowercase, underscores) |
| `number` | integer | Yes | Card number in sequence |
| `name` | string | Yes | Full name of the card |
| `arcana` | string | Yes | "major" or "minor" |
| `img` | string | No | Image path or URL |
| `keywords.upright` | array | No | Keywords for upright position |
| `keywords.reversed` | array | No | Keywords for reversed position |
| `meanings.upright` | string | No | Detailed upright meaning |
| `meanings.reversed` | string | No | Detailed reversed meaning |
| `description` | string | No | General card description |
| `symbolism` | array | No | Key symbols in the card |
| `advice.upright` | string | No | Advice when upright |
| `advice.reversed` | string | No | Advice when reversed |

### Major Arcana Specific

| Field | Type | Description |
|-------|------|-------------|
| `suit` | null | Always null for major arcana |
| `rank` | null | Always null for major arcana |
| `correspondences.element` | string | Associated element (if any) |
| `correspondences.astrology` | string | Planet, sign, or astrological body |
| `correspondences.numerology` | integer | Numerological value (0-21) |
| `correspondences.hebrew_letter` | string | Associated Hebrew letter |
| `correspondences.kabbalistic_path` | integer | Path on Tree of Life |

### Minor Arcana Specific

| Field | Type | Description |
|-------|------|-------------|
| `suit` | string | "wands", "cups", "swords", or "pentacles" |
| `rank` | string | "ace", "2"-"10", "page", "knight", "queen", "king" |
| `correspondences.element` | string | Suit element (fire/water/air/earth) |
| `correspondences.astrology` | string | Zodiac signs associated with suit |

## Major Arcana Card List

| Number | Name | Astrology | Element | Hebrew Letter |
|--------|------|-----------|---------|---------------|
| 0 | The Fool | Uranus | Air | Aleph |
| 1 | The Magician | Mercury | Air | Beth |
| 2 | The High Priestess | Moon | Water | Gimel |
| 3 | The Empress | Venus | Earth | Daleth |
| 4 | The Emperor | Aries | Fire | Heh |
| 5 | The Hierophant | Taurus | Earth | Vav |
| 6 | The Lovers | Gemini | Air | Zayin |
| 7 | The Chariot | Cancer | Water | Cheth |
| 8 | Strength | Leo | Fire | Teth |
| 9 | The Hermit | Virgo | Earth | Yod |
| 10 | Wheel of Fortune | Jupiter | Fire | Kaph |
| 11 | Justice | Libra | Air | Lamed |
| 12 | The Hanged Man | Neptune | Water | Mem |
| 13 | Death | Scorpio | Water | Nun |
| 14 | Temperance | Sagittarius | Fire | Samekh |
| 15 | The Devil | Capricorn | Earth | Ayin |
| 16 | The Tower | Mars | Fire | Peh |
| 17 | The Star | Aquarius | Air | Tzaddi |
| 18 | The Moon | Pisces | Water | Qoph |
| 19 | The Sun | Sun | Fire | Resh |
| 20 | Judgement | Pluto | Fire | Shin |
| 21 | The World | Saturn | Earth | Tau |

## Minor Arcana Structure

### Suits and Their Correspondences

| Suit | Element | Astrological Signs | Represents |
|------|---------|-------------------|------------|
| Wands | Fire | Aries, Leo, Sagittarius | Action, energy, passion, creativity |
| Cups | Water | Cancer, Scorpio, Pisces | Emotions, relationships, intuition |
| Swords | Air | Gemini, Libra, Aquarius | Thoughts, communication, conflict |
| Pentacles | Earth | Taurus, Virgo, Capricorn | Material, practical, financial |

### Ranks in Each Suit

1. Ace (number: 1)
2. Two (number: 2)
3. Three (number: 3)
4. Four (number: 4)
5. Five (number: 5)
6. Six (number: 6)
7. Seven (number: 7)
8. Eight (number: 8)
9. Nine (number: 9)
10. Ten (number: 10)
11. Page (number: 11)
12. Knight (number: 12)
13. Queen (number: 13)
14. King (number: 14)

## ID Naming Convention

### Major Arcana
Format: `the_[card_name]` (lowercase, underscores)
- Examples: `the_fool`, `the_magician`, `the_high_priestess`

### Minor Arcana
Format: `[rank]_of_[suit]` (lowercase, underscores)
- Examples: `ace_of_wands`, `two_of_cups`, `page_of_swords`, `king_of_pentacles`

## Usage Examples

### Creating a Major Arcana Card

```json
{
  "id": "the_magician",
  "number": 1,
  "name": "The Magician",
  "arcana": "major",
  "suit": null,
  "rank": null,
  "keywords": {
    "upright": ["manifestation", "resourcefulness", "power"],
    "reversed": ["manipulation", "poor planning", "untapped talents"]
  }
}
```

### Creating a Minor Arcana Card

```json
{
  "id": "three_of_cups",
  "number": 3,
  "name": "Three of Cups",
  "arcana": "minor",
  "suit": "cups",
  "rank": "3",
  "keywords": {
    "upright": ["celebration", "friendship", "community"],
    "reversed": ["overindulgence", "gossip", "isolation"]
  }
}
```

## Database Implementation Suggestions

### SQL Schema Example

```sql
CREATE TABLE tarot_cards (
    id VARCHAR(50) PRIMARY KEY,
    number INTEGER,
    name VARCHAR(100) NOT NULL,
    arcana VARCHAR(10) NOT NULL,
    suit VARCHAR(20),
    rank VARCHAR(10),
    img VARCHAR(255),
    description TEXT,
    upright_meaning TEXT,
    reversed_meaning TEXT,
    upright_advice TEXT,
    reversed_advice TEXT,
    element VARCHAR(10),
    astrology VARCHAR(100),
    numerology INTEGER,
    hebrew_letter VARCHAR(20),
    kabbalistic_path INTEGER
);

CREATE TABLE card_keywords (
    card_id VARCHAR(50),
    keyword VARCHAR(50),
    position VARCHAR(10), -- 'upright' or 'reversed'
    FOREIGN KEY (card_id) REFERENCES tarot_cards(id)
);

CREATE TABLE card_symbolism (
    card_id VARCHAR(50),
    symbol TEXT,
    FOREIGN KEY (card_id) REFERENCES tarot_cards(id)
);
```

### NoSQL (MongoDB) Example

```javascript
db.tarot_cards.insertOne({
  _id: "the_fool",
  number: 0,
  name: "The Fool",
  arcana: "major",
  keywords: {
    upright: ["beginnings", "innocence"],
    reversed: ["recklessness", "naivety"]
  }
});

// Create indexes for efficient querying
db.tarot_cards.createIndex({ "arcana": 1 });
db.tarot_cards.createIndex({ "suit": 1 });
db.tarot_cards.createIndex({ "number": 1 });
```

## Validation

Use the included `schema.json` file to validate your card data against the defined structure. This ensures consistency across your database.

```bash
# Using a JSON schema validator
jsonschema -i your_card.json schema.json
```

## API Endpoint Suggestions

Consider implementing these endpoints:

- `GET /cards` - Get all cards
- `GET /cards/:id` - Get specific card
- `GET /cards/major` - Get all major arcana
- `GET /cards/minor` - Get all minor arcana
- `GET /cards/suit/:suit` - Get all cards of a suit
- `GET /cards/random` - Get random card
- `GET /cards/draw/:count` - Draw multiple random cards

## Contributing

When adding new card data:
1. Follow the template structure
2. Validate against schema.json
3. Use consistent ID naming conventions
4. Include both upright and reversed meanings
5. Add relevant symbolism and correspondences

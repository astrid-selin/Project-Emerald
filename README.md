# TarotAPI

A simple tarot API that fetches Tarot cards with all their correspondences and information

## Overview

This project provides a comprehensive template system for creating a tarot card database. It includes structure for all 78 cards of a standard tarot deck:
- 22 Major Arcana cards
- 56 Minor Arcana cards (4 suits × 14 cards each)

## Project Structure

```
TarotAPI/
├── schema.json                          # JSON Schema for validation
├── deck_reference.json                  # Complete list of all 78 cards
├── TEMPLATE_GUIDE.md                    # Comprehensive documentation
├── templates/
│   ├── major_arcana_template.json      # Template for major arcana
│   └── minor_arcana_template.json      # Template for minor arcana
└── examples/
    ├── major_arcana_example.json       # The Fool example
    └── minor_arcana_example.json       # Ace of Wands example
```

## Quick Start

1. Review the `TEMPLATE_GUIDE.md` for detailed documentation
2. Use templates in `templates/` directory to create new cards
3. Validate your cards against `schema.json`
4. Reference `deck_reference.json` for a complete card list
5. See `examples/` directory for sample implementations

## Card Data Structure

Each card includes:
- Basic info (id, name, number, arcana type)
- Keywords (upright and reversed)
- Meanings and advice
- Symbolism
- Correspondences (astrological, elemental, numerological)
- Image references

## Database Implementation

The templates are designed to work with:
- SQL databases (PostgreSQL, MySQL, SQLite)
- NoSQL databases (MongoDB, CouchDB)
- JSON file storage
- REST/GraphQL APIs

See `TEMPLATE_GUIDE.md` for database schema examples and API endpoint suggestions.

## Next Steps

1. Populate database with all 78 cards using the templates
2. Implement API endpoints for querying cards
3. Add card images
4. Create drawing/shuffle functionality
5. Implement spread patterns (Celtic Cross, Three Card, etc.)

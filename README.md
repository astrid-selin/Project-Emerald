# TarotAPI

A simple REST API for fetching tarot cards with all their correspondences and information. Built with Python and Flask.

## Features

- Complete deck of 78 tarot cards (22 Major Arcana + 56 Minor Arcana)
- Detailed card information including:
  - Card name, number, and arcana type
  - Element and astrological correspondences
  - Keywords
  - Upright and reversed meanings
  - Card descriptions
- Multiple API endpoints for flexible querying
- Search functionality
- Filter by arcana, suit, or element

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Start the API server:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Get API Documentation
```
GET /
```
Returns API information and available endpoints.

### Get All Cards
```
GET /cards
```
Returns all 78 tarot cards.

Optional query parameters:
- `arcana` - Filter by "Major Arcana" or "Minor Arcana"
- `suit` - Filter by suit: "Wands", "Cups", "Swords", or "Pentacles"
- `element` - Filter by element: "Fire", "Water", "Air", or "Earth"

Examples:
```
GET /cards?arcana=Major Arcana
GET /cards?suit=Cups
GET /cards?element=Fire
```

### Get Card by Number
```
GET /cards/<number>
```
Returns a specific card by its number (0-77).

Examples:
```
GET /cards/0           # The Fool
GET /cards/13          # Death
GET /cards/36          # Ace of Cups
```

### Get Card by Name
```
GET /cards/name/<card_name>
```
Returns a specific card by its name (case-insensitive).

Examples:
```
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

### Search Cards
```
GET /cards/search?q=<query>
```
Search cards by keyword in name, keywords, or meanings.

Examples:
```
GET /cards/search?q=love
GET /cards/search?q=success
GET /cards/search?q=change
```

## Example Response

```json
{
  "number": 0,
  "name": "The Fool",
  "arcana": "Major Arcana",
  "suit": null,
  "element": "Air",
  "astrology": "Uranus",
  "keywords": ["beginnings", "innocence", "spontaneity", "free spirit", "adventure"],
  "upright_meaning": "New beginnings, innocence, spontaneity, a free spirit, taking a leap of faith",
  "reversed_meaning": "Recklessness, taking risks, lack of direction, naivety, poor judgment",
  "description": "The Fool represents new beginnings and adventures. It symbolizes infinite possibilities and taking a leap of faith into the unknown."
}
```

## Testing the API

You can test the API using curl, your browser, or any HTTP client:

```bash
# Get all cards
curl http://localhost:5000/cards

# Get a specific card by number
curl http://localhost:5000/cards/0

# Get a specific card by name
curl http://localhost:5000/cards/name/The%20Fool

# Get a random card
curl http://localhost:5000/cards/random

# Search for cards
curl http://localhost:5000/cards/search?q=love

# Filter cards
curl http://localhost:5000/cards?arcana=Major%20Arcana
```

## Project Structure

```
TarotAPI/
├── app.py              # Main Flask application
├── tarot_data.json     # Complete tarot card data
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## License

MIT
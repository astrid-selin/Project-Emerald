-- SQLite Database Schema for Comprehensive Tarot Card Database
-- Includes esoteric correspondences and descriptions from major tarot systems

CREATE TABLE IF NOT EXISTS cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER NOT NULL UNIQUE,
    name TEXT NOT NULL,
    arcana TEXT NOT NULL CHECK(arcana IN ('Major Arcana', 'Minor Arcana')),
    suit TEXT CHECK(suit IN ('Wands', 'Cups', 'Swords', 'Pentacles') OR suit IS NULL),

    -- Elemental and Astrological
    element TEXT,
    astrology TEXT,
    astrological_decan TEXT, -- For minor arcana pip cards

    -- Qabbalah Correspondences
    hebrew_letter TEXT,
    tree_of_life_path TEXT,
    sephiroth TEXT,

    -- Sensory Correspondences
    musical_note TEXT,
    color_primary TEXT,
    color_secondary TEXT,
    gemstone TEXT,
    herb TEXT,

    -- Basic Meanings (Generic)
    upright_meaning TEXT,
    reversed_meaning TEXT,
    description TEXT,

    -- Symbolism
    key_symbols TEXT, -- JSON array or comma-separated

    -- Created/Modified timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for keywords (many-to-many relationship)
CREATE TABLE IF NOT EXISTS keywords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_id INTEGER NOT NULL,
    keyword TEXT NOT NULL,
    FOREIGN KEY (card_id) REFERENCES cards(id) ON DELETE CASCADE
);

-- Table for system-specific descriptions
CREATE TABLE IF NOT EXISTS system_descriptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_id INTEGER NOT NULL,
    system_name TEXT NOT NULL CHECK(system_name IN ('RWS', 'Thoth', 'Golden Dawn', 'Marseille')),
    description TEXT NOT NULL,
    upright_meaning TEXT,
    reversed_meaning TEXT,
    key_imagery TEXT, -- Specific imagery described in this system
    divinatory_meaning TEXT,
    esoteric_meaning TEXT,
    FOREIGN KEY (card_id) REFERENCES cards(id) ON DELETE CASCADE,
    UNIQUE(card_id, system_name)
);

-- Indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_cards_arcana ON cards(arcana);
CREATE INDEX IF NOT EXISTS idx_cards_suit ON cards(suit);
CREATE INDEX IF NOT EXISTS idx_cards_element ON cards(element);
CREATE INDEX IF NOT EXISTS idx_cards_number ON cards(number);
CREATE INDEX IF NOT EXISTS idx_keywords_card_id ON keywords(card_id);
CREATE INDEX IF NOT EXISTS idx_keywords_keyword ON keywords(keyword);
CREATE INDEX IF NOT EXISTS idx_system_descriptions_card_id ON system_descriptions(card_id);
CREATE INDEX IF NOT EXISTS idx_system_descriptions_system ON system_descriptions(system_name);

-- Create a view for easy querying with all data combined
CREATE VIEW IF NOT EXISTS cards_complete AS
SELECT
    c.*,
    GROUP_CONCAT(DISTINCT k.keyword) as keywords,
    (SELECT json_group_object(sd.system_name,
        json_object(
            'description', sd.description,
            'upright_meaning', sd.upright_meaning,
            'reversed_meaning', sd.reversed_meaning,
            'key_imagery', sd.key_imagery,
            'divinatory_meaning', sd.divinatory_meaning,
            'esoteric_meaning', sd.esoteric_meaning
        )
    ) FROM system_descriptions sd WHERE sd.card_id = c.id) as system_descriptions
FROM cards c
LEFT JOIN keywords k ON c.id = k.id
GROUP BY c.id;

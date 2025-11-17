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

-- ============================================================================
-- QABALAH TABLES
-- ============================================================================

-- Table for the 10 Sephiroth (spheres) on the Tree of Life
CREATE TABLE IF NOT EXISTS sephiroth (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER NOT NULL UNIQUE CHECK(number BETWEEN 1 AND 10),
    name TEXT NOT NULL UNIQUE, -- e.g., "Kether", "Chokmah", etc.
    name_hebrew TEXT, -- Hebrew name
    meaning TEXT, -- Translation/meaning of the name
    divine_name TEXT, -- God name (e.g., "Eheieh" for Kether)
    archangel TEXT, -- Associated archangel
    angelic_order TEXT, -- Order of angels
    planet TEXT, -- Associated planet or celestial body
    mundane_chakra TEXT, -- Physical/mundane correspondence
    spiritual_experience TEXT, -- Spiritual experience of this sephirah
    virtue TEXT, -- Associated virtue
    vice TEXT, -- Associated vice
    color_atziluth TEXT, -- Color in Atziluth (archetypal world)
    color_briah TEXT, -- Color in Briah (creative world)
    color_yetzirah TEXT, -- Color in Yetzirah (formative world)
    color_assiah TEXT, -- Color in Assiah (material world)
    tarot_association TEXT, -- Associated tarot cards
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for the 22 Paths connecting the Sephiroth
CREATE TABLE IF NOT EXISTS paths (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER NOT NULL UNIQUE CHECK(number BETWEEN 11 AND 32), -- 11-32 in Qabalah
    name TEXT NOT NULL, -- e.g., "Path of Aleph", "The Fool's Path"
    hebrew_letter TEXT NOT NULL UNIQUE, -- The Hebrew letter (Aleph, Beth, etc.)
    hebrew_letter_meaning TEXT, -- Meaning of the letter
    tarot_card_id INTEGER, -- Links to Major Arcana card
    connects_from INTEGER NOT NULL, -- Sephirah number it connects from
    connects_to INTEGER NOT NULL, -- Sephirah number it connects to
    element TEXT, -- Associated element (if applicable)
    planet TEXT, -- Associated planet (if applicable)
    sign TEXT, -- Associated zodiac sign (if applicable)
    color TEXT, -- Primary color correspondence
    description TEXT,
    FOREIGN KEY (tarot_card_id) REFERENCES cards(id) ON DELETE SET NULL,
    FOREIGN KEY (connects_from) REFERENCES sephiroth(number) ON DELETE CASCADE,
    FOREIGN KEY (connects_to) REFERENCES sephiroth(number) ON DELETE CASCADE
);

-- ============================================================================
-- ASTROLOGY TABLES
-- ============================================================================

-- Table for Planets (7 classical + Sun/Moon)
CREATE TABLE IF NOT EXISTS planets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE, -- e.g., "Sun", "Moon", "Mercury", etc.
    symbol TEXT, -- Astrological symbol
    day_of_week TEXT, -- Ruled day
    metal TEXT, -- Associated metal
    color TEXT, -- Associated color
    gemstone TEXT, -- Associated gemstone
    sephiroth_number INTEGER, -- Associated sephirah on Tree of Life
    rules_signs TEXT, -- JSON array of signs this planet rules
    exalted_in TEXT, -- Sign of exaltation
    detriment_in TEXT, -- Sign of detriment
    fall_in TEXT, -- Sign of fall
    quality TEXT, -- Hot/cold, dry/moist
    tarot_association TEXT, -- Associated tarot cards
    magical_powers TEXT, -- Magical abilities/influences
    description TEXT,
    FOREIGN KEY (sephiroth_number) REFERENCES sephiroth(number) ON DELETE SET NULL
);

-- Table for Zodiac Signs
CREATE TABLE IF NOT EXISTS zodiac_signs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE, -- e.g., "Aries", "Taurus", etc.
    symbol TEXT, -- Unicode symbol
    element TEXT NOT NULL CHECK(element IN ('Fire', 'Earth', 'Air', 'Water')),
    modality TEXT NOT NULL CHECK(modality IN ('Cardinal', 'Fixed', 'Mutable')),
    ruling_planet TEXT, -- Primary ruling planet
    exalted_planet TEXT, -- Planet exalted in this sign
    detriment_planet TEXT, -- Planet in detriment
    fall_planet TEXT, -- Planet in fall
    polarity TEXT CHECK(polarity IN ('Positive', 'Negative')),
    house_number INTEGER CHECK(house_number BETWEEN 1 AND 12),
    body_part TEXT, -- Ruled body part
    tarot_association TEXT, -- Associated Major Arcana card
    dates_start TEXT, -- Start date (MM-DD format)
    dates_end TEXT, -- End date (MM-DD format)
    keywords TEXT, -- JSON array of keywords
    description TEXT,
    FOREIGN KEY (ruling_planet) REFERENCES planets(name) ON DELETE SET NULL
);

-- Table for Lunar Mansions (optional - 28 stations of the Moon)
CREATE TABLE IF NOT EXISTS lunar_mansions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER NOT NULL UNIQUE CHECK(number BETWEEN 1 AND 28),
    name_arabic TEXT, -- Arabic name
    name_sanskrit TEXT, -- Sanskrit nakshatra name (if applicable)
    name_chinese TEXT, -- Chinese mansion name (if applicable)
    degrees_start REAL, -- Starting degree in zodiac (0-360)
    degrees_end REAL, -- Ending degree
    zodiac_sign TEXT, -- Which sign it falls in
    ruling_planet TEXT, -- Ruling planet
    symbolism TEXT, -- Associated symbols
    nature TEXT, -- Beneficial/malefic
    activities TEXT, -- Favorable activities
    description TEXT,
    FOREIGN KEY (ruling_planet) REFERENCES planets(name) ON DELETE SET NULL
);

-- ============================================================================
-- RITUALS TABLE
-- ============================================================================

-- Table for Esoteric Rituals and Practices
CREATE TABLE IF NOT EXISTS rituals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    abbreviation TEXT, -- e.g., "LBRP", "BRH"
    tradition TEXT, -- e.g., "Golden Dawn", "Thelema", "Hermetic"
    category TEXT, -- e.g., "Banishing", "Invoking", "Middle Pillar"
    purpose TEXT, -- Primary purpose/goal
    difficulty TEXT CHECK(difficulty IN ('Beginner', 'Intermediate', 'Advanced', 'Expert')),
    duration_minutes INTEGER, -- Approximate duration
    requires_tools TEXT, -- JSON array of required tools
    elemental_focus TEXT, -- Primary element (if applicable)
    sephiroth_focus TEXT, -- Primary sephiroth worked with
    planetary_focus TEXT, -- Primary planet (if applicable)
    timing_notes TEXT, -- When to perform (moon phase, planetary hour, etc.)
    instructions TEXT, -- Full ritual instructions
    visualization TEXT, -- Visualization notes
    words_of_power TEXT, -- Specific words, god names, or phrases
    benefits TEXT, -- Benefits of regular practice
    warnings TEXT, -- Warnings or precautions
    source TEXT, -- Source text or grimoire
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- INDEXES FOR NEW TABLES
-- ============================================================================

CREATE INDEX IF NOT EXISTS idx_sephiroth_number ON sephiroth(number);
CREATE INDEX IF NOT EXISTS idx_sephiroth_planet ON sephiroth(planet);

CREATE INDEX IF NOT EXISTS idx_paths_number ON paths(number);
CREATE INDEX IF NOT EXISTS idx_paths_hebrew_letter ON paths(hebrew_letter);
CREATE INDEX IF NOT EXISTS idx_paths_tarot_card ON paths(tarot_card_id);
CREATE INDEX IF NOT EXISTS idx_paths_connects_from ON paths(connects_from);
CREATE INDEX IF NOT EXISTS idx_paths_connects_to ON paths(connects_to);

CREATE INDEX IF NOT EXISTS idx_planets_name ON planets(name);
CREATE INDEX IF NOT EXISTS idx_planets_sephiroth ON planets(sephiroth_number);

CREATE INDEX IF NOT EXISTS idx_zodiac_element ON zodiac_signs(element);
CREATE INDEX IF NOT EXISTS idx_zodiac_modality ON zodiac_signs(modality);
CREATE INDEX IF NOT EXISTS idx_zodiac_ruling_planet ON zodiac_signs(ruling_planet);

CREATE INDEX IF NOT EXISTS idx_lunar_mansions_number ON lunar_mansions(number);
CREATE INDEX IF NOT EXISTS idx_lunar_mansions_sign ON lunar_mansions(zodiac_sign);

CREATE INDEX IF NOT EXISTS idx_rituals_tradition ON rituals(tradition);
CREATE INDEX IF NOT EXISTS idx_rituals_category ON rituals(category);
CREATE INDEX IF NOT EXISTS idx_rituals_difficulty ON rituals(difficulty);

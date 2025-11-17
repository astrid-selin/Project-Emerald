"""
Comprehensive Tarot Card Correspondences
Including Qabbalah, musical notes, colors, gemstones, and other esoteric attributes
Based on Golden Dawn, Thoth, and traditional systems
"""

# Major Arcana Correspondences
MAJOR_ARCANA_CORRESPONDENCES = {
    "The Fool": {
        "hebrew_letter": "Aleph",
        "tree_of_life_path": "11 (Kether to Chokmah)",
        "sephiroth": None,
        "musical_note": "E",
        "color_primary": "Bright pale yellow",
        "color_secondary": "Sky blue",
        "gemstone": "Topaz",
        "herb": "Aspen, Ginseng",
        "key_symbols": "Dog, white rose, cliff, sun, mountains, bundle"
    },
    "The Magician": {
        "hebrew_letter": "Beth",
        "tree_of_life_path": "12 (Kether to Binah)",
        "sephiroth": None,
        "musical_note": "E (between D and E)",
        "color_primary": "Yellow",
        "color_secondary": "Purple",
        "gemstone": "Opal, Agate",
        "herb": "Vervain, Palm",
        "key_symbols": "Infinity symbol, wand, cup, sword, pentacle, roses, lilies"
    },
    "The High Priestess": {
        "hebrew_letter": "Gimel",
        "tree_of_life_path": "13 (Kether to Tiphareth)",
        "sephiroth": None,
        "musical_note": "G#",
        "color_primary": "Blue",
        "color_secondary": "Silver",
        "gemstone": "Moonstone, Pearl",
        "herb": "Pomegranate, Almond",
        "key_symbols": "Pillars (B and J), veil, crescent moon, Torah scroll, water"
    },
    "The Empress": {
        "hebrew_letter": "Daleth",
        "tree_of_life_path": "14 (Chokmah to Binah)",
        "sephiroth": None,
        "musical_note": "F#",
        "color_primary": "Emerald Green",
        "color_secondary": "Pink",
        "gemstone": "Emerald, Turquoise",
        "herb": "Myrtle, Rose",
        "key_symbols": "Venus symbol, crown, wheat, waterfall, cushioned throne"
    },
    "The Emperor": {
        "hebrew_letter": "Heh (Tzaddi in Thoth)",
        "tree_of_life_path": "15 (Chokmah to Tiphareth)",
        "sephiroth": None,
        "musical_note": "C",
        "color_primary": "Scarlet Red",
        "color_secondary": "Orange",
        "gemstone": "Ruby, Diamond",
        "herb": "Tiger Lily, Geranium",
        "key_symbols": "Ram heads, ankh, orb, scepter, stone throne, mountains"
    },
    "The Hierophant": {
        "hebrew_letter": "Vau",
        "tree_of_life_path": "16 (Chokmah to Chesed)",
        "sephiroth": None,
        "musical_note": "C#",
        "color_primary": "Red-Orange",
        "color_secondary": "Deep Indigo",
        "gemstone": "Topaz, Diamond",
        "herb": "Mallow, Clover",
        "key_symbols": "Triple crown, crossed keys, two pillars, two acolytes, hand blessing"
    },
    "The Lovers": {
        "hebrew_letter": "Zain",
        "tree_of_life_path": "17 (Binah to Tiphareth)",
        "sephiroth": None,
        "musical_note": "D",
        "color_primary": "Orange",
        "color_secondary": "Pale mauve",
        "gemstone": "Alexandrite, Agate",
        "herb": "Orchid, Mace",
        "key_symbols": "Angel Raphael, man and woman, tree of knowledge, tree of life, serpent"
    },
    "The Chariot": {
        "hebrew_letter": "Cheth",
        "tree_of_life_path": "18 (Binah to Geburah)",
        "sephiroth": None,
        "musical_note": "D#",
        "color_primary": "Amber",
        "color_secondary": "Maroon",
        "gemstone": "Amber, Chalcedony",
        "herb": "Lotus, Water Lily",
        "key_symbols": "Sphinxes (black and white), starry canopy, crescent moons, water"
    },
    "Strength": {
        "hebrew_letter": "Teth",
        "tree_of_life_path": "19 (Chesed to Geburah)",
        "sephiroth": None,
        "musical_note": "E",
        "color_primary": "Yellow-Green",
        "color_secondary": "Deep purple",
        "gemstone": "Cat's Eye, Sardonyx",
        "herb": "Sunflower, Marigold",
        "key_symbols": "Lion, infinity symbol, woman, white robe, mountains, flowers"
    },
    "The Hermit": {
        "hebrew_letter": "Yod",
        "tree_of_life_path": "20 (Chesed to Tiphareth)",
        "sephiroth": None,
        "musical_note": "F",
        "color_primary": "Yellow-Green",
        "color_secondary": "Slate grey",
        "gemstone": "Peridot, Olivine",
        "herb": "Snowdrop, Lily",
        "key_symbols": "Lantern with six-pointed star, staff, mountain peak, grey robes"
    },
    "Wheel of Fortune": {
        "hebrew_letter": "Kaph",
        "tree_of_life_path": "21 (Chesed to Netzach)",
        "sephiroth": None,
        "musical_note": "A#",
        "color_primary": "Violet",
        "color_secondary": "Blue",
        "gemstone": "Sapphire, Amethyst",
        "herb": "Hyssop, Oak",
        "key_symbols": "Wheel, sphinx, serpent, Anubis, TARO/ROTA, Hebrew letters (YHVH)"
    },
    "Justice": {
        "hebrew_letter": "Lamed",
        "tree_of_life_path": "22 (Geburah to Tiphareth)",
        "sephiroth": None,
        "musical_note": "F#",
        "color_primary": "Emerald Green",
        "color_secondary": "Blue-green",
        "gemstone": "Emerald, Jade",
        "herb": "Aloe, Eucalyptus",
        "key_symbols": "Scales, sword, purple cloak, crown, pillars, veil"
    },
    "The Hanged Man": {
        "hebrew_letter": "Mem",
        "tree_of_life_path": "23 (Geburah to Hod)",
        "sephiroth": None,
        "musical_note": "G#",
        "color_primary": "Deep Blue",
        "color_secondary": "Sea green",
        "gemstone": "Aquamarine, Beryl",
        "herb": "Myrrh, Dulse",
        "key_symbols": "Inverted man, halo, T-cross, bound foot, calm expression"
    },
    "Death": {
        "hebrew_letter": "Nun",
        "tree_of_life_path": "24 (Tiphareth to Netzach)",
        "sephiroth": None,
        "musical_note": "G",
        "color_primary": "Blue-Green",
        "color_secondary": "Dull brown",
        "gemstone": "Snakestone, Obsidian",
        "herb": "Cactus, Wormwood",
        "key_symbols": "Skeleton, white horse, black flag with white rose, sun, people of all classes"
    },
    "Temperance": {
        "hebrew_letter": "Samekh",
        "tree_of_life_path": "25 (Tiphareth to Yesod)",
        "sephiroth": None,
        "musical_note": "G#",
        "color_primary": "Blue",
        "color_secondary": "Yellow",
        "gemstone": "Jacinth, Amethyst",
        "herb": "Rush, Arrowroot",
        "key_symbols": "Angel, triangle, cups, water flow, path, mountain, sun/crown"
    },
    "The Devil": {
        "hebrew_letter": "Ayin",
        "tree_of_life_path": "26 (Tiphareth to Hod)",
        "sephiroth": None,
        "musical_note": "A",
        "color_primary": "Indigo",
        "color_secondary": "Black",
        "gemstone": "Black Diamond, Jet",
        "herb": "Orchid, Thistle",
        "key_symbols": "Baphomet, inverted pentagram, chains, naked humans, torch, grapes"
    },
    "The Tower": {
        "hebrew_letter": "Peh",
        "tree_of_life_path": "27 (Netzach to Hod)",
        "sephiroth": None,
        "musical_note": "C",
        "color_primary": "Scarlet",
        "color_secondary": "Red",
        "gemstone": "Ruby, Garnet",
        "herb": "Hibiscus, Nettle",
        "key_symbols": "Lightning, falling crown, falling figures, flames, grey clouds"
    },
    "The Star": {
        "hebrew_letter": "Heh (Tzaddi in traditional)",
        "tree_of_life_path": "28 (Netzach to Yesod)",
        "sephiroth": None,
        "musical_note": "A#",
        "color_primary": "Violet",
        "color_secondary": "Sky blue",
        "gemstone": "Turquoise, Aquamarine",
        "herb": "Olive, Coconut",
        "key_symbols": "Large star, seven smaller stars, naked woman, two pools, ibis, water pouring"
    },
    "The Moon": {
        "hebrew_letter": "Qoph",
        "tree_of_life_path": "29 (Netzach to Malkuth)",
        "sephiroth": None,
        "musical_note": "B",
        "color_primary": "Crimson (ultra-violet)",
        "color_secondary": "Buff flecked silver-white",
        "gemstone": "Pearl, Crystal",
        "herb": "Opium, Poppy",
        "key_symbols": "Moon, dog, wolf, crayfish, path, towers, water"
    },
    "The Sun": {
        "hebrew_letter": "Resh",
        "tree_of_life_path": "30 (Hod to Yesod)",
        "sephiroth": None,
        "musical_note": "D",
        "color_primary": "Orange",
        "color_secondary": "Gold-yellow",
        "gemstone": "Sunstone, Diamond",
        "herb": "Sunflower, Heliotrope",
        "key_symbols": "Sun, child, white horse, sunflowers, wall, red banner"
    },
    "Judgement": {
        "hebrew_letter": "Shin",
        "tree_of_life_path": "31 (Hod to Malkuth)",
        "sephiroth": None,
        "musical_note": "C",
        "color_primary": "Glowing orange-scarlet",
        "color_secondary": "Vermillion",
        "gemstone": "Fire Opal, Garnet",
        "herb": "Red Poppy, Hibiscus",
        "key_symbols": "Angel Gabriel, trumpet, cross, rising people, coffins, mountains, water"
    },
    "The World": {
        "hebrew_letter": "Tau",
        "tree_of_life_path": "32 (Yesod to Malkuth)",
        "sephiroth": None,
        "musical_note": "A",
        "color_primary": "Indigo",
        "color_secondary": "Black",
        "gemstone": "Onyx, Salt",
        "herb": "Oak, Ivy, Ash",
        "key_symbols": "Dancer, wreath, four creatures (lion, bull, angel, eagle), wands"
    }
}

# Minor Arcana Suit Correspondences
SUIT_CORRESPONDENCES = {
    "Wands": {
        "element": "Fire",
        "color_primary": "Red",
        "color_secondary": "Orange",
        "musical_note": "C (base)",
        "season": "Spring",
        "qabbalah_world": "Atziluth (Archetypal)",
        "direction": "South"
    },
    "Cups": {
        "element": "Water",
        "color_primary": "Blue",
        "color_secondary": "Silver",
        "musical_note": "G# (base)",
        "season": "Summer",
        "qabbalah_world": "Briah (Creative)",
        "direction": "West"
    },
    "Swords": {
        "element": "Air",
        "color_primary": "Yellow",
        "color_secondary": "Violet",
        "musical_note": "E (base)",
        "season": "Autumn",
        "qabbalah_world": "Yetzirah (Formative)",
        "direction": "East"
    },
    "Pentacles": {
        "element": "Earth",
        "color_primary": "Green",
        "color_secondary": "Brown",
        "musical_note": "F (base)",
        "season": "Winter",
        "qabbalah_world": "Assiah (Material)",
        "direction": "North"
    }
}

# Court Cards Correspondences
COURT_CARDS = {
    "Page": {
        "qabbalah_element": "Earth of [Suit]",
        "age": "Youth",
        "represents": "Student, messenger, new energy"
    },
    "Knight": {
        "qabbalah_element": "Air of [Suit] (Fire in some systems)",
        "age": "Young adult",
        "represents": "Action, movement, quest"
    },
    "Queen": {
        "qabbalah_element": "Water of [Suit]",
        "age": "Mature feminine",
        "represents": "Mastery, nurturing, inner power"
    },
    "King": {
        "qabbalah_element": "Fire of [Suit] (Air in some systems)",
        "age": "Mature masculine",
        "represents": "Authority, mastery, outer power"
    }
}

# Pip Cards Sephiroth and Decan Correspondences
PIP_CORRESPONDENCES = {
    "Ace": {
        "sephiroth": "Kether (Crown)",
        "meaning": "Root/Essence of suit",
        "decan": None
    },
    "Two": {
        "sephiroth": "Chokmah (Wisdom)",
        "wands_decan": "Mars in Aries",
        "cups_decan": "Venus in Cancer",
        "swords_decan": "Moon in Libra",
        "pentacles_decan": "Jupiter in Capricorn"
    },
    "Three": {
        "sephiroth": "Binah (Understanding)",
        "wands_decan": "Sun in Aries",
        "cups_decan": "Mercury in Cancer",
        "swords_decan": "Saturn in Libra",
        "pentacles_decan": "Mars in Capricorn"
    },
    "Four": {
        "sephiroth": "Chesed (Mercy)",
        "wands_decan": "Venus in Aries",
        "cups_decan": "Moon in Cancer",
        "swords_decan": "Jupiter in Libra",
        "pentacles_decan": "Sun in Capricorn"
    },
    "Five": {
        "sephiroth": "Geburah (Severity)",
        "wands_decan": "Saturn in Leo",
        "cups_decan": "Mars in Scorpio",
        "swords_decan": "Venus in Aquarius",
        "pentacles_decan": "Mercury in Taurus"
    },
    "Six": {
        "sephiroth": "Tiphareth (Beauty)",
        "wands_decan": "Jupiter in Leo",
        "cups_decan": "Sun in Scorpio",
        "swords_decan": "Mercury in Aquarius",
        "pentacles_decan": "Moon in Taurus"
    },
    "Seven": {
        "sephiroth": "Netzach (Victory)",
        "wands_decan": "Mars in Leo",
        "cups_decan": "Venus in Scorpio",
        "swords_decan": "Moon in Aquarius",
        "pentacles_decan": "Saturn in Taurus"
    },
    "Eight": {
        "sephiroth": "Hod (Splendor)",
        "wands_decan": "Mercury in Sagittarius",
        "cups_decan": "Saturn in Pisces",
        "swords_decan": "Jupiter in Gemini",
        "pentacles_decan": "Sun in Virgo"
    },
    "Nine": {
        "sephiroth": "Yesod (Foundation)",
        "wands_decan": "Moon in Sagittarius",
        "cups_decan": "Jupiter in Pisces",
        "swords_decan": "Mars in Gemini",
        "pentacles_decan": "Venus in Virgo"
    },
    "Ten": {
        "sephiroth": "Malkuth (Kingdom)",
        "wands_decan": "Saturn in Sagittarius",
        "cups_decan": "Mars in Pisces",
        "swords_decan": "Sun in Gemini",
        "pentacles_decan": "Mercury in Virgo"
    }
}

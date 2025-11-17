"""
System-Specific Tarot Card Descriptions
From major tarot systems: Rider-Waite-Smith (RWS), Thoth, Golden Dawn, and Marseille
"""

# Rider-Waite-Smith System Descriptions (1909)
RWS_DESCRIPTIONS = {
    "The Fool": {
        "description": "A young man in colorful garments stands at the edge of a precipice, looking upward with a white rose in hand. A small dog leaps at his heels. He carries a small bundle on a staff over his shoulder.",
        "upright_meaning": "New beginnings, adventure, innocence, unlimited potential, free spirit",
        "reversed_meaning": "Naivety, foolishness, recklessness, risk-taking, inconsideration",
        "key_imagery": "White rose (purity), precipice (unknown), dog (loyalty/instinct), mountains (challenges ahead), sun (consciousness)",
        "divinatory_meaning": "Folly, mania, extravagance, intoxication, delirium, frenzy, betrayal",
        "esoteric_meaning": "The spirit in search of experience, the divine breath about to crystallize into matter"
    },
    "The Magician": {
        "description": "A red-robed figure stands before a table bearing the four suit symbols. One hand points to heaven, the other to earth. An infinity symbol hovers above his head. Roses and lilies grow around him.",
        "upright_meaning": "Manifestation, willpower, desire, creation, resourcefulness, power",
        "reversed_meaning": "Manipulation, cunning, wasted talent, illusion, deception",
        "key_imagery": "Infinity symbol (unlimited potential), four symbols (mastery of elements), white wand (willpower), red robe (activity), white undergarment (purity)",
        "divinatory_meaning": "Skill, diplomacy, address, subtlety, pain, loss, disaster, snares of enemies, self-confidence",
        "esoteric_meaning": "The conscious will to create, the bridge between divine consciousness and earthly manifestation"
    },
    "The High Priestess": {
        "description": "A woman sits between two pillars marked 'B' and 'J', holding a scroll marked 'TORA'. A crescent moon sits at her feet. Behind her hangs a veil decorated with pomegranates and palms.",
        "upright_meaning": "Intuition, sacred knowledge, subconscious mind, mystery, divine feminine",
        "reversed_meaning": "Hidden agendas, secrets, information withheld, lack of personal harmony",
        "key_imagery": "Pillars B and J (duality, Solomon's temple), veil (mysteries), scroll/Torah (divine law), moon (intuition), blue robe (knowledge)",
        "divinatory_meaning": "Secrets, mystery, the unrevealed future, silence, tenacity, wisdom, science",
        "esoteric_meaning": "The virgin principle of the universe, the gateway to the inner mysteries"
    },
    "The Empress": {
        "description": "A crowned woman sits on a luxurious throne in a lush garden. She wears a gown decorated with pomegranates and holds a scepter. A heart-shaped shield with the Venus symbol leans against her throne.",
        "upright_meaning": "Femininity, abundance, nature, fertility, nurturing, sensuality, creativity",
        "reversed_meaning": "Dependence, smothering, emptiness, nosiness, lack of growth",
        "key_imagery": "Venus symbol (love and beauty), crown of twelve stars (connection to zodiac), pomegranates (fertility), wheat (abundance), flowing water (emotions)",
        "divinatory_meaning": "Fruitfulness, action, initiative, length of days, the unknown, clandestine, difficulty, doubt, ignorance",
        "esoteric_meaning": "The great mother, nature's abundance, the anima mundi"
    },
    "The Emperor": {
        "description": "An emperor sits on a throne decorated with ram heads, holding an ankh and an orb. He wears armor beneath his robes and a golden crown. Barren mountains rise behind him.",
        "upright_meaning": "Authority, structure, control, fatherhood, stability, power, protection",
        "reversed_meaning": "Domination, excessive control, rigidity, inflexibility, lack of discipline",
        "key_imagery": "Ram heads (Aries), ankh (life), orb (world), armor (protection), stone throne (stability), barren mountains (masculine yang)",
        "divinatory_meaning": "Stability, power, protection, realization, conviction, also war, conquest, victory",
        "esoteric_meaning": "Temporal power, the archetype of the Father, reason in its highest form"
    },
    # Additional major arcana cards would continue...
}

# Thoth Tarot System Descriptions (Aleister Crowley/Lady Frieda Harris, 1969)
THOTH_DESCRIPTIONS = {
    "The Fool": {
        "description": "A divine child figure leaps forward with spiraling energy. A white tiger and dove accompany him. Geometric patterns and symbols of Dionysus surround the figure in vibrant colors.",
        "upright_meaning": "The primordial creative force, divine inspiration, air element, infinite possibility, the Holy Guardian Angel",
        "reversed_meaning": "Not traditionally reversed in Thoth system",
        "key_imagery": "Spiraling horns (creative force), tiger (passionate energy), dove (purity), grapes (Dionysus), geometric patterns (sacred geometry)",
        "divinatory_meaning": "Idea, thought, spirituality, that which endeavors to rise above the material",
        "esoteric_meaning": "The Fool represents the negative veiling the Ain (nothingness), the primordial potential before manifestation, associated with air and Aleph"
    },
    "The Magician": {
        "description": "The Magus figure manipulates cosmic energies, crowned with an Ibis-headed wand. The caduceus, winged eggs, and magical implements surround him. Monkeys of Thoth dance at the bottom.",
        "upright_meaning": "Communication, skill, the Word, Mercury, trickster energy, versatility, dexterity",
        "reversed_meaning": "Not traditionally reversed in Thoth system",
        "key_imagery": "Caduceus (Hermes/Mercury), Ibis (Thoth), winged eggs (potential), monkeys (mind), scrolls (knowledge), eight spokes (directions)",
        "divinatory_meaning": "Skill, wisdom, adaptability, craft, cunning, address, sometimes occult wisdom or power",
        "esoteric_meaning": "The messenger of the gods, the word made manifest, consciousness directing will through communication"
    },
    "The High Priestess": {
        "description": "Isis-Artemis figure veiled in light, seated between pillars. She holds the bow of Artemis. The moon in its phases crowns her head. The mysteries of life and death flow around her.",
        "upright_meaning": "Purity, virginity, the Moon, mysteries unrevealed, sacred feminine wisdom, intuition",
        "reversed_meaning": "Not traditionally reversed in Thoth system",
        "key_imagery": "Camel (Gimel), lunar phases, bow of Artemis, fruit of life, crystalline structure, flowing energy",
        "divinatory_meaning": "Pure, exalted and gracious influence enters the matter, change, fluctuation, alternation",
        "esoteric_meaning": "The idea of the Moon, the most spiritual form of Isis, the link between supernal and mundane consciousness"
    },
    "The Empress": {
        "description": "A radiant figure holds a lotus wand seated on a throne. The alchemical symbol for Venus dominates. A pelican feeds its young. Geometric patterns of bees and flames surround her.",
        "upright_meaning": "Love, beauty, Venus, alchemical salt, the gate of heaven, creation, growth",
        "reversed_meaning": "Not traditionally reversed in Thoth system",
        "key_imagery": "Venus symbol, pelican (sacrifice for offspring), lotus (enlightenment), bees (industry), twin pillars, flames",
        "divinatory_meaning": "Love, beauty, happiness, pleasure, success, fruitfulness, good fortune, graciousness, elegance",
        "esoteric_meaning": "The gateway of heaven, daughter of the mighty ones, the alchemical process of creation"
    },
    "The Emperor": {
        "description": "A powerful figure sits on a throne, crowned and holding a scepter topped with a ram's head. The Lamb and the Bee appear. Fleur-de-lis patterns and solar symbolism dominate.",
        "upright_meaning": "War, energy, Aries, paternal power, authority, the Sun in exaltation, structure, dominion",
        "reversed_meaning": "Not traditionally reversed in Thoth system",
        "key_imagery": "Ram (Aries), disc of the sun, orb and scepter, fleur-de-lis (spiritual power), bee (industry), lamb (sacrifice)",
        "divinatory_meaning": "War, conquest, victory, strife, ambition, realization of authority, worldly power",
        "esoteric_meaning": "The son of the morning, chief among the mighty, war-like in defense of the people"
    },
    # Additional major arcana cards would continue...
}

# Golden Dawn System Descriptions
GOLDEN_DAWN_DESCRIPTIONS = {
    "The Fool": {
        "description": "A figure poised at the edge of an abyss, representing the negative above the Tree of Life. The dark abyss below, the limitless light above.",
        "upright_meaning": "The Spiritual Air, the breath of life, the crown of wisdom, folly if ill-dignified",
        "reversed_meaning": "Folly, wavering, instability, trouble from unforeseen or unexpected sources",
        "key_imagery": "Aleph symbol, air symbolism, position before manifestation, butterfly of transformation",
        "divinatory_meaning": "In spiritual matters, wisdom. In material matters, foolishness, eccentricity, or even mania if ill-dignified",
        "esoteric_meaning": "The Negative Existence sending forth a Ray, the cohesive principle of the universe"
    },
    "The Magician": {
        "description": "The Juggler or Magus stands with the implements of magic before him, channeling divine power into earthly form through will and concentration.",
        "upright_meaning": "Skill, wisdom, adaptation, craft, eloquence, the connection of Kether with Binah",
        "reversed_meaning": "Weakness, lack of skill, failure to use talents, deception",
        "key_imagery": "Four magical implements, Beth (house), the path connecting the supernals",
        "divinatory_meaning": "Skill, wisdom, diplomacy, craft, cunning, the use of magical powers",
        "esoteric_meaning": "The transparent intelligence, the channel through which divine wisdom flows"
    },
    "The High Priestess": {
        "description": "The Priestess of the Silver Star sits veiled between the pillars, guardian of the mysteries, the path from Kether to Tiphareth through the Abyss.",
        "upright_meaning": "Wisdom, knowledge, learning, intuition, the Moon in its highest aspect, secrets revealed to the worthy",
        "reversed_meaning": "Conceit, ignorance, shallowness, passion, moral or physical ardor",
        "key_imagery": "Gimel (camel), the Moon, the veil of the temple, the crossing of the Abyss",
        "divinatory_meaning": "Pure and exalted influence, wisdom, learning, change but with constancy",
        "esoteric_meaning": "The Uniting Intelligence, the link between the highest and middle pillar of the Tree"
    },
    "The Empress": {
        "description": "The Daughter of the Mighty Ones, the sacred feminine principle seated in abundance, the path connecting Wisdom and Understanding.",
        "upright_meaning": "Love, beauty, happiness, pleasure, success, the sacred feminine, Venus in exaltation",
        "reversed_meaning": "Dissipation, debauchery, loss, sterility, delay",
        "key_imagery": "Daleth (door), Venus, the gateway, lush vegetation, flowing water",
        "divinatory_meaning": "Love, beauty, happiness, luxury, sometimes dissipation",
        "esoteric_meaning": "The Luminous Intelligence, the gate through which the soul may ascend"
    },
    "The Emperor": {
        "description": "The Son of the Morning, constituting the throne of power, the path from Wisdom to Mercy, temporal and spiritual authority combined.",
        "upright_meaning": "Authority, power, leadership, Aries, war, conquest when necessary, stability through strength",
        "reversed_meaning": "Loss of power, weakness, tyranny, immaturity, ineffectiveness",
        "key_imagery": "Heh or Tzaddi (window), Aries the Ram, sight and vision, the constituting intelligence",
        "divinatory_meaning": "War, conquest, victory, strife, ambition, originality, over-weening confidence and megalomania",
        "esoteric_meaning": "The Constituting Intelligence, establishing the foundations of reality"
    },
    # Additional major arcana cards would continue...
}

# Marseille System Descriptions (Traditional, pre-1700s)
MARSEILLE_DESCRIPTIONS = {
    "The Fool": {
        "description": "A wanderer in colorful patched clothing walks with a staff, a small animal (dog or cat) at his heels appearing to bite or pull at him. Simple, archetypal imagery.",
        "upright_meaning": "The wanderer, the outsider, unlimited potential, divine madness, the beginning and end",
        "reversed_meaning": "Obsession, hesitation, bad decision, apathy, indecision",
        "key_imagery": "Patched clothing (poverty/simplicity), staff (support), animal (base instincts), bundle (material possessions)",
        "divinatory_meaning": "Folly, madness, carelessness, creative expression, lack of discipline, wandering",
        "esoteric_meaning": "The soul before incarnation, the spirit not yet bound by matter"
    },
    "The Magician": {
        "description": "Known as 'Le Bateleur' (The Juggler), a figure stands before a table with various objects, performing or displaying goods as a street magician or merchant.",
        "upright_meaning": "Skill, dexterity, sleight of hand, communication, the trickster, initiative",
        "reversed_meaning": "Deceit, trickery, lack of skill, delays, unclear communication",
        "key_imagery": "Table with objects, hat (sometimes infinity-shaped), wand or pointer, merchant display",
        "divinatory_meaning": "Initiative, action, beginning of an enterprise, sometimes trickery or deception",
        "esoteric_meaning": "The active principle, human will and skill applied to material reality"
    },
    "The High Priestess": {
        "description": "Known as 'La Papesse' (The Popess), a seated female religious figure holds a book, wearing papal regalia. Associated with the legendary Pope Joan.",
        "upright_meaning": "Hidden knowledge, secrets, feminine spiritual authority, study, patience",
        "reversed_meaning": "Ignorance, superficiality, inability to access inner wisdom",
        "key_imagery": "Book (secret knowledge), papal tiara and robes (spiritual authority), seated pose (contemplation)",
        "divinatory_meaning": "Secrets, mystery, science, wisdom, silence, hidden knowledge, the unrevealed",
        "esoteric_meaning": "The hidden wisdom, the divine feminine in its contemplative aspect"
    },
    "The Empress": {
        "description": "Known as 'L'Impératrice', a crowned and seated female figure holds a scepter and shield, representing temporal feminine power and sovereignty.",
        "upright_meaning": "Feminine power, fertility, abundance, earthly authority, material wealth",
        "reversed_meaning": "Poverty, sterility, delays, obstacles, domestic problems",
        "key_imagery": "Crown (sovereignty), shield (protection), scepter (power), throne (stability)",
        "divinatory_meaning": "Fruitfulness, material wealth, sovereignty, power, marriage, children",
        "esoteric_meaning": "The material mother, earthly abundance and sovereignty"
    },
    "The Emperor": {
        "description": "Known as 'L'Empereur', a crowned, bearded figure sits in profile on a throne, holding a scepter and orb, representing temporal masculine authority.",
        "upright_meaning": "Masculine power, authority, structure, law, fatherhood, leadership",
        "reversed_meaning": "Tyranny, rigidity, loss of authority, immaturity, weakness",
        "key_imagery": "Crown (authority), orb (world dominion), scepter (power), profile pose (decisive action), throne",
        "divinatory_meaning": "Authority, power, leadership, sometimes war or conflict, stability, establishment",
        "esoteric_meaning": "The material father, temporal authority and order"
    },
    # Additional major arcana cards would continue...
}

def get_system_description(card_name, system):
    """
    Retrieve system-specific description for a card

    Args:
        card_name: Name of the tarot card
        system: One of 'RWS', 'Thoth', 'Golden Dawn', or 'Marseille'

    Returns:
        Dictionary with system-specific description or None
    """
    systems = {
        'RWS': RWS_DESCRIPTIONS,
        'Thoth': THOTH_DESCRIPTIONS,
        'Golden Dawn': GOLDEN_DAWN_DESCRIPTIONS,
        'Marseille': MARSEILLE_DESCRIPTIONS
    }

    return systems.get(system, {}).get(card_name)

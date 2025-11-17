#!/usr/bin/env python3
"""
Migration Script: JSON to SQLite
Converts tarot_data.json to a comprehensive SQLite database with esoteric correspondences
and descriptions from multiple tarot systems (RWS, Thoth, Golden Dawn, Marseille)
"""

import json
import sqlite3
import os
from datetime import datetime
from card_correspondences import (
    MAJOR_ARCANA_CORRESPONDENCES,
    SUIT_CORRESPONDENCES,
    COURT_CARDS,
    PIP_CORRESPONDENCES
)
from system_descriptions import (
    RWS_DESCRIPTIONS,
    THOTH_DESCRIPTIONS,
    GOLDEN_DAWN_DESCRIPTIONS,
    MARSEILLE_DESCRIPTIONS
)
from seed_qabalah import seed_sephiroth, seed_paths
from seed_astrology import seed_planets, seed_zodiac_signs
from seed_rituals import seed_rituals


class TarotDatabaseMigration:
    def __init__(self, json_file='tarot_data.json', db_file='esoteric_knowledge.db'):
        self.json_file = json_file
        self.db_file = db_file
        self.conn = None
        self.cursor = None

    def connect(self):
        """Create database connection"""
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        print(f"✓ Connected to database: {self.db_file}")

    def load_json_data(self):
        """Load existing JSON data"""
        with open(self.json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✓ Loaded {len(data['cards'])} cards from {self.json_file}")
        return data['cards']

    def create_schema(self):
        """Create database schema from schema.sql"""
        with open('schema.sql', 'r') as f:
            schema_sql = f.read()

        # Execute schema (split by semicolons for multiple statements)
        for statement in schema_sql.split(';'):
            if statement.strip():
                self.cursor.execute(statement)

        self.conn.commit()
        print("✓ Database schema created")

    def get_minor_arcana_correspondences(self, card_name, suit):
        """Get correspondences for minor arcana cards"""
        correspondences = {}

        # Get suit-level correspondences
        if suit in SUIT_CORRESPONDENCES:
            suit_data = SUIT_CORRESPONDENCES[suit]
            correspondences['color_primary'] = suit_data['color_primary']
            correspondences['color_secondary'] = suit_data['color_secondary']
            correspondences['musical_note'] = suit_data['musical_note']

        # Determine card type (Ace, Two-Ten, or Court)
        card_parts = card_name.split(' of ')
        if len(card_parts) == 2:
            rank = card_parts[0]

            # Court cards
            if rank in COURT_CARDS:
                court_data = COURT_CARDS[rank]
                correspondences['sephiroth'] = court_data['qabbalah_element'].replace('[Suit]', suit)

            # Pip cards (Ace through Ten)
            elif rank in PIP_CORRESPONDENCES:
                pip_data = PIP_CORRESPONDENCES[rank]
                correspondences['sephiroth'] = pip_data['sephiroth']

                # Get astrological decan
                suit_lower = suit.lower()
                decan_key = f"{suit_lower}_decan"
                if decan_key in pip_data:
                    correspondences['astrological_decan'] = pip_data[decan_key]

        return correspondences

    def insert_card(self, card_data):
        """Insert a card into the database with all correspondences"""
        card_name = card_data['name']
        is_major = card_data['arcana'] == 'Major Arcana'

        # Start with base data from JSON
        insert_data = {
            'number': card_data['number'],
            'name': card_name,
            'arcana': card_data['arcana'],
            'suit': card_data.get('suit'),
            'element': card_data.get('element'),
            'astrology': card_data.get('astrology'),
            'upright_meaning': card_data['upright_meaning'],
            'reversed_meaning': card_data['reversed_meaning'],
            'description': card_data['description']
        }

        # Add correspondences based on card type
        if is_major and card_name in MAJOR_ARCANA_CORRESPONDENCES:
            corr = MAJOR_ARCANA_CORRESPONDENCES[card_name]
            insert_data.update({
                'hebrew_letter': corr.get('hebrew_letter'),
                'tree_of_life_path': corr.get('tree_of_life_path'),
                'sephiroth': corr.get('sephiroth'),
                'musical_note': corr.get('musical_note'),
                'color_primary': corr.get('color_primary'),
                'color_secondary': corr.get('color_secondary'),
                'gemstone': corr.get('gemstone'),
                'herb': corr.get('herb'),
                'key_symbols': corr.get('key_symbols')
            })
        else:
            # Minor arcana
            minor_corr = self.get_minor_arcana_correspondences(
                card_name,
                card_data.get('suit')
            )
            insert_data.update(minor_corr)

            # Set astrological_decan if available
            if 'astrological_decan' in minor_corr:
                insert_data['astrological_decan'] = minor_corr['astrological_decan']

        # Insert card
        columns = ', '.join(insert_data.keys())
        placeholders = ', '.join(['?' for _ in insert_data])
        sql = f"INSERT INTO cards ({columns}) VALUES ({placeholders})"

        self.cursor.execute(sql, list(insert_data.values()))
        card_id = self.cursor.lastrowid

        # Insert keywords
        for keyword in card_data.get('keywords', []):
            self.cursor.execute(
                "INSERT INTO keywords (card_id, keyword) VALUES (?, ?)",
                (card_id, keyword)
            )

        return card_id

    def insert_system_descriptions(self, card_id, card_name):
        """Insert system-specific descriptions for a card"""
        systems = {
            'RWS': RWS_DESCRIPTIONS,
            'Thoth': THOTH_DESCRIPTIONS,
            'Golden Dawn': GOLDEN_DAWN_DESCRIPTIONS,
            'Marseille': MARSEILLE_DESCRIPTIONS
        }

        for system_name, descriptions in systems.items():
            if card_name in descriptions:
                desc_data = descriptions[card_name]

                self.cursor.execute("""
                    INSERT INTO system_descriptions
                    (card_id, system_name, description, upright_meaning, reversed_meaning,
                     key_imagery, divinatory_meaning, esoteric_meaning)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    card_id,
                    system_name,
                    desc_data.get('description'),
                    desc_data.get('upright_meaning'),
                    desc_data.get('reversed_meaning'),
                    desc_data.get('key_imagery'),
                    desc_data.get('divinatory_meaning'),
                    desc_data.get('esoteric_meaning')
                ))

    def migrate(self):
        """Run the full migration"""
        print("\n" + "="*60)
        print("Tarot Database Migration: JSON → SQLite")
        print("="*60 + "\n")

        # Remove existing database if it exists
        if os.path.exists(self.db_file):
            os.remove(self.db_file)
            print(f"✓ Removed existing database: {self.db_file}")

        # Connect and create schema
        self.connect()
        self.create_schema()

        # Load and migrate data
        cards = self.load_json_data()

        print("\nMigrating cards...")
        for i, card_data in enumerate(cards, 1):
            card_id = self.insert_card(card_data)
            self.insert_system_descriptions(card_id, card_data['name'])

            if i % 10 == 0:
                print(f"  Processed {i}/{len(cards)} cards...")

        self.conn.commit()
        print(f"\n✓ Successfully migrated {len(cards)} cards")

        # Seed Qabalah data
        print("\n" + "-"*60)
        print("Seeding Qabalah data...")
        print("-"*60)
        seed_sephiroth(self.cursor)
        seed_paths(self.cursor)
        self.conn.commit()

        # Seed Astrology data
        print("\n" + "-"*60)
        print("Seeding Astrology data...")
        print("-"*60)
        seed_planets(self.cursor)
        seed_zodiac_signs(self.cursor)
        self.conn.commit()

        # Seed Rituals data
        print("\n" + "-"*60)
        print("Seeding Rituals data...")
        print("-"*60)
        seed_rituals(self.cursor)
        self.conn.commit()

        # Print statistics
        self.print_statistics()

        # Close connection
        self.conn.close()
        print("\n✓ Database migration complete!")
        print(f"\nDatabase file: {os.path.abspath(self.db_file)}")
        print("="*60 + "\n")

    def print_statistics(self):
        """Print database statistics"""
        print("\n" + "="*60)
        print("DATABASE STATISTICS")
        print("="*60)

        # Card counts
        self.cursor.execute("SELECT COUNT(*) FROM cards")
        total_cards = self.cursor.fetchone()[0]
        print(f"\nTarot Cards:")
        print(f"  Total cards: {total_cards}")

        self.cursor.execute("SELECT COUNT(*) FROM cards WHERE arcana = 'Major Arcana'")
        major_count = self.cursor.fetchone()[0]
        print(f"  Major Arcana: {major_count}")

        self.cursor.execute("SELECT COUNT(*) FROM cards WHERE arcana = 'Minor Arcana'")
        minor_count = self.cursor.fetchone()[0]
        print(f"  Minor Arcana: {minor_count}")

        # Keywords count
        self.cursor.execute("SELECT COUNT(*) FROM keywords")
        keyword_count = self.cursor.fetchone()[0]
        print(f"  Total keywords: {keyword_count}")

        # System descriptions count
        self.cursor.execute("SELECT COUNT(*) FROM system_descriptions")
        system_desc_count = self.cursor.fetchone()[0]
        print(f"  System descriptions: {system_desc_count}")

        # Descriptions by system
        for system in ['RWS', 'Thoth', 'Golden Dawn', 'Marseille']:
            self.cursor.execute(
                "SELECT COUNT(*) FROM system_descriptions WHERE system_name = ?",
                (system,)
            )
            count = self.cursor.fetchone()[0]
            print(f"    {system}: {count}")

        # Qabalah counts
        self.cursor.execute("SELECT COUNT(*) FROM sephiroth")
        sephiroth_count = self.cursor.fetchone()[0]
        print(f"\nQabalah:")
        print(f"  Sephiroth: {sephiroth_count}")

        self.cursor.execute("SELECT COUNT(*) FROM paths")
        paths_count = self.cursor.fetchone()[0]
        print(f"  Paths: {paths_count}")

        # Astrology counts
        self.cursor.execute("SELECT COUNT(*) FROM planets")
        planets_count = self.cursor.fetchone()[0]
        print(f"\nAstrology:")
        print(f"  Planets: {planets_count}")

        self.cursor.execute("SELECT COUNT(*) FROM zodiac_signs")
        signs_count = self.cursor.fetchone()[0]
        print(f"  Zodiac signs: {signs_count}")

        # Rituals count
        self.cursor.execute("SELECT COUNT(*) FROM rituals")
        rituals_count = self.cursor.fetchone()[0]
        print(f"\nRituals:")
        print(f"  Total rituals: {rituals_count}")

        # Rituals by tradition
        self.cursor.execute("SELECT DISTINCT tradition FROM rituals")
        traditions = self.cursor.fetchall()
        for tradition in traditions:
            self.cursor.execute(
                "SELECT COUNT(*) FROM rituals WHERE tradition = ?",
                (tradition[0],)
            )
            count = self.cursor.fetchone()[0]
            print(f"    {tradition[0]}: {count}")

        print("="*60)


def main():
    """Main migration function"""
    migrator = TarotDatabaseMigration()
    migrator.migrate()


if __name__ == '__main__':
    main()

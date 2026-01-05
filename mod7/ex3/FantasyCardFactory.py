from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Any


class FantasyCardFactory(CardFactory):
    """
    A concrete factory that produces fantasy-themed game cards.

    This factory contains a predefined database of fantasy creatures, spells,
    and artifacts, and instantiates the appropriate concrete classes
    (CreatureCard, SpellCard, ArtifactCard) upon request.
    """

    def __init__(self) -> None:
        """
        Initialize the factory with a database of fantasy card definitions.
        """
        self._creatures: dict[str, dict[str, str | int]] = {
            "Fire Dragon": {
                "cost": 5,
                "rarity": "Legendary",
                "attack": 7,
                "health": 5
            },
            "Goblin Warrior": {
                "cost": 2,
                "rarity": "Common",
                "attack": 2,
                "health": 1
            },
            "Ice Wizard": {
                "cost": 4,
                "rarity": "Rare",
                "attack": 3,
                "health": 4
            },
            "Lightning Elemental": {
                "cost": 3,
                "rarity": "Uncommon",
                "attack": 4,
                "health": 2
            },
            "Stone Golem": {
                "cost": 6,
                "rarity": "Rare",
                "attack": 5,
                "health": 8
            },
            "Shadow Assassin": {
                "cost": 3,
                "rarity": "Uncommon",
                "attack": 5,
                "health": 2
            },
            "Healing Angel": {
                "cost": 4,
                "rarity": "Rare",
                "attack": 2,
                "health": 6
            },
            "Forest Sprite": {
                "cost": 1,
                "rarity": "Common",
                "attack": 1,
                "health": 1
            },
        }

        self._spells: dict[str, dict[str, str | int]] = {
            "Lightning Bolt": {
                "cost": 3,
                "rarity": "Common",
                "effect_type": "damage"
            },
            "Healing Potion": {
                "cost": 2,
                "rarity": "Common",
                "effect_type": "heal"
            },
            "Fireball": {
                "cost": 4,
                "rarity": "Uncommon",
                "effect_type": "damage"
            },
            "Shield Spell": {
                "cost": 1,
                "rarity": "Common",
                "effect_type": "buff"
            },
            "Meteor": {
                "cost": 8,
                "rarity": "Legendary",
                "effect_type": "damage"
            },
            "Ice Shard": {
                "cost": 2,
                "rarity": "Common",
                "effect_type": "damage"
            },
            "Divine Light": {
                "cost": 5,
                "rarity": "Rare",
                "effect_type": "heal"
            },
            "Magic Missile": {
                "cost": 1,
                "rarity": "Common",
                "effect_type": "damage"
            },
        }

        self._artifacts: dict[str, dict[str, str | int]] = {
            "Mana Crystal": {
                "cost": 2,
                "rarity": "Common",
                "durability": 5,
                "effect": "Permanent: +1 mana per turn"
            },
            "Sword of Power": {
                "cost": 3,
                "rarity": "Uncommon",
                "durability": 3,
                "effect": "Permanent: +2 attack"
            },
            "Ring of Wisdom": {
                "cost": 4,
                "rarity": "Rare",
                "durability": 4,
                "effect": "Permanent: Draw extra card"
            },
            "Shield of Defense": {
                "cost": 5,
                "rarity": "Rare",
                "durability": 6,
                "effect": "Permanent: +3 health"
            },
            "Crown of Kings": {
                "cost": 7,
                "rarity": "Legendary",
                "durability": 8,
                "effect": "Permanent: +1 cost reduction"
            },
            "Boots of Speed": {
                "cost": 2,
                "rarity": "Uncommon",
                "durability": 2,
                "effect": "Permanent: Cost -1"
            },
            "Cloak of Shadows": {
                "cost": 3,
                "rarity": "Uncommon",
                "durability": 3,
                "effect": "Permanent: Stealth"
            },
            "Staff of Elements": {
                "cost": 6,
                "rarity": "Legendary",
                "durability": 7,
                "effect": "Permanent: +1 spell damage"
            },
        }

    def _get_card_data(
        self,
        name_or_power: str | int,
        database: dict[str, dict[str, str | int]]
    ) -> tuple[str, dict[str, str | int]]:
        """
        Helper to find card data by name or power (cost).

        Args:
            name_or_power: The name (str) or cost (int) to search for.
            database: The dictionary to search (creatures, spells, etc).

        Returns:
            A tuple of (name, data_dict).
        """

        if isinstance(name_or_power, str):
            if name_or_power in database:
                return name_or_power, database[name_or_power]
            raise ValueError(f"Card '{name_or_power}' not found in factory.")
        for name, data in database.items():
            if "cost" in data:
                if data["cost"] == name_or_power:
                    return name, data
        raise ValueError(f"No card found with power/cost {name_or_power}")

    def create_creature(self, name_or_power: str | int) -> Card:
        """
        Create a new Creature card.

        Args:
            name_or_power (str | int): Name or mana cost of the creature.

        Returns:
            Card: A new CreatureCard instance.
        """

        name, data = self._get_card_data(name_or_power, self._creatures)

        return CreatureCard(
            name=name,
            cost=int(data["cost"]),
            rarity=str(data["rarity"]),
            attack=int(data["attack"]),
            health=int(data["health"])
        )

    def create_spell(self, name_or_power: str | int) -> Card:
        """
        Create a new Spell card.

        Args:
            name_or_power (str | int): Name or mana cost of the spell.

        Returns:
            Card: A new SpellCard instance.
        """

        name, data = self._get_card_data(name_or_power, self._spells)

        return SpellCard(
            name=name,
            cost=int(data["cost"]),
            rarity=str(data["rarity"]),
            effect_type=str(data["effect_type"])
        )

    def create_artifact(self, name_or_power: str | int) -> Card:
        """
        Create a new Artifact card.

        Args:
            name_or_power (str | int): Name or mana cost of the artifact.

        Returns:
            Card: A new ArtifactCard instance.
        """

        name, data = self._get_card_data(name_or_power, self._artifacts)

        return ArtifactCard(
            name=name,
            cost=int(data["cost"]),
            rarity=str(data["rarity"]),
            durability=int(data["durability"]),
            effect=str(data["effect"])
        )

    def create_themed_deck(self, size: int) -> dict[str, Any]:
        """
        Generate a complete deck of cards with uniform randomness.
        """
        import random

        pool: list[tuple[str, str]] = []
        for name in self._creatures:
            pool.append((name, "creature"))
        for name in self._spells:
            pool.append((name, "spell"))
        for name in self._artifacts:
            pool.append((name, "artifact"))

        deck: list[Card] = []

        for _ in range(size):
            name, card_type = random.choice(pool)

            if card_type == "creature":
                card = self.create_creature(name)
            elif card_type == "spell":
                card = self.create_spell(name)
            elif card_type == "artifact":
                card = self.create_artifact(name)
            else:
                raise ValueError("Invalid Card type.")

            deck.append(card)

        return {
            "deck_name": "Random Fantasy Deck",
            "cards": deck
        }

    def get_supported_types(self) -> dict[str, Any]:
        """
        Retrieve a list of card types supported by this factory.
        """

        return {
            "creatures": list(self._creatures.keys()),
            "spells": list(self._spells.keys()),
            "artifacts": list(self._artifacts.keys())
        }

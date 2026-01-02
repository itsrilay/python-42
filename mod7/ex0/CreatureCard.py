"""
This module implements the CreatureCard class, a card type for DataDeck.

It defines the behaviors specific to creature cards, including combat mechanics
and health/attack validation.
"""

from ex0.Card import Card
from typing import Any


class CreatureCard(Card):
    """
    A concrete implementation of Card representing a creature in the game.

    Creature cards have specific attack and health attributes and can
    engage in combat with other targets.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int
    ) -> None:
        """
        Initialize a new CreatureCard instance.

        Args:
            name (str): The name of the creature.
            cost (int): The mana cost to summon the creature.
            rarity (str): The rarity level of the card.
            attack (int): The attack power of the creature (must be positive).
            health (int): The health points of the creature (must be
                positive).

        Raises:
            ValueError: If attack or health are not positive integers.
        """
        super().__init__(name, cost, rarity)
        if attack <= 0 or health <= 0:
            raise ValueError("Invalid CreatureCard attributes.")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """
        Execute the action of playing the creature card.

        Args:
            game_state (dict[str, Any]): The current state of the game.

        Returns:
            dict[str, Any]: A result dictionary indicating the creature was
            summoned.
        """
        return super().play(game_state) | {
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: "CreatureCard") -> dict[str, Any]:
        """
        Perform an attack on a target creature.

        Args:
            target (CreatureCard): The creature card being attacked.

        Returns:
            dict[str, Any]: A dictionary containing details of the combat
            interaction, including damage dealt and whether the combat
            resolved.
        """
        target.health -= self.attack
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": target.health <= 0
        }

    def get_card_info(self) -> dict[str, Any]:
        """
        Retrieve the creature card's detailed information.

        Overrides the parent method to include creature-specific attributes
        like type, attack, and health.

        Returns:
            dict[str, Any]: A dictionary containing the card's name, cost,
            rarity, type, attack, and health.
        """
        return super().get_card_info() | {
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        }

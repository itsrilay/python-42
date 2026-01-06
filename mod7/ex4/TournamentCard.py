"""
This module implements the TournamentCard class for the Tournament Platform.

It combines the foundational Card behaviors, the Combatable mechanics, and the
Rankable competitive tracking into a single, versatile entity capable of
participating in tournament matches.
"""

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from typing import Any


class TournamentCard(Card, Combatable, Rankable):
    """
    A concrete implementation of a card designed for tournament play.

    This class uses multiple inheritance to combine:
    1. Card: Identity, mana cost, and rarity.
    2. Combatable: Attack, defense, and combat stats.
    3. Rankable: Wins, losses, and rating calculation.
    """

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int,
            armor: int,
            rating: int
    ) -> None:
        """
        Initialize a new TournamentCard instance.

        Args:
            name (str): The name of the card.
            cost (int): The mana cost to play the card.
            rarity (str): The rarity level of the card.
            attack (int): The attack power.
            health (int): The hit points.
            armor (int): The damage reduction value.
        """

        if attack <= 0 or health <= 0:
            raise ValueError("Invalid TournamentCard attributes.")
        super().__init__(name, cost, rarity)
        self._attack = attack
        self._health = health
        self._armor = armor
        self._wins = 0
        self._losses = 0
        self._base_rating = rating
        self._rating = rating

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """
        Execute the action of playing the tournament card.

        Args:
            game_state (dict[str, Any]): The current state of the game.

        Returns:
            dict[str, Any]: A result dictionary indicating the creature was
            summoned.
        """
        return super().play(game_state) | {
            "effect": "Creature summoned to battlefield"
        }

    def attack(self, target: Any) -> dict[str, Any]:
        """
        Perform an attack on a target entity.

        Args:
            target (Any): The entity being attacked.

        Returns:
            dict[str, Any]: A dictionary detailing the attack, including
            attacker name, target name, damage dealt, and combat type.
        """
        if hasattr(target, "defend"):
            damage_dealt = target.defend(self._attack)["damage_taken"]
        elif hasattr(target, "_health"):
            damage_dealt = min(target._health, self._attack)
            target._health -= self._attack
        else:
            return {"error": "Invalid target"}

        return {
            "attacker": self._name,
            "target": target._name,
            "damage_dealt": damage_dealt
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        """
        Process incoming damage, applying armor reduction.

        Args:
            incoming_damage (int): The raw damage amount received.

        Returns:
            dict[str, Any]: A dictionary detailing the defense, including
            actual damage taken, blocked amount, and survival status.
        """
        taken = max(incoming_damage - self._armor, 0)
        self._health -= taken
        return {
            "defender": self._name,
            "damage_taken": taken,
            "damage_blocked": self._armor,
            "still_alive": self._health > 0
        }

    def get_combat_stats(self) -> dict[str, Any]:
        """
        Retrieve the card's combat-related statistics.

        Returns:
            dict[str, Any]: A dictionary containing health, attack, and armor.
        """
        return {
            "health": self._health,
            "attack": self._attack,
            "armor": self._armor
        }

    def update_wins(self, wins: int) -> None:
        """
        Update the win count for this entity.

        Args:
            wins (int): The number of wins to set.
        """
        self._wins = wins

    def update_losses(self, losses: int) -> None:
        """
        Update the loss count for this entity.

        Args:
            losses (int): The number of losses to set.
        """
        self._losses = losses

    def get_rank_info(self) -> dict[str, Any]:
        """
        Retrieve a summary of the entity's competitive status.

        Returns:
            dict[str, Any]: A dictionary containing the current rating,
            wins, and losses.
        """
        return {
            "rating": self._rating,
            "wins": self._wins,
            "losses": self._losses
        }

    def calculate_rating(self) -> int:
        """
        Calculate and update the skill rating based on performance.

        Returns:
            int: The newly calculated rating value.
        """
        self._rating = self._base_rating + (self._wins*16 - self._losses*16)
        return self._rating

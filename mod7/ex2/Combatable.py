"""
This module defines the Combatable interface for the DataDeck game.

It establishes a contract for any entity that can engage in combat,
requiring implementation of attack, defense, and stat retrieval methods.
"""

from abc import ABC, abstractmethod
from typing import Any


class Combatable(ABC):
    """
    Abstract interface for entities capable of combat.

    This class serves as a mixin to add combat capabilities to cards
    or other game objects, enforcing standard combat behaviors.
    """

    @abstractmethod
    def attack(self, target: "Combatable") -> dict[str, Any]:
        """
        Perform an attack on a target.

        Args:
            target (Combatable): The entity being attacked.

        Returns:
            dict[str, Any]: A dictionary containing details of the attack
            interaction (e.g., damage dealt, target status).
        """
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict[str, Any]:
        """
        Process incoming damage from an attack.

        Args:
            incoming_damage (int): The amount of damage received.

        Returns:
            dict[str, Any]: A dictionary describing the defense result
            (e.g., damage taken, damage mitigated, survival status).
        """
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict[str, Any]:
        """
        Retrieve the entity's combat-related statistics.

        Returns:
            dict[str, Any]: A dictionary containing combat stats like
            attack power and health points.
        """
        pass

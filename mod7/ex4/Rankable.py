"""
Rankable Interface for the DataDeck Tournament Platform.

This module defines the Rankable interface, which adds competitive tracking
capabilities to objects. It allows entities to track wins, losses, and
calculate a competitive rating (like ELO).
"""

from abc import ABC, abstractmethod
from typing import Any


class Rankable(ABC):
    """
    Abstract interface for competitive ranking mechanics.

    Classes implementing this interface must provide storage for match
    outcomes (wins/losses) and logic to calculate a skill rating.
    """

    @abstractmethod
    def calculate_rating(self) -> int:
        """
        Calculate the current skill rating of the entity.

        Returns:
            int: The calculated rating value (e.g., an ELO score).
        """
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """
        Update the win count for this entity.

        Args:
            wins (int): The number of wins to add or set.
        """
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """
        Update the loss count for this entity.

        Args:
            losses (int): The number of losses to add or set.
        """
        pass

    @abstractmethod
    def get_rank_info(self) -> dict[str, Any]:
        """
        Retrieve a summary of the entity's competitive status.

        Returns:
            dict[str, Any]: A dictionary containing wins, losses, and
                            current rating.
        """
        pass

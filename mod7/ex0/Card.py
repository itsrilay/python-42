"""
This module defines the abstract base class for all cards in the DataDeck.

It provides the Card class, which establishes the contract for card attributes
and behaviors that all specific card types must implement.
"""

from abc import ABC, abstractmethod
from typing import Any


class Card(ABC):
    """
    Abstract base class representing a generic card in the DataDeck game.

    This class serves as the foundational blueprint for all card types,
    defining common attributes and enforcing the implementation of the
    play method in subclasses.
    """

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """
        Initialize a new Card instance.

        Args:
            name (str): The name of the card.
            cost (int): The mana cost required to play the card.
            rarity (str): The rarity level of the card.
        """
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """
        Execute the card's effect when played.

        Args:
            game_state (dict[str, Any]): The current state of the game.

        Returns:
            dict[str, Any]: A dictionary describing the result of the play.
        """
        pass

    def get_card_info(self) -> dict[str, Any]:
        """
        Retrieve the card's essential information.

        Returns:
            dict[str, Any]: A dictionary containing the card's name, cost,
            and rarity.
        """
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """
        Check if the card can be played with the available mana.

        Args:
            available_mana (int): The amount of mana available to the player.

        Returns:
            bool: True if the card's cost is less than or equal to available
            mana, False otherwise.
        """
        return self.cost <= available_mana

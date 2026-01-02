"""
Abstract Factory Interface for the DataDeck Game Engine.

This module defines the CardFactory interface, which establishes the contract
for creating families of related card objects (creatures, spells, artifacts)
and cohesive decks without specifying their concrete classes.
"""

from typing import Any
from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """
    Abstract Factory for creating game components.

    This interface enforces the implementation of creation methods for all
    card types, ensuring that any concrete factory (e.g., Fantasy, Sci-Fi)
    can produce a complete set of compatible game assets.
    """

    @abstractmethod
    def create_creature(self, name_or_power: str | int) -> Card:
        """
        Create a new Creature card.

        Args:
            name_or_power (str | int): The name of the specific creature to
                                       create, or a power level indicator.

        Returns:
            Card: A new instance of a creature card.
        """
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int) -> Card:
        """
        Create a new Spell card.

        Args:
            name_or_power (str | int): The name of the specific creature to
                                       create, or a power level indicator.

        Returns:
            Card: A new instance of a spell card.
        """
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int) -> Card:
        """
        Create a new Artifact card.

        Args:
            name_or_power (str | int): The name of the specific creature to
                                       create, or a power level indicator.

        Returns:
            Card: A new instance of an artifact card.
        """
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict[str, Any]:
        """
        Generate a complete deck of cards following a specific theme.

        Args:
            size (int): The total number of cards to include in the deck.

        Returns:
            dict[str, Any]: A dictionary containing the generated cards
                            organized by type or as a single list.
        """
        pass

    @abstractmethod
    def get_supported_types(self) -> dict[str, Any]:
        """
        Retrieve a list of card types supported by this factory.

        Returns:
            dict[str, Any]: A dictionary listing available creatures, spells,
                            and artifacts that this factory can produce.
        """
        pass

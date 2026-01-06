"""
This module implements the Deck class.

It provides a system to manage a collection of cards, including adding,
removing, shuffling, and drawing operations.
"""

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Any
from statistics import mean
import random


class Deck:
    """
    A class representing a deck of cards.

    This class manages a collection of Card objects, allowing for standard
    deck operations like shuffling, drawing, and analyzing deck composition.
    """

    def __init__(self) -> None:
        """
        Initialize an empty Deck instance.
        """
        self._cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        """
        Add a card to the deck.

        Args:
            card (Card): The card instance to add.
        """
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """
        Remove the first occurrence of a card by name.

        Args:
            card_name (str): The name of the card to remove.

        Returns:
            bool: True if the card was found and removed, False otherwise.
        """
        for card in self._cards:
            if card.get_card_info()["name"] == card_name:
                self._cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """
        Randomize the order of cards in the deck.
        """
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        """
        Draw the top card from the deck.

        Returns:
            Card: The card removed from the top of the deck.

        Raises:
            IndexError: If the deck is empty.
        """
        return self._cards.pop()

    def get_deck_stats(self) -> dict[str, Any]:
        """
        Calculate statistics about the current deck composition.

        Returns:
            dict[str, Any]: A dictionary containing counts of card types
            (creatures, spells, artifacts) and the average mana cost.
        """
        creatures = sum(isinstance(card, CreatureCard) for card in self._cards)
        spells = sum(isinstance(card, SpellCard) for card in self._cards)
        artifacts = sum(isinstance(card, ArtifactCard) for card in self._cards)
        costs = [card.get_card_info()["cost"] for card in self._cards]

        return {
            "total_cards": len(self._cards),
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": round(mean(costs), 1) if self._cards else 0.0
        }

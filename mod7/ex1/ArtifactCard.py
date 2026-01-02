"""
This module implements the ArtifactCard class, a card type for DataDeck.

It defines the behaviors of permanent items that remain on the battlefield
and have limited durability.
"""

from typing import Any
from ex0.Card import Card


class ArtifactCard(Card):
    """
    A concrete implementation of Card representing a permanent artifact.

    Artifacts remain in play, possess a specific durability, and provide
    continuous or activatable effects.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str
    ) -> None:
        """
        Initialize a new ArtifactCard instance.

        Args:
            name (str): The name of the artifact.
            cost (int): The mana cost to play the artifact.
            rarity (str): The rarity level of the card.
            durability (int): The number of times the artifact can be used
                or how long it lasts.
            effect (str): A description of the artifact's ability.
        """
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """
        Execute the action of playing the artifact card.

        Args:
            game_state (dict[str, Any]): The current state of the game.

        Returns:
            dict[str, Any]: A result dictionary including the artifact's
            effect description.
        """
        return super().play(game_state) | {"effect": self.effect}

    def activate_ability(self) -> dict[str, Any]:
        """
        Activate the artifact's ability, reducing its durability.

        Returns:
            dict[str, Any]: A dictionary reporting the remaining durability
            and the effect triggered.
        """
        self.durability -= 1
        return {
            "durability": self.durability,
            "effect": self.effect
        }

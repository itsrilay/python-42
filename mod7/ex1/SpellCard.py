"""
This module implements the SpellCard class, a concrete card type for DataDeck.

It handles immediate magic effects that are consumed upon use, defining how
spells are played and resolved against targets.
"""

from ex0.Card import Card
from typing import Any


class SpellCard(Card):
    """
    A concrete implementation of Card representing a single-use spell.

    Spell cards have an effect type (e.g., damage, heal) and are consumed
    immediately upon being played.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str
    ) -> None:
        """
        Initialize a new SpellCard instance.

        Args:
            name (str): The name of the spell.
            cost (int): The mana cost to cast the spell.
            rarity (str): The rarity level of the card.
            effect_type (str): The category of effect (e.g., 'damage', 'heal').
        """
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """
        Execute the action of playing the spell card.

        Args:
            game_state (dict[str, Any]): The current state of the game.

        Returns:
            dict[str, Any]: A result dictionary describing the spell's effect.
        """
        effect = "Unknown spell effect"
        match self.effect_type:
            case "damage":
                effect = "Deal damage to target"
            case "heal":
                effect = "Heal target"
            case "buff":
                effect = "Buff target"
            case "debuff":
                effect = "Debuff target"
            case _:
                pass

        return super().play(game_state) | {
            "effect": effect
        }

    def resolve_effect(self, targets: list[Card]) -> dict[str, Any]:
        """
        Apply the spell's effect to a list of targets.

        Args:
            targets (list[Card]): A list of Card objects targeted by the spell.

        Returns:
            dict[str, Any]: A dictionary reporting the type of effect applied
            and the names of the targets.
        """
        return {
            "effect_applied": self.effect_type,
            "applied_to": ", ".join(target.name for target in targets)
        }

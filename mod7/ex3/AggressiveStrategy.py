"""
This module implements the AggressiveStrategy class.

It defines a specific AI behavior that prioritizes dealing damage and
playing cards quickly to overwhelm opponents.
"""

from typing import Any
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class AggressiveStrategy(GameStrategy):
    """
    A concrete strategy implementation focusing on offense.

    This strategy prioritizes playing low-cost cards to maximize board presence
    and attacking the weakest targets (lowest health).
    """

    def _get_target_health(self, target: Any) -> int:
        if hasattr(target, "get_combat_stats"):
            return target.get_combat_stats()["health"]

        card_info = target.get_card_info()
        if "health" in card_info:
            return card_info["health"]

        return 9999

    def execute_turn(
        self,
        hand: list[Card],
        battlefield: list[Any]
    ) -> dict[str, Any]:
        """
        Execute a turn with aggressive logic.

        Plays as many cards as possible (cheapest first) and attacks
        available targets, prioritizing those with the lowest health.

        Args:
            hand (list[Card]): The cards currently available in the hand.
            battlefield (list[Any]): The potential targets on the board.

        Returns:
            dict[str, Any]: A summary of the turn, including cards played,
            damage dealt, and targets attacked.
        """
        hand = sorted(hand, key=lambda card: card.get_card_info()["cost"])

        targets = self.prioritize_targets(battlefield)

        played_cards: list[str] = []
        targets_attacked: list[str] = []
        mana = 10
        damage_dealt = 0

        for card in hand:
            if card.is_playable(mana):
                card.play({})
                card_info = card.get_card_info()
                played_cards.append(card_info["name"])
                mana -= card_info["cost"]

                if targets:
                    if hasattr(card, "attack_target"):
                        attack_info = card.attack_target(targets[0])
                        damage_dealt += attack_info["damage_dealt"]
                    elif hasattr(card, "attack"):
                        damage_dealt += card.attack(targets[0])["damage_dealt"]
                    else:
                        continue

                    targets_attacked.append(targets[0].get_card_info()["name"])

        return {
            "cards_played": played_cards,
            "mana_used": 10 - mana,
            "damage_dealt": damage_dealt,
            "targets_attacked": targets_attacked
        }

    def get_strategy_name(self) -> str:
        """
        Retrieve the name of this strategy.

        Returns:
            str: The string "AggressiveStrategy".
        """
        return self.__class__.__name__

    def prioritize_targets(
        self,
        available_targets: list[Any]
    ) -> list[Any]:
        """
        Sort targets to favor attacking the weakest ones first.

        Filters the list for valid targets (those with health) and sorts
        them by health in ascending order.

        Args:
            available_targets (list[Any]): The list of potential targets.

        Returns:
            list[Any]: The sorted list of valid targets.
        """
        valid_targets = [
            target for target in available_targets
            if self._get_target_health(target) < 9999
        ]

        return sorted(
            valid_targets,
            key=lambda target: self._get_target_health(target)
        )

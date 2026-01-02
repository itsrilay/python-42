from typing import Any
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from ex2.Combatable import Combatable


class AggressiveStrategy(GameStrategy):
    def execute_turn(
        self,
        hand: list[Card],
        battlefield: list[Card]
    ) -> dict[str, Any]:
        hand = sorted(hand, key=lambda card: card.cost)

        played_cards: list[Card] = []
        mana = 10
        for card in hand:
            if card.is_playable(mana):
                card.play({})
                played_cards.append(card)
                mana -= card.cost


    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(
        self,
        available_targets: list[Combatable]
    ) -> list[Combatable]:
        return sorted(
            available_targets,
            key=lambda target: target.get_combat_stats()["health"]
        )
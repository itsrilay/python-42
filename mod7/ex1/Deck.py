from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Any
from statistics import mean
import random


class Deck:
    def __init__(self) -> None:
        self._cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self._cards:
            if card.get_card_info()["name"] == card_name:
                self._cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        return self._cards.pop()

    def get_deck_stats(self) -> dict[str, Any]:
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

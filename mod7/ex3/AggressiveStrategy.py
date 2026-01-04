from typing import Any
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class AggressiveStrategy(GameStrategy):
    def execute_turn(
        self,
        hand: list[Card],
        battlefield: list[Any]
    ) -> dict[str, Any]:
        hand = sorted(hand, key=lambda card: card.cost)

        targets = self.prioritize_targets(battlefield)

        played_cards: list[str] = []
        targets_attacked: list[str] = []
        mana = 10
        damage_dealt = 0
        for card in hand:
            if card.is_playable(mana):
                card.play({})
                played_cards.append(card.name)
                mana -= card.cost

                if targets:
                    if hasattr(card, "attack"):
                        damage_dealt += card.attack(targets[0])["damage_dealt"]
                    elif hasattr(card, "attack_target"):
                        attack_info = card.attack_target(targets[0])
                        damage_dealt += attack_info["damage_dealt"]
                    else:
                        continue

                    target_name = getattr(targets[0], "name", "Unknown")
                    targets_attacked.append(target_name)

        return {
            "cards_played": played_cards,
            "mana_used": 10 - mana,
            "damage_dealt": damage_dealt,
            "targets_attacked": targets_attacked
        }

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(
        self,
        available_targets: list[Any]
    ) -> list[Any]:

        valid_targets: list[Card] = [
            target for target in available_targets
            if hasattr(target, "health")
        ]

        return sorted(
            valid_targets,
            key=lambda target: target.health
        )

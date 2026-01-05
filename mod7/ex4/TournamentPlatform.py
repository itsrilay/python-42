from ex4.TournamentCard import TournamentCard
from typing import Any


class TournamentPlatform:
    def __init__(self):
        self._registry: dict[str, TournamentCard] = {}
        self._counts: dict[str, int] = {}

    def register_card(self, card: TournamentCard) -> str:
        name = card.get_card_info()["name"]

        id = None

        split_name = name.split()
        gen_name = split_name[len(split_name) - 1].lower()
        if gen_name not in self._counts:
            self._counts[gen_name] = 1
        id = f"{gen_name}_{self._counts[gen_name]:03d}"

        self._counts[gen_name] += 1
        self._registry[id] = card

        return id

    def create_match(self, card1_id: str, card2_id: str) -> dict[str, Any]:
        card1 = self._registry.get(card1_id)
        card2 = self._registry.get(card2_id)

        if not card1 or not card2:
            raise ValueError("Couldn't find card ID.")

        while True:
            card1.attack(card2)

            if card2.get_combat_stats()["health"] <= 0:


    def get_leaderboard(self) -> list:
        pass

    def generate_tournament_report(self) -> dict:
        pass

"""
This module implements the TournamentPlatform class.

The platform acts as the central manager for the tournament system, handling
card registration, matchmaking, leaderboard generation, and reporting.
"""

from ex4.TournamentCard import TournamentCard
from typing import Any


class TournamentPlatform:
    """
    Manages the tournament environment, including card registration and
    matchmaking.

    This class maintains a registry of participating cards, tracks their
    performance statistics, and facilitates combat matches between them.
    """

    def __init__(self):
        """
        Initialize a new TournamentPlatform instance.

        Sets up the card registry, the name counter for ID generation,
        and the match counter.
        """
        self._registry: dict[str, TournamentCard] = {}
        self._counts: dict[str, int] = {}
        self._matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        """
        Register a new card in the tournament system.

        Generates a unique ID for the card based on its name
        and stores it in the registry.

        Args:
            card (TournamentCard): The card instance to register.

        Returns:
            str: The unique identifier assigned to the registered card.
        """
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
        """
        Conduct a match between two registered cards.

        Retrieves cards by their IDs and initiates a turn-based combat loop
        until one card is defeated. Updates the wins, losses, and ratings
        for both participants.

        Args:
            card1_id (str): The ID of the first competitor.
            card2_id (str): The ID of the second competitor.

        Returns:
            dict[str, Any]: A dictionary containing the match results,
            including the winner's ID, loser's ID, and their new ratings.

        Raises:
            ValueError: If either card ID cannot be found in the registry.
        """
        card1 = self._registry.get(card1_id)
        card2 = self._registry.get(card2_id)

        if not card1 or not card2:
            raise ValueError("Couldn't find card ID.")

        curr, prev = card1, card2
        curr_id, prev_id = card1_id, card2_id
        while True:
            curr.attack(prev)

            if prev.get_combat_stats()["health"] <= 0:
                curr.update_wins(curr.get_rank_info()["wins"] + 1)
                prev.update_losses(prev.get_rank_info()["losses"] + 1)
                self._matches_played += 1
                break

            curr, prev = prev, curr
            curr_id, prev_id = prev_id, curr_id

        return {
            "winner": curr_id,
            "loser": prev_id,
            "winner_rating": curr.calculate_rating(),
            "loser_rating": prev.calculate_rating()
        }

    def get_leaderboard(self) -> list[TournamentCard]:
        """
        Retrieve the current tournament leaderboard.

        Updates the ratings for all cards and returns a list of card objects
        sorted by their rating in descending order.

        Returns:
            list[TournamentCard]: The sorted list of registered cards.
        """
        card_list = [card for _, card in self._registry.items()]

        return sorted(
            card_list,
            key=lambda card: card.get_rank_info()["rating"],
            reverse=True
        )

    def generate_tournament_report(self) -> dict[str, Any]:
        """
        Generate a status report for the tournament platform.

        Returns:
            dict[str, Any]: A summary dictionary containing the total number
            of cards, matches played, average rating, and platform status.
        """
        ratings = [
            card.get_rank_info()["rating"]
            for _, card in self._registry.items()
        ]

        avg_rating = round(sum(ratings) / len(ratings)) if ratings else 0

        return {
            "total_cards": len(self._registry),
            "matches_played": self._matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }

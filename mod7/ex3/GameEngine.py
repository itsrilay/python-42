"""
This module implements the GameEngine class.

The GameEngine acts as the central coordinator that orchestrates
the interaction between the CardFactory and the GameStrategy.
"""

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from typing import Any


class GameEngine:
    """
    The main engine class responsible for running the game simulation.

    It maintains the game state, manages the turn lifecycle, and tracks
    aggregate statistics like total damage and cards created.
    """

    def __init__(self) -> None:
        """
        Initialize a new GameEngine instance with default counters.
        """
        self._turns = 0
        self._factory: CardFactory | None = None
        self._strategy: GameStrategy | None = None
        self._total_damage = 0
        self._total_cards = 0

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy
    ) -> None:
        """
        Inject the dependencies required to run the engine.

        Args:
            factory (CardFactory): The factory used to generate game assets.
            strategy (GameStrategy): The AI logic used to play the turns.
        """
        self._factory = factory
        self._strategy = strategy

    def simulate_turn(self) -> dict[str, Any]:
        """
        Execute a single turn of the game simulation.

        This method generates a hand of cards using the factory, sets up a
        mock battlefield, and delegates the gameplay decisions to the
        active strategy.

        Returns:
            dict[str, Any]: A summary of the turn's outcome.

        Raises:
            ValueError: If the engine has not been properly configured with
                        a factory and strategy.
        """
        if isinstance(self._factory, CardFactory):
            deck_data = self._factory.create_themed_deck(2)
            hand: list[Card] = deck_data["cards"]

            hand_format = [
                f"{card.name} ({card.cost})"
                for card in hand
            ]
            print(f"Hand: {hand_format}")

            battlefield = [
                self._factory.create_creature("Goblin Warrior")
            ]
            self._total_cards += 3

            if isinstance(self._strategy, GameStrategy):
                result = self._strategy.execute_turn(hand, battlefield)
                self._turns += 1
                self._total_damage += result["damage_dealt"]

                return result
            else:
                raise ValueError("Invalid strategy")
        else:
            raise ValueError("Invalid factory")

    def get_engine_status(self) -> dict[str, Any]:
        """
        Retrieve the current status of the game engine.

        Returns:
            dict[str, Any]: A report containing the number of turns simulated,
                            the strategy name, total damage dealt, and total
                            cards created.
        """
        return {
            "turns_simulated": self._turns,
            "strategy_used": type(self._strategy).__name__,
            "total_damage": self._total_damage,
            "cards_created": self._total_cards
        }

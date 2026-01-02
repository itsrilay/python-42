"""
Strategy Interface for the DataDeck Game Engine.

This module defines the GameStrategy interface, which encapsulates the
logic for AI decision-making. Different concrete strategies (e.g., Aggressive,
Defensive) can be swapped at runtime to change how the game is played.
"""

from typing import Any
from abc import ABC, abstractmethod
from ex0.Card import Card
from ex2.Combatable import Combatable


class GameStrategy(ABC):
    """
    Abstract base class for game playing strategies.

    This interface defines the essential behaviors required for an AI agent
    to interact with the game, including turn execution and target selection.
    """

    @abstractmethod
    def execute_turn(
        self,
        hand: list[Card],
        battlefield: list[Card]
    ) -> dict[str, Any]:
        """
        Execute a full game turn based on the specific strategy logic.

        Args:
            hand (list[Card]): The cards currently available in the
                               player's hand.
            battlefield (list[Card]): The cards currently active on the board.

        Returns:
            dict[str, Any]: A summary of actions taken during the turn, such as
                            cards played and damage dealt.
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """
        Retrieve the display name of this strategy.

        Returns:
            str: The human-readable name of the strategy (e.g., "Aggressive").
        """
        pass

    @abstractmethod
    def prioritize_targets(
        self,
        available_targets: list[Combatable]
    ) -> list[Combatable]:
        """
        Sort a list of potential targets according to strategic priority.

        Args:
            available_targets (list[Combatable]): A list of entities that
                                                  can be attacked.

        Returns:
            list[Combatable]: The same list sorted by priority
                              (highest priority first).
        """
        pass

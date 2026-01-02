"""
This module defines the Magical interface for the DataDeck game.

It establishes a contract for entities that can cast spells and manipulate
mana, ensuring consistent magic system behaviors.
"""

from abc import ABC, abstractmethod
from typing import Any
from ex2.Combatable import Combatable


class Magical(ABC):
    """
    Abstract interface for entities capable of using magic.

    This class serves as a mixin to add spellcasting and mana management
    capabilities to cards, enforcing standard magical behaviors.
    """

    @abstractmethod
    def cast_spell(
        self,
        spell_name: str,
        targets: list[Combatable]
    ) -> dict[str, Any]:
        """
        Cast a specific spell on a list of targets.

        Args:
            spell_name (str): The name of the spell to cast.
            targets (list[Combatable]): list of entities targeted by the spell.

        Returns:
            dict[str, Any]: A dictionary detailing the spell's effect,
            targets involved, and the outcome.
        """
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict[str, Any]:
        """
        Generate or channel mana for magical effects.

        Args:
            amount (int): The amount of mana to channel.

        Returns:
            dict[str, Any]: A dictionary reporting the mana generation
            process and current mana state.
        """
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict[str, Any]:
        """
        Retrieve the entity's magic-related statistics.

        Returns:
            dict[str, Any]: A dictionary containing magic stats (e.g.,
            spell power, current mana).
        """
        pass

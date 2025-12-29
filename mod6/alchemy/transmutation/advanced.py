"""Module for advanced transmutations using relative imports."""

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """Synthesize a result from local and parent-level module functions."""
    res_gold = lead_to_gold()
    res_heal = healing_potion()
    return f"Philosopher's stone created using {res_gold} and {res_heal}"


def elixir_of_life() -> str:
    """Return a static string representing the elixir of life."""
    return "Elixir of life: eternal youth achieved!"

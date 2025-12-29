"""Module for performing base level transmutations."""

from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """Combine lead and fire strings to represent a transmutation result."""
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    """Combine stone and earth strings to represent a transmutation result."""
    return f"Stone transmuted to gem using {create_earth()}"

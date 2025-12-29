"""Module for synthesizing compound strings from elemental module functions."""

from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    """Combines fire and water string outputs into a formatted result."""
    fire_result = create_fire()
    water_result = create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion() -> str:
    """Combines earth and fire string outputs into a formatted result."""
    earth_result = create_earth()
    fire_result = create_fire()
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion() -> str:
    """Combines air and water string outputs into a formatted result."""
    air_result = create_air()
    water_result = create_water()
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion() -> str:
    """Aggregates all four elemental string outputs into a single result."""
    f = create_fire()
    wa = create_water()
    e = create_earth()
    a = create_air()
    return f"Wisdom potion brewed with all elements: {f}, {wa}, {e}, {a}"

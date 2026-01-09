"""
Exercise 1: Higher Realm

This module demonstrates higher-order functions: functions that accept other
functions as arguments or return them. It includes utilities for combining,
amplifying, and conditionally executing magical spells.
"""

from typing import Callable, Any


def spell_combiner(
    spell1: Callable[..., Any],
    spell2: Callable[..., Any]
) -> Callable[..., Any]:
    """
    Creates a new function that executes two spells simultaneously.

    Args:
        spell1: The first spell function to execute.
        spell2: The second spell function to execute.

    Returns:
        A new function that calls both spells with the same arguments and
        returns a tuple of their results.
    """
    def wrapper(*args: Any, **kwargs: Any):
        res_1 = spell1(*args, **kwargs)
        res_2 = spell2(*args, **kwargs)

        return (res_1, res_2)

    return wrapper


def power_amplifier(
    base_spell: Callable[..., Any],
    multiplier: int
) -> Callable[..., Any]:
    """
    Creates a new function that amplifies the numeric result of a base spell.

    Args:
        base_spell: A spell function that returns a number.
        multiplier: The factor by which to multiply the spell's result.

    Returns:
        A new function that returns the base spell's result multiplied by
        the multiplier.
    """
    def wrapper(*args: Any, **kwargs: Any):
        return base_spell(*args, **kwargs) * multiplier

    return wrapper


def conditional_caster(
    condition: Callable[..., Any],
    spell: Callable[..., Any]
) -> Callable[..., Any]:
    """
    Creates a function that only casts a spell if a condition is met.

    Args:
        condition: A function returning a boolean to check before casting.
        spell: The spell function to execute if the condition is True.

    Returns:
        A new function that returns the spell's result if the condition is
        met, or "Spell fizzled" otherwise.
    """
    def wrapper(*args: Any, **kwargs: Any):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"

    return wrapper


def spell_sequence(spells: list[Callable[..., Any]]) -> Callable[..., Any]:
    """
    Creates a function that executes a list of spells in order.

    Args:
        spells: A list of spell functions to execute.

    Returns:
        A new function that returns a list containing the results of all
        spells executed with the same arguments.
    """
    def wrapper(*args: Any, **kwargs: Any):
        results: list[Any] = []

        for spell in spells:
            results.append(spell(*args, **kwargs))

        return results

    return wrapper


def main() -> None:
    """Executes test scenarios for Exercise 1: Higher Realm."""
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def damage(power: int) -> int:
        return power

    def is_dragon(target: str) -> bool:
        return target == "Dragon"

    print("\nTesting spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    print(f"Combined spell result: {', '.join(combined_spell('Dragon'))}")

    print("\nTesting power amplifier...")
    power = 10
    amplified_spell = power_amplifier(damage, 3)
    print(f"Original: {power}, Amplified: {amplified_spell(power)}")

    print("\nTesting conditional caster...")
    action = conditional_caster(is_dragon, fireball)
    print(f"Casting on valid target: {action('Dragon')}")
    print(f"Casting on invalid target: {action('Peasant')}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([heal, heal, fireball])
    print(f"Casting spells sequentially: {', '.join(sequence('Peasant'))}")


if __name__ == "__main__":
    main()

"""
Exercise 3: Ancient Library

This module explores the powerful tools within the `functools` module.
It demonstrates high-level functional programming concepts including
reduction, partial application, memoization, and single-dispatch
generic functions.
"""

from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    Combines a list of spell power levels into a single value using a
    specified operation.

    Args:
        spells: A list of integer power levels.
        operation: The name of the operation ('add', 'multiply', 'max', 'min').

    Returns:
        The result of reducing the list using the specified operation.
    """
    operations: dict[str, Callable[..., Any]] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }
    return reduce(operations[operation], spells)


def partial_enchanter(
        base_enchantment: Callable[[int, str, str], Any]
) -> dict[str, Callable[..., Any]]:
    """
    Creates specialized enchantment functions by freezing arguments of a
    base enchantment function.

    Args:
        base_enchantment: A function taking (power, element, target).

    Returns:
        A dictionary containing three specialized functions:
        - 'fire_enchant': Fixed power=50, element='fire'.
        - 'ice_enchant': Fixed power=50, element='ice'.
        - 'lightning_enchant': Fixed power=50, element='lightning'.
    """
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning")
    }


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    """
    Calculates the nth Fibonacci number efficiently using memoization.

    Uses an LRU (Least Recently Used) cache to store results of previous
    computations, changing the complexity from exponential to linear.

    Args:
        n: The index of the Fibonacci sequence to calculate.

    Returns:
        The nth Fibonacci number.
    """
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], Any]:
    """
    Creates a single-dispatch generic function for casting spells.

    The returned function behaves differently based on the input type:
    - int: Deals damage.
    - str: Casts an enchantment.
    - list: Casts multiple spells.
    - other: Returns an unknown spell message.

    Returns:
        The 'cast_spell' function which is decorated with @singledispatch.
    """
    @singledispatch
    def cast_spell(arg: Any) -> str:
        return f"Unknown spell type: {arg}"

    @cast_spell.register(int)
    def _(arg: int) -> str:  # _ for namespace hygiene
        return f"Deals {arg} damage"

    @cast_spell.register(str)
    def _(arg: str) -> str:
        return f"Enchants with {arg}"

    @cast_spell.register(list)
    def _(arg: list[Any]) -> str:
        return f"Casting {len(arg)} spells"

    return cast_spell


def main() -> None:
    """Executes test scenarios for Exercise 3: Ancient Library."""
    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return (
            f"{element.capitalize()} Enchantment: Power {power}, "
            f"Element {element}, Target {target}"
        )

    partials = partial_enchanter(base_enchantment)
    print(partials["fire_enchant"]("Sword"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()

    print(cast(100))
    print(cast("Invisibility"))
    print(cast(["Fireball", "Frostbolt"]))
    print(cast(None))


if __name__ == "__main__":
    main()

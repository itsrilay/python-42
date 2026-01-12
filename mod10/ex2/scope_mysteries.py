"""
Exercise 2: Memory Depths

This module explores lexical scoping and closures. It demonstrates how inner
functions can capture and manipulate variables from their enclosing scope,
creating persistent state without global variables.
"""

from typing import Callable, Any


def mage_counter() -> Callable[[], int]:
    """
    Creates a closure that counts how many times it has been called.

    Returns:
        A function that returns the current count (increments on each call).
    """
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """
    Creates a closure that accumulates power over time.

    Args:
        initial_power: The starting power level.

    Returns:
        A function that accepts a power value to add, updates the total,
        and returns the new accumulated power.
    """
    total_power = initial_power

    def accumulator(given_power: int) -> int:
        nonlocal total_power
        total_power += given_power
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """
    Creates a factory for generating specific enchantment descriptions.

    Args:
        enchantment_type: The type of enchantment (e.g., "Flaming").

    Returns:
        A function that takes an item name and returns the full
        enchanted string (e.g., "Flaming Sword").
    """
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable[..., Any]]:
    """
    Creates a secure memory storage system using closures.

    Returns:
        A dictionary containing two functions:
        - 'store(key, value)': Saves a value to the private vault.
        - 'recall(key)': Retrieves a value from the private vault.
    """
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        memory = vault.get(key, "Memory not found")
        return memory

    return {"store": store, "recall": recall}


def main() -> None:
    """Executes test scenarios for Exercise 2: Memory Depths."""
    print("\nTesting mage counter...")
    counter = mage_counter()
    for i in range(3):
        print(f"Call {i + 1}: {counter()}")

    print("\nTesting spell accumulator...")
    initial_power = 10
    additional_power = 20
    print(f"Initial power: {initial_power}")
    accumulator = spell_accumulator(initial_power)
    print(f"Accumulating {additional_power} power...")
    print(f"Total power: {accumulator(additional_power)}")

    print("\nTesting enchantment factory...")
    enchantments = {
        "Flaming": "Sword",
        "Frozen": "Shield"
    }
    for enchantment, item in enchantments.items():
        enchanter = enchantment_factory(enchantment)
        print(enchanter(item))

    print("\nTesting memory vault...")
    vault_functions = memory_vault()
    total_power = accumulator(0)
    power_key = "power"
    print("Storing total power...")
    vault_functions["store"](power_key, total_power)
    print("Recalling stored memory...")
    print(f"Power: {vault_functions['recall'](power_key)}")
    print("Recalling missing memory...")
    print(vault_functions['recall']('nice'))


if __name__ == "__main__":
    main()

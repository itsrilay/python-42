"""
Main execution script for Exercise 2: The Ability System.

This script demonstrates the use of Multiple Inheritance and Interfaces
(Mixins) by instantiating an EliteCard and exercising its combined
Combatable and Magical capabilities.
"""

from ex2.EliteCard import EliteCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card


def print_capabilities(cls: type, interface_class: type) -> None:
    """
    Print the methods of a class that belong to a specific interface.

    Uses introspection to find methods in the 'cls' that are also defined
    in the 'interface_class'.

    Args:
        cls (type): The class to inspect (e.g., EliteCard).
        interface_class (type): The interface to filter by (e.g., Combatable).
    """
    interface_methods = dir(interface_class)

    methods = [
        m for m in dir(cls)
        if m in interface_methods and not m.startswith("_")
    ]

    print(f"- {interface_class.__name__}: {methods}")


def main() -> None:
    """
    Execute the test scenario for the Ability System.

    Verifies that EliteCard correctly inherits methods from all three
    parent classes (Card, Combatable, Magical) and demonstrates a
    mock game scenario involving combat and spellcasting.
    """
    print("\n=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    classes: list[type] = [Card, Combatable, Magical]
    for class_name in classes:
        print_capabilities(EliteCard, class_name)

    print("\nPlaying Arcane Warrior (Elite Card):")
    warrior = EliteCard("Arcane Warrior", 5, "Epic", 5, 5, 8, 3, "melee")

    enemy = EliteCard("Enemy", 4, "Epic", 5, 3, 1, 2, "melee")
    enemy1 = EliteCard("Enemy1", 4, "Epic", 5, 3, 1, 2, "melee")
    enemy2 = EliteCard("Enemy2", 4, "Epic", 5, 3, 1, 2, "melee")

    print("\nCombat phase:")
    print(f"Attack result: {warrior.attack(enemy)}")
    print(f"Defense result: {warrior.defend(5)}")

    print("\nMagic phase:")
    print(f"Spell cast: {warrior.cast_spell('Fireball', [enemy1, enemy2])}")
    print(f"Mana channel: {warrior.channel_mana(3)}")


if __name__ == "__main__":
    main()

"""
Main execution script for Exercise 0: Card Foundation.

This script demonstrates the functionality of the abstract Card class
and its concrete implementation, CreatureCard.
"""

from ex0.CreatureCard import CreatureCard


def main() -> None:
    """
    Execute the test scenario for the Card Foundation.

    Instantiates a CreatureCard, displays its information, tests
    playability with different mana levels, and performs a mock combat
    interaction.
    """
    print("\n=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:")
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("\nCreatureCard Info:")
    print(dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    print(f"Play result: {dragon.play({})}")

    print("\nFire Dragon attacks Goblin Warrior")
    goblin = CreatureCard("Goblin Warrior", 2, "Common", 1, 2)
    print(f"Attack result: {dragon.attack_target(goblin)}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()

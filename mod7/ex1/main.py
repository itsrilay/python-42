"""
Main execution script for Exercise 1: Deck Builder.

This script demonstrates polymorphism by managing a Deck containing
different card types (Creature, Spell, Artifact) and processing them
through a unified interface.
"""

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


def main() -> None:
    """
    Execute the test scenario for the Deck Builder.

    Creates a Deck, populates it with various card types, prints deck
    statistics, and simulates drawing and playing cards to demonstrate
    polymorphic behavior.
    """
    print("\n=== DataDeck Deck Builder ===")

    print("\nBuilding deck with different card types...")
    cards: list[Card] = [
        CreatureCard("Fire Dragon", 5, "Legendary", 7, 5),
        ArtifactCard(
            "Mana Crystal",
            2,
            "Epic",
            999999,
            "Permanent: +1 mana per turn"
        ),
        SpellCard("Lightning Bolt", 3, "Rare", "damage")
    ]
    deck = Deck()
    for card in cards:
        deck.add_card(card)
    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:\n")
    while len(deck.cards) > 0:
        card = deck.draw_card()
        print(f"Drew: {card.name} ({type(card).__name__.replace('Card', '')})")
        print(f"Play result: {card.play({})}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()

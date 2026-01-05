"""
Main entry point for Exercise 3: Game Engine.

This script demonstrates the integration of the Abstract Factory and Strategy
design patterns by configuring a GameEngine, generating cards, and simulating
a turn using aggressive AI logic.
"""

from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
import sys


def main() -> None:
    """
    Orchestrate the Game Engine demonstration.
    """
    print("\n=== DataDeck Game Engine ===")

    print("\nConfiguring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print(f"Factory: {type(factory).__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")

    available_types = factory.get_supported_types()
    print(f"Available types: {available_types}")

    print("\nSimulating aggressive turn...")

    try:
        turn_result = engine.simulate_turn()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit()

    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {turn_result}")

    print("\nGame Report:")
    report = engine.get_engine_status()
    print(report)

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main() -> None:
    """
    Orchestrates the achievement tracking and displaying.
    """
    print("=== Achievement Tracker System ===\n")

    alice = {
        'first_kill',
        'first_kill',
        'level_10',
        'treasure_hunter',
        'speed_demon'
    }

    bob = {
        'first_kill',
        'level_10',
        'boss_slayer',
        'collector'
    }

    charlie = {
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist'
    }

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    all_achievements = alice.union(bob, charlie)

    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    common_achievements = alice.intersection(bob, charlie)

    print(f"Common to all players: {common_achievements}")

    alice_unique = alice.difference(bob, charlie)
    bob_unique = bob.difference(alice, charlie)
    charlie_unique = charlie.difference(bob, alice)

    rare_achievements = alice_unique.union(bob_unique, charlie_unique)

    print(f"Rare achievements (1 player): {rare_achievements}")

    common_alice_bob = alice.intersection(bob)

    print(f"\nAlice vs Bob common: {common_alice_bob}")

    new_alice_unique = alice.difference(bob)
    new_bob_unique = bob.difference(alice)

    print(f"Alice unique: {new_alice_unique}")
    print(f"Bob unique: {new_bob_unique}")


if __name__ == "__main__":
    main()

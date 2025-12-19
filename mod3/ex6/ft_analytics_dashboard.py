#!/usr/bin/env python3

def main() -> None:
    """
    Calculates and displays all analytics related to the game.
    """
    print("=== Game Analytics Dashboard ===")

    players = [
        ("bob", 1800),
        ("alice", 2300),
        ("diana", 2050),
        ("charlie", 2150)
    ]
    activity = [
        ("bob", True),
        ("alice", True),
        ("diana", False),
        ("charlie", True)
    ]
    all_achievements = [
        "first_kill",
        "boss_slayer",
        "first_kill",
        "dungeon_clearer",
        "world_ender",
        "level_10"
    ]

    print("\n=== List Comprehension Examples ===")

    high_scores = [name for name, score in players if score > 2000]
    scores_doubled = [score*2 for _, score in players]
    active_players = [name for name, active in activity if active]

    print(f"High scorers (>2000): {sorted(high_scores)}")
    print(f"Scores doubled: {sorted(scores_doubled)}")
    print(f"Active players: {sorted(active_players)}")

    print("\n=== Dict Comprehension Examples ===")

    scoreboard = {player: score for player, score in players}
    score_categories = {player: ('high' if score > 2000 else 'standard')
                        for player, score in players}

    print(f"Player scores: {scoreboard}")
    print(f"Score categories: {score_categories}")

    print("\n=== Set Comprehension Examples ===")

    unique_achievements = {achievement for achievement in all_achievements}

    print(f"Unique achievements: {unique_achievements}")

    print("\n=== Combined Analysis ===")

    total_players = len(players)
    total_score = sum([score for _, score in players])
    max_score = max([score for _, score in players])
    avg_score = total_score / total_players
    top_scorer = [f"{name} ({score} points)"
                  for name, score in players if score == max_score]

    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {avg_score}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print(f"Top scorer: {top_scorer[0]}")


if __name__ == "__main__":
    main()

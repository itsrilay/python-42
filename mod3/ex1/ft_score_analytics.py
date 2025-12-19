#!/usr/bin/env python3

import sys


def main() -> None:
    """
    Processes scores and displays them.
    """
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    arg = None
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Error: {arg} is not a valid score.")
    if not scores:
        print(
            "No scores provided.",
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()

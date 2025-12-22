#!/usr/bin/env python3

import sys


def main() -> None:
    """
    Reads user input from standard input.
    Routes user input to messages to standard output.
    Displays error message on standard error.
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    archivist_id = input("\nInput Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    print(
        f"\n[STANDARD] Archive status from {archivist_id}: {status}",
        file=sys.stdout
    )
    print(
        "[ALERT] System diagnostic: Communication channels verified",
        file=sys.stderr
    )
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print("\nThree-channel communication test successful.", file=sys.stdout)


if __name__ == "__main__":
    main()

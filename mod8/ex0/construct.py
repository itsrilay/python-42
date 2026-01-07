import sys
import os
import site

"""
Mission: Enter the Matrix (Exercise 0)

This script detects the current Python environment and guides the user
on how to set up a virtual environment (The Construct) if they are
currently in the global system.
"""


def main() -> None:
    """
    Main entry point for the Construct program.

    Checks sys.prefix against sys.base_prefix to determine the environment
    status, prints the appropriate Matrix-themed messages, and displays
    package paths.
    """
    print("\nMATRIX STATUS: ", end="")
    virtual = sys.prefix != sys.base_prefix

    if virtual:
        print("Welcome to the construct")
    else:
        print("You're still plugged in")

    print(f"\nCurrent Python: {sys.executable}")

    if virtual:
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        print("\nPackage installation path:")
        try:
            print(site.getsitepackages()[0])
        except IndexError:
            print("Couldn't get path.")
    else:
        print("Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate    # On Windows")

        print("\nThen run this program again.")


if __name__ == "__main__":
    main()

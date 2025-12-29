#!/usr/bin/env python3

"""Demonstrates Python package initialization and attribute visibility."""

import alchemy.elements
import alchemy


def test_direct_access() -> None:
    """Tests direct access to the elements module."""
    print(
        "alchemy.elements.create_fire():",
        alchemy.elements.create_fire()
    )
    print(
        "alchemy.elements.create_water():",
        alchemy.elements.create_water()
    )
    print(
        "alchemy.elements.create_earth():",
        alchemy.elements.create_earth()
    )
    print(
        "alchemy.elements.create_air():",
        alchemy.elements.create_air()
    )


def test_package_access() -> None:
    """Tests visibility control via __init__.py."""
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")

    try:
        alchemy.create_earth()
    except AttributeError as e:
        print(f"alchemy.create_earth(): {type(e).__name__} - not exposed")

    try:
        alchemy.create_air()
    except AttributeError as e:
        print(f"alchemy.create_air(): {type(e).__name__} - not exposed")


if __name__ == "__main__":
    print("\n=== Sacred Scroll Mastery ===")

    print("\nTesting direct module access:")
    test_direct_access()

    print("\nTesting package-level access (controlled by __init__.py):")
    test_package_access()

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")

#!/usr/bin/env python3

class SecurePlant:
    """
    Acts as a blueprint for SecurePlant objects

    Protects data by validating before changing it with setters.
    Encapsulates it by adding _ prefix to variables
    Getters return value instead of accessing directly
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Creates SecurePlant objects

        Encapsulates variables
        """
        self._name = name
        self._height = height
        self._age = age

    def get_height(self) -> int:
        """
        Returns plant's height
        """
        return self._height

    def get_age(self) -> int:
        """
        Returns plant's age
        """
        return self._age

    def set_height(self, height: int) -> None:
        """
        Sets plant's height

        Checks if height is valid (>= 0)
        """
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        """
        Sets plant's age

        Checks if age is valid (>= 0)
        """
        if (age < 0):
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age


def main() -> None:
    """
    Orchestrates the display and testing of SecurePlant
    """
    print("=== Garden Security System ===")
    plt = SecurePlant("Rose", 10, 20)
    print("Plant created: Rose")
    plt.set_height(25)
    print(f"Height updated: {plt.get_height()}cm [OK]")
    plt.set_age(30)
    print(f"Age updated: {plt.get_age()} days [OK]\n")
    plt.set_height(-5)
    print()
    print(f"Current plant: Rose ({plt.get_height()}cm, {plt.get_age()} days)")


if __name__ == "__main__":
    main()

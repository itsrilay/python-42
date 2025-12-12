#!/usr/bin/env python3

class Plant:
    """
    Acts as a blueprint for Plant objects.
    """
    def __init__(self, name: str, height: int, lifetime: int) -> None:
        """
        Constructs a Plant object.
        """
        self.name = name
        self.height = height
        self.lifetime = lifetime

    def grow(self) -> None:
        """
        Increases the plant's height by 1 unit.
        """
        self.height += 1

    def age(self) -> None:
        """
        Increases the plant's lifetime by 1 day.
        """
        self.lifetime += 1

    def get_info(self) -> None:
        """
        Displays the current status of the plant (name, height, age).
        """
        print(f"{self.name}: {self.height}cm, {self.lifetime} days old")


def plant_generator(plants: list[tuple[str, int, int]]):
    """
    Yields Plant objects from a list of tuples
    """
    for plant in plants:
        yield Plant(plant[0], plant[1], plant[2])


def main() -> None:
    """
    Orchestrates the generation of plant objects and printing
    """
    plants = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    total = 0
    print("=== Plant Factory Output ===")
    for plt in plant_generator(plants):
        print(f"Created: {plt.name} ({plt.height}cm, {plt.lifetime} days)")
        total += 1
    print(f"\nTotal plants created: {total}")


if __name__ == "__main__":
    main()

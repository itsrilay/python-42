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

    def get_info(self) -> str:
        """
        Displays the current status of the plant (name, height, age).
        """
        return f"{self.name}: {self.height}cm, {self.lifetime} days old"


def main() -> None:
    """
    Orchestrates the plant growth simulation.

    Initializes plants, runs the simulation and prints reports.
    """
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    init_heights = [plant.height for plant in plants]
    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())
    day = 1
    while day < 7:
        for plant in plants:
            plant.grow()
            plant.age()
        day += 1
    print("=== Day 7 ===")
    i = 0
    for plant in plants:
        growth = plant.height - init_heights[i]
        print(plant.get_info())
        print(f"Growth this week: +{growth}cm")
        i += 1


if __name__ == "__main__":
    main()

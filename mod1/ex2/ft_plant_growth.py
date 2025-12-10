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


def simulate_plants(plants: list[Plant]) -> None:
    """
    Simulates growth for a list of plants over a period of days.

    Each day, every plant grows and ages.
    """
    day = 1
    while day < 7:
        for plant in plants:
            plant.grow()
            plant.age()
        day += 1


def init_week(plants: list[Plant]) -> None:
    """
    Displays the initial status of all plants on Day 1.
    """
    print("=== Day 1 ===")
    for plant in plants:
        plant.get_info()


def end_week(plants: list[Plant], init_heights: list[int]) -> None:
    """
    Displays the final status on Day 7 and calculates weekly growth.

    Args:
        plants: The list of Plant objects after simulation.
        init_heights: A list of integers representing starting heights.
    """
    print("=== Day 7 ===")
    i = 0
    for plant in plants:
        growth = plant.height - init_heights[i]
        plant.get_info()
        print(f"Growth this week: +{growth}cm")
        i += 1


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
    init_week(plants)
    simulate_plants(plants)
    end_week(plants, init_heights)


if __name__ == "__main__":
    main()

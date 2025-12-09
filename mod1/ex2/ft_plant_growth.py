#!/usr/bin/env python3

class Plant:
    """
    This class acts as a blueprint for Plant objects.

    It builds those objects through the __init__ method.

    """
    def __init__(self, name: str, height: int, lifetime: int) -> None:
        self.name = name
        self.height = height
        self.lifetime = lifetime

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.lifetime += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.lifetime} days old")


def simulate_plant(plant: Plant):
    plant.age()
    plant.grow()


def main() -> None:
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Sunflower", 80, 45)
    plant_3 = Plant("Cactus", 15, 120)
    print("=== Day 1 ===")
    plant_1.get_info()
    plant_2.get_info()
    plant_3.get_info()


main()

#!/usr/bin/env python3

class Plant:
    """
    This class acts as a blueprint for Plant objects.

    It builds those objects through the __init__ method.
    Example:
    new_plant = Plant("Sunflower", 30, 60)
    """
    def __init__(self, name: str, height: int, lifetime: int) -> None:
        self.name = name
        self.height = height
        self.lifetime = lifetime


def main():
    """
    This function creates Plant objects and displays their information.
    """
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Sunflower", 80, 45)
    plant_3 = Plant("Cactus", 15, 120)
    print(
        "=== Garden Plant Registry ===\n"
        f"{plant_1.name}: {plant_1.height}cm, {plant_1.lifetime} days old\n"
        f"{plant_2.name}: {plant_2.height}cm, {plant_2.lifetime} days old\n"
        f"{plant_3.name}: {plant_3.height}cm, {plant_3.lifetime} days old"
    )


main()

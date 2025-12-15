#!/usr/bin/env python3

class GardenError(Exception):
    """
    Base class for all garden-related errors.
    """
    pass


class PlantError(GardenError):
    """
    Error related to plant status.
    """
    pass


class WaterError(GardenError):
    """
    Error related to watering systems.
    """
    pass


def test_plant_error() -> str:
    """
    Raises a PlantError and returns a message
    """
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        return f"Caught PlantError: {e}\n"


def test_water_error() -> str:
    """
    Raises a WaterError and returns a message
    """
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        return f"Caught WaterError: {e}\n"


def test_garden_error() -> None:
    """
    Raises a PlantError and a WaterError and catches both.
    """
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")


def test_errors() -> None:
    """
    Orchestrates the testing of GardenError, PlantError and WaterError

    Displays all messages.
    """
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    print(test_plant_error())
    print("Testing WaterError...")
    print(test_water_error())
    print("Testing catching all garden errors...")
    test_garden_error()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_errors()

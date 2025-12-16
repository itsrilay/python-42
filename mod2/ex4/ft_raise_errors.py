#!/usr/bin/env python3

def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int) -> str:
    """
    Checks if all plant attributes are valid.

    Raises error on invalid attribute.
    """
    try:
        if not plant_name:
            raise ValueError("Plant name cannot be empty!")

        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")

        if sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        if sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )
    except TypeError:
        raise ValueError("Water level and sunlight hours must be valid ints")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """
    Tests the Health Checker with valid and invalid values.
    """
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    print(check_plant_health("tomato", 4, 7))
    print()

    print("Testing empty plant name...")
    try:
        check_plant_health("", 4, 7)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 7)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 4, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()

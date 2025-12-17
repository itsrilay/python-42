#!/usr/bin/env python3

def water_plants(plant_list: list[object]) -> None:
    """
    Waters plants in the list.

    Raises error when plant isn't a str and handles it. Ensures cleanup.
    """
    try:
        print("Opening watering system")
        for plant in plant_list:
            if not isinstance(plant, str):
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
    Tests the watering system with valid and invalid lists.
    """
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")
    print()

    print("Testing with error...")
    water_plants(["tomato", None, "lettuce"])
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()

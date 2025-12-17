#!/usr/bin/env python3

def water_plants(plant_list: list[object]) -> None:
    """
    Waters plants in the list.

    Raises error when plant isn't a str and handles it. Ensures cleanup.
    """
    plant = None
    try:
        print("Opening watering system")
        for plant in plant_list:
            # Will raise exception on a non-str value
            print("Watering " + plant)  # type: ignore
    except TypeError:
        print(f"Error: Cannot water {plant} - invalid plant!")
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

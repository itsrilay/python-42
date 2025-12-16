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


class GardenManager:
    """
    Manages list of plants, their health and watering system.
    """
    def __init__(self) -> None:
        """
        Initializes an empty list of plants.
        """
        self.plants: list[tuple[str, int, int]] = []

    def check_plant_health(self, name: str, water: int, sun: int) -> None:
        """
        Validates plant health metrics.
        """
        try:
            if not name:
                raise PlantError("Plant name cannot be empty!")

            if water < 1:
                raise PlantError(f"Water level {water} is too low (min 1)")
            if water > 10:
                raise PlantError(f"Water level {water} is too high (max 10)")

            if sun < 2:
                raise PlantError(f"Sunlight hours {sun} is too low (min 2)")
            if sun > 12:
                raise PlantError(
                    f"Sunlight hours {sun} is too high (max 12)"
                )
        except TypeError:
            raise PlantError(
                f"Invalid data for {name}: water and sun must be numbers"
            )

    def add_plant(self, name: str, water: int, sun: int) -> None:
        """
        Adds a plant to the plant list.
        """
        try:
            if not name:
                raise PlantError("Plant name cannot be empty!")
            self.plants.append((name, water, sun))
            print(f"Added {name} successfully")
        except (PlantError, TypeError) as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        """
        Simulates watering plants in the plant list.
        """
        try:
            print("Opening watering system")
            for plant in self.plants:
                print(f"Watering {plant[0]} - success")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_all_plants(self) -> None:
        """
        Validates the health of every plant in the list.
        """
        for plant in self.plants:
            try:
                self.check_plant_health(plant[0], plant[1], plant[2])
                print(
                    f"{plant[0]}: healthy (water: {plant[1]}, sun: {plant[2]})"
                )
            except PlantError as e:
                print(f"Error checking {plant[0]}: {e}")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    manager = GardenManager()

    print("Adding plants to garden...")
    manager.add_plant("tomato", 5, 8)
    manager.add_plant("lettuce", 15, 6)
    manager.add_plant("", 5, 8)

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    manager.check_all_plants()

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")

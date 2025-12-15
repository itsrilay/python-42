#!/usr/bin/env python3

class Plant:
    """
    Acts as a blueprint for Plant objects.
    """
    def __init__(self, name: str, height: int) -> None:
        """
        Initializes common attributes for any plant.
        """
        self.name = name
        self.height = height
        self.growth_amount = 0

    def grow(self) -> str:
        """
        Increases the plant's height by 1 unit.

        Tracks plant's total growth.
        """
        self.height += 1
        self.growth_amount += 1
        return f"{self.name} grew 1cm"

    def __str__(self) -> str:
        """
        Displays the base information (name, type, height, age).
        """
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """
    Acts as a blueprint for FloweringPlant objects.
    """
    def __init__(self, name: str, height: int, color: str) -> None:
        """
        Calls parent __init__ method for common attributes.

        Initializes color attribute.
        """
        super().__init__(name, height)
        self.color = color

    def __str__(self) -> str:
        """
        Extends parent __str__ to display color.
        """
        base = super().__str__()
        return base + f", {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """
    Acts as a blueprint for PrizeFlower objects.
    """
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        """
        Calls parent __init__ method for common attributes.

        Initializes prize attribute.
        """
        super().__init__(name, height, color)
        self.prize = prize

    def __str__(self) -> str:
        """
        Extends parent __str__ to display prize points.
        """
        base = super().__str__()
        return base + f", Prize points: {self.prize}"


class Garden:
    """
    Acts as a blueprint for Garden objects.
    """
    def __init__(self, owner: str) -> None:
        """
        Initializes attributes for Garden objects.
        """
        self.owner = owner
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> str:
        """
        Adds a Plant object to the Garden plants list.
        """
        self.plants.append(plant)
        return f"Added {plant.name} to {self.owner}'s garden"

    def get_score(self) -> int:
        """
        Calculates score for a Garden plants list.
        """
        score = 0
        for plant in self.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize
            if isinstance(plant, FloweringPlant):
                score += 15
        return score


class GardenManager:
    """
    Acts as a blueprint for GardenManager objects.

    Manages list of Garden objects.
    """
    def __init__(self) -> None:
        """
        Initializes an empty dictionary to store Garden objects.

        str - Owner name.
        Garden - Garden object.
        """
        self.gardens: dict[str, Garden] = {}

    def add_garden(self, garden: Garden) -> None:
        """
        Adds Garden object to dictionary.
        """
        self.gardens[garden.owner] = garden

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> "GardenManager":
        """
        Creates a garden network by initializing a GardenManager object.
        Creates Garden objects to add to the GardenManager dictionary.
        """
        manager = GardenManager()
        for owner in owners:
            garden = Garden(owner)
            manager.add_garden(garden)
        return manager

    class GardenStats:
        """
        Calculates Garden statistics.
        """
        @staticmethod
        def count_plants(plants: list[Plant]) -> int:
            """
            Calculates number of Plant objects in a list.
            """
            return len(plants)

        @staticmethod
        def get_plant_types(plants: list[Plant]) -> dict[str, int]:
            """
            Calculates number of instances for different Plant types.
            """
            counts = {"Regular": 0, "Flowering": 0, "Prize": 0}
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    counts["Prize"] += 1
                elif isinstance(plant, FloweringPlant):
                    counts["Flowering"] += 1
                else:
                    counts["Regular"] += 1
            return counts

        @staticmethod
        def get_total_growth(plants: list[Plant]) -> int:
            """
            Calculates total growth in a Plant object list.
            """
            total_growth = 0
            for plant in plants:
                total_growth += plant.growth_amount
            return total_growth


def height_check(plants: list[Plant]) -> bool:
    """
    Checks for valid height value (> 0)
    """
    for plant in plants:
        if plant.height <= 0:
            return False
    return True


def main() -> None:
    """
    Orchestrates the creation of the garden network.

    Displays statistics and score.
    """
    plants_alice: list[Plant] = [
        Plant("Oak Tree", 100),
        FloweringPlant("Rose", 25,  "red"),
        PrizeFlower("Sunflower", 50, "yellow", 10)
    ]
    plant_bob = Plant("Cacao Tree", 92)
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager.create_garden_network(["Alice", "Bob"])
    alice = manager.gardens["Alice"]
    bob = manager.gardens["Bob"]
    for plant in plants_alice:
        print(alice.add_plant(plant))
    bob.add_plant(plant_bob)
    print()
    print("Alice is helping all plants grow...")
    for plant in alice.plants:
        print(plant.grow())
    print()
    print("=== Alice's Garden Report ===")
    print("Plants in garden:")
    for plant in alice.plants:
        print(plant)
    print()
    plant_count = GardenManager.GardenStats.count_plants(alice.plants)
    plant_growth = GardenManager.GardenStats.get_total_growth(alice.plants)
    plant_types = GardenManager.GardenStats.get_plant_types(alice.plants)
    print(f"Plants added: {plant_count}, Total growth: {plant_growth}cm")
    print(
        "Plant types: "
        f"{plant_types['Regular']} regular, "
        f"{plant_types['Flowering']} flowering, "
        f"{plant_types['Prize']} prize flowers\n"
    )
    print(f"Height validation test: {height_check(alice.plants)}")
    print(
        "Garden scores - "
        f"{alice.owner}: {alice.get_score()}, "
        f"{bob.owner}: {bob.get_score()}"
    )
    print(f"Total gardens managed: {len(manager.gardens)}")


if __name__ == "__main__":
    main()

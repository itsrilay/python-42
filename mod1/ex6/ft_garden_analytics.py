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

    def grow(self) -> None:
        self.height += 1
        self.growth_amount += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> None:
        """
        Displays the base information (name, type, height, age).
        """
        print(f"- {self.name}: {self.height}cm", end="")


class FloweringPlant(Plant):
    """
    Acts as a blueprint for FloweringPlant objects.
    """
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def get_info(self) -> None:
        super().get_info()
        print(f", {self.color} flowers (blooming)", end="")


class PrizeFlower(FloweringPlant):
    """
    Acts as a blueprint for PrizeFlower objects.
    """
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self.prize = prize

    def get_info(self) -> None:
        super().get_info()
        print(f", Prize points: {self.prize}", end="")


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def add_plant_list(self, plants: list[Plant]) -> None:
        for plant in plants:
            self.add_plant(plant)

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def get_score(self) -> int:
        score = 0
        for plant in self.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize
            if isinstance(plant, FloweringPlant):
                score += 15
        return score


class GardenManager:
    def __init__(self) -> None:
        self.gardens: dict[str, Garden] = {}

    def add_garden(self, garden: Garden) -> None:
        self.gardens[garden.owner] = garden

    @classmethod
    def create_garden_network(cls, owners: list[str]):
        manager = GardenManager()
        for owner in owners:
            garden = Garden(owner)
            manager.add_garden(garden)
        return manager

    class GardenStats:

        @staticmethod
        def count_plants(plants: list[Plant]) -> int:
            return len(plants)

        @staticmethod
        def get_plant_types(plants: list[Plant]) -> dict[str, int]:
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
            total_growth = 0
            for plant in plants:
                total_growth += plant.growth_amount
            return total_growth


def height_check(plants: list[Plant]) -> bool:
    for plant in plants:
        if plant.height <= 0:
            return False
    return True


def main() -> None:
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
    alice.add_plant_list(plants_alice)
    bob.add_plant(plant_bob)
    print()
    alice.grow_all()
    print()
    print("=== Alice's Garden Report ===")
    print("Plants in garden:")
    for plant in alice.plants:
        plant.get_info()
        print()
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

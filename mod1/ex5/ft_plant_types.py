class Plant:
    """
    Acts as a blueprint for all plant types.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes common attributes for any plant.
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        """
        Displays the base information (name, type, height, age).
        """
        class_name = self.__class__.__name__
        print(f"{self.name}, ({class_name}): "
              f"{self.height}cm, {self.age} days, ", end="")


class Flower(Plant):
    """
    Represents a specialized Plant type: Flower.
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initializes a Flower with an additional color attribute.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """
        Simulates the flower blooming.
        """
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        """
        Extends parent get_info to display color.
        """
        super().get_info()
        print(f"{self.color} color")


class Tree(Plant):
    """
    Represents a specialized Plant type: Tree.
    """
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int
    ) -> None:
        """
        Initializes a Tree with an additional trunk diameter attribute.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """
        Calculates and displays the shade produced based on height.
        """
        shade = self.height * 0.4
        print(f"{self.name} provides {shade:0n} square meters of shade")

    def get_info(self) -> None:
        """
        Extends parent get_info to display trunk diameter.
        """
        super().get_info()
        print(f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    Represents a specialized Plant type: Vegetable.
    """
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str
    ) -> None:
        """
        Initializes a Vegetable with harvest and nutrition info.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_benefits(self) -> None:
        """
        Displays the nutritional benefits of the vegetable.
        """
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self) -> None:
        """
        Extends parent get_info to display harvest season.
        """
        super().get_info()
        print(f"{self.harvest_season} harvest")


def plant_generator(plants: list[tuple[str, int, int]]):
    """
    Yields Plant objects from a list of tuples
    """
    for plant in plants:
        yield Plant(plant[0], plant[1], plant[2])


def flower_generator(flowers: list[tuple[str, int, int, str]]):
    """
    Yields Flower objects from a list of tuples
    """
    for flower in flowers:
        yield Flower(flower[0], flower[1], flower[2], flower[3])


def tree_generator(trees: list[tuple[str, int, int, int]]):
    """
    Yields Tree objects from a list of tuples
    """
    for tree in trees:
        yield Tree(tree[0], tree[1], tree[2], tree[3])


def vegetable_generator(vegetables: list[tuple[str, int, int, str, str]]):
    """
    Yields Flower objects from a list of tuples
    """
    for vege in vegetables:
        yield Vegetable(vege[0], vege[1], vege[2], vege[3], vege[4])


def main() -> None:
    """
    Demonstrates inheritance by iterating through specialized plant lists.
    """
    flowers = [
        ("Rose", 25, 30, "red"),
        ("Sunflower", 80, 45, "yellow")
    ]
    trees = [
        ("Oak", 500, 1825, 50),
        ("Cacao", 700, 1123, 30)
    ]
    vegetables = [
        ("Tomato", 80, 90, "summer", "vitamin C"),
        ("Lettuce", 50, 40, "spring", "vitamin A")
    ]
    print("=== Garden Plant Types ===\n")
    for flower in flower_generator(flowers):
        flower.get_info()
        flower.bloom()
        print()
    for tree in tree_generator(trees):
        tree.get_info()
        tree.produce_shade()
        print()
    for vege in vegetable_generator(vegetables):
        vege.get_info()
        vege.show_benefits()
        print()
    print("==========================")


if __name__ == "__main__":
    main()

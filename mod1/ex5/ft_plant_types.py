#!/usr/bin/env python3

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

    def __str__(self) -> str:
        """
        Displays the base information (name, type, height, age).
        """
        cls_name = self.__class__.__name__
        return f"{self.name} ({cls_name}): {self.height}cm, {self.age} days, "


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

    def bloom(self) -> str:
        """
        Simulates the flower blooming.
        """
        return f"{self.name} is blooming beautifully!"

    def __str__(self) -> str:
        """
        Extends parent __str__ to display color.
        """
        base = super().__str__()
        return base + f"{self.color} color"


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

    def produce_shade(self) -> str:
        """
        Calculates and displays the shade produced based on height.
        """
        shade = self.height * 0.4
        return f"{self.name} provides {shade:0n} square meters of shade"

    def __str__(self) -> str:
        """
        Extends parent __str__ to display trunk diameter.
        """
        base = super().__str__()
        return base + f"{self.trunk_diameter}cm diameter"


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

    def show_benefits(self) -> str:
        """
        Displays the nutritional benefits of the vegetable.
        """
        return f"{self.name} is rich in {self.nutritional_value}"

    def __str__(self) -> str:
        """
        Extends parent __str__ to display harvest season.
        """
        base = super().__str__()
        return base + f"{self.harvest_season} harvest"


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
        print(flower)
        print(flower.bloom())
        print()
    for tree in tree_generator(trees):
        print(tree)
        print(tree.produce_shade())
        print()
    for vege in vegetable_generator(vegetables):
        print(vege)
        print(vege.show_benefits())
        print()
    print("==========================")


if __name__ == "__main__":
    main()

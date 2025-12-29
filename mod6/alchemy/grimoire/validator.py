"""Module for validating spell ingredients based on elemental keywords."""


def validate_ingredients(ingredients: str) -> str:
    """Checks if the ingredient string contains valid elemental keywords."""
    valid_elements = ["fire", "water", "earth", "air"]
    for item in ingredients.split(" "):
        if item not in valid_elements:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"

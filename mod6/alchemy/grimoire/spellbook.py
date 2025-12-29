"""Module for recording spells in the grimoire using late imports."""


def record_spell(spell_name: str, ingredients: str) -> str:
    """Record the spell if the ingredient validation passes."""
    from .validator import validate_ingredients

    val_result = validate_ingredients(ingredients)

    if "INVALID" in val_result:
        return f"Spell rejected: {spell_name} ({val_result})"
    else:
        return f"Spell recorded: {spell_name} ({val_result})"

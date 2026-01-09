"""
Exercise 0: Lambda Sanctum

This module demonstrates the use of anonymous functions (lambdas) in Python.
It includes functions for sorting artifacts, filtering mages by power,
transforming spell names, and calculating mage statistics using functional
programming patterns.
"""

from typing import TypedDict


class Artifact(TypedDict):
    """Represents a magical artifact with name, power, and type."""
    name: str
    power: int
    type: str


class Mage(TypedDict):
    """Represents a mage with name, power level, and elemental affinity."""
    name: str
    power: int
    element: str


class PowerStats(TypedDict):
    """Container for aggregated power statistics."""
    max_power: int
    min_power: int
    avg_power: float


def artifact_sorter(artifacts: list[Artifact]) -> list[Artifact]:
    """
    Sorts a list of artifacts by power in descending order.

    Args:
        artifacts: A list of Artifact dictionaries.

    Returns:
        A new list of Artifacts sorted by power (highest to lowest).
    """
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[Mage], min_power: int) -> list[Mage]:
    """
    Filters mages to keep only those meeting a minimum power threshold.

    Args:
        mages: A list of Mage dictionaries.
        min_power: The minimum power level required.

    Returns:
        A list of Mage dictionaries with power >= min_power.
    """
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """
    Applies visual formatting to a list of spell names.

    Args:
        spells: A list of spell names (strings).

    Returns:
        A new list of strings where each spell is wrapped in '*' symbols.
    """
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[Mage]) -> PowerStats:
    """
    Calculates aggregate power statistics for a group of mages.

    Args:
        mages: A list of Mage dictionaries.

    Returns:
        A PowerStats dictionary containing max, min, and average power.
    """
    powers = list(map(lambda m: m["power"], mages))

    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2)
    }


def main() -> None:
    """
    Executes test scenarios for Exercise 0: Lambda Sanctum.
    """
    artifacts: list[Artifact] = [
        {"name": "Crystal Orb", "power": 85, "type": "relic"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"}
    ]

    spells = ["fireball", "heal", "shield"]

    mages: list[Mage] = [
        {'name': 'Luna', 'power': 58, 'element': 'wind'},
        {'name': 'River', 'power': 51, 'element': 'water'},
        {'name': 'Kai', 'power': 63, 'element': 'light'},
        {'name': 'Ember', 'power': 93, 'element': 'ice'},
        {'name': 'Rowan', 'power': 74, 'element': 'light'}
    ]

    print("\nTesting artifact sorter...")
    s_artifacts = artifact_sorter(artifacts)
    artifact_1 = f"{s_artifacts[0]['name']} ({s_artifacts[0]['power']} power)"
    artifact_2 = f"{s_artifacts[1]['name']} ({s_artifacts[1]['power']} power)"
    print(f"{artifact_1} comes before {artifact_2}")

    print("\nTesting spell transformer...")
    t_spells = spell_transformer(spells)
    print(*t_spells)

    print("\nTesting power filter...")
    filtered_mages = power_filter(mages, 60)
    print("Strong mages:")
    for mage in filtered_mages:
        print(f"- {mage['name']} ({mage['power']} power)")
    print("Weak mages:")
    for mage in list(filter(lambda m: m not in filtered_mages, mages)):
        print(f"- {mage['name']} ({mage['power']} power)")

    print("\nTesting mage stats...")
    stats_mages = mage_stats(mages)
    print(f"Max power: {stats_mages['max_power']}")
    print(f"Min power: {stats_mages['min_power']}")
    print(f"Avg power: {stats_mages['avg_power']}")


if __name__ == "__main__":
    main()

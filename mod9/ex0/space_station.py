"""
Space Station Data Validation Module.

This module defines the data model for space station monitoring and provides
a demonstration of valid and invalid data handling using Pydantic.
"""

from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """
    Represents a space station's operational status and vital metrics.

    Validates dimensions, environmental controls, and maintenance status
    according to Observatory regulations.
    """
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    """
    Demonstrates the usage of the SpaceStation model.

    Creates a valid instance to show successful data parsing and attempts
    to create an invalid instance to demonstrate error handling.
    """
    print("Space Station Data Validation")
    print("========================================")
    valid = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.today()
    )
    print("Valid station created:")
    print(f"ID: {valid.station_id}")
    print(f"Name: {valid.name}")
    print(f"Crew: {valid.crew_size} people")
    print(f"Power: {valid.power_level}%")
    print(f"Oxygen: {valid.oxygen_level}%")
    print(
        f"Status: {'Operational' if valid.is_operational else 'Inoperative'}"
    )

    print("\n========================================")
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="ISS002",
            name="International Space Station 2",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.today()
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()

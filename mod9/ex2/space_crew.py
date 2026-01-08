"""
Space Crew Management Module.

This module defines models for crew members and space missions, implementing
nested validation logic to ensure safety protocols and crew composition
requirements.
"""

from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class Rank(str, Enum):
    """Enumeration of space crew ranks."""
    CDT = "cadet"
    OFF = "officer"
    LT = "lieutenant"
    CPT = "captain"
    COM = "commander"


class CrewMember(BaseModel):
    """
    Represents an individual space crew member.

    Validates personal details, rank, experience, and operational status.
    """
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """
    Represents a planned space mission including its assigned crew.

    Enforces complex safety regulations regarding leadership presence,
    crew experience ratios for long-duration flights, and active duty status.
    """
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_custom_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if not [m for m in self.crew if m.rank in [Rank.COM, Rank.CPT]]:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        if self.duration_days > 365:
            experienced = [m for m in self.crew if m.years_experience >= 5]
            if len(experienced) / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew " +
                    "(5+ years)"
                )
        if [m for m in self.crew if not m.is_active]:
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    """
    Demonstrates the usage of the SpaceMission model.

    Creates a valid mission with a compliant crew and tests error handling
    by attempting to create a mission that violates safety protocols.
    """
    print("Space Mission Crew Validation")
    print("=========================================")
    valid_crew = [
        CrewMember(
            member_id="CM001",
            name="Sarah Connor",
            rank=Rank.COM,
            age=45,
            specialization="Mission Command",
            years_experience=15,
            is_active=True
        ),
        CrewMember(
            member_id="CM002",
            name="John Smith",
            rank=Rank.LT,
            age=32,
            specialization="Navigation",
            years_experience=8,
            is_active=True
        ),
        CrewMember(
            member_id="CM003",
            name="Alice Johnson",
            rank=Rank.OFF,
            age=28,
            specialization="Engineering",
            years_experience=3,
            is_active=True
        )
    ]

    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 5, 15),
        duration_days=900,
        crew=valid_crew,
        budget_millions=2500.0
    )

    print("Valid mission created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")
    for member in valid_mission.crew:
        print(f"- {member.name} ({member.rank}) - {member.specialization}")

    print("\n=========================================")
    print("Expected validation error:")
    invalid_crew = [
        CrewMember(
            member_id="CM001",
            name="Sarah Connor",
            rank=Rank.OFF,
            age=45,
            specialization="Mission Command",
            years_experience=15,
            is_active=True
        ),
        CrewMember(
            member_id="CM002",
            name="John Smith",
            rank=Rank.LT,
            age=32,
            specialization="Navigation",
            years_experience=8,
            is_active=True
        ),
        CrewMember(
            member_id="CM003",
            name="Alice Johnson",
            rank=Rank.OFF,
            age=28,
            specialization="Engineering",
            years_experience=3,
            is_active=True
        )
    ]

    try:
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 5, 15),
            duration_days=900,
            crew=invalid_crew,
            budget_millions=2500.0
        )
    except ValidationError as e:
        msg = e.errors()[0]["msg"]
        print(msg.replace("Value error, ", ""))


if __name__ == "__main__":
    main()

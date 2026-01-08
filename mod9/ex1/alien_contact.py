"""
Alien Contact Log Validation Module.

This module defines the data model for recording alien encounters and
implements custom business logic for verifying reports based on
contact type and signal data.
"""

from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class ContactType(str, Enum):
    """Enumeration of recognized alien contact classifications."""
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """
    Represents a single report of an alien encounter.

    Validates field constraints and enforces complex business rules regarding
    verification status, witness requirements, and signal characteristics.
    """
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_custom_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses"
                )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )

        return self


def main() -> None:
    """
    Demonstrates the usage of the AlienContact model.

    Creates a valid contact report and attempts to create an invalid one
    to showcase the custom validation rules in action.
    """
    print("Alien Contact Log Validation")
    print("======================================")
    valid = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.today(),
        contact_type=ContactType.RADIO,
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli"
    )
    print("Valid contact report:")
    print(f"ID: {valid.contact_id}")
    print(f"Type: {valid.contact_type}")
    print(f"Location: {valid.location}")
    print(f"Signal: {valid.signal_strength}/10")
    print(f"Duration: {valid.duration_minutes} minutes")
    print(f"Witnesses: {valid.witness_count}")
    print(f"Message: '{valid.message_received}'")

    print("\n======================================")
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.today(),
            contact_type=ContactType.TELEPATHIC,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli"
        )
    except ValidationError as e:
        msg = e.errors()[0]["msg"]
        print(msg.replace("Value error, ", ""))


if __name__ == "__main__":
    main()

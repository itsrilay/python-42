"""
Exercise 4: Master's Tower

This module demonstrates advanced decorator patterns including:
- Simple decorators (timer)
- Decorator factories with arguments (power validator)
- Exception handling decorators (retry logic)
- Class integration with static methods
"""

from typing import Callable, Any
from functools import wraps
from time import time


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that measures and prints the execution time of a function.

    Args:
        func: The function to be timed.

    Returns:
        The wrapped function which prints timing info upon execution.
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time()

        result = func(*args, **kwargs)

        end = time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    """
    A decorator factory that validates if a spell has sufficient power.

    It searches through the arguments for the first integer (the power level)
    and compares it against min_power.

    Args:
        min_power: The minimum power level required to cast the spell.

    Returns:
        A decorator that enforces the power check.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Find the first integer argument to treat as 'power'
            for arg in args:
                if isinstance(arg, int):
                    if arg >= min_power:
                        return func(*args, **kwargs)
                    else:
                        return "Insufficient power for this spell"
            # Fallback if no integer is found
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    """
    A decorator factory that retries a function if it raises an exception.

    Args:
        max_attempts: The maximum number of times to try the function.

    Returns:
        A decorator that implements the retry logic.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempt += 1
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    """
    Represents a Guild of Mages with validation and spell-casting capabilities.
    """

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        Validates a mage's name.

        Args:
            name: The name to validate.

        Returns:
            True if name > 2 chars and contains only letters/spaces.
        """
        if len(name) > 2 and name.replace(" ", "").isalpha():
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """
        Casts a spell if the power level is sufficient.

        Args:
            spell_name: The name of the spell.
            power: The power level of the spell.

        Returns:
            A success message string.
        """
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    """Executes test scenarios for Exercise 4: Master's Tower."""
    print("\nTesting spell timer...")

    @spell_timer
    def fireball() -> str:
        from time import sleep
        sleep(0.1)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\nTesting MageGuild...")
    guild = MageGuild()

    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Gandalf 2.0"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))

    print("\nTesting spell retry...")

    @retry_spell(3)
    def failure() -> None:
        raise ValueError

    print(failure())


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int | None:
    """
    Checks if the str passed as argument is a valid temperature for plants.
    Return an integer on success, None on failure.
    """
    try:
        temp = int(temp_str)
        if 0 <= temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!\n")
            return temp
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperature_input() -> None:
    """
    Provides input values for check_temperature to test it.
    """
    test_values = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===\n")
    for value in test_values:
        print(f"Testing temperature: {value}")
        check_temperature(value)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()

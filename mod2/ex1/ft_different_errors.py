#!/usr/bin/env python3

def garden_operations(test: str) -> None:
    """
    Raises different exceptions, depending on input str.
    """
    if test == "ValueError":
        int("abc")
    elif test == "ZeroDivisionError":
        int(20 / 0)
    elif test == "FileNotFoundError":
        open("missing.txt")
    elif test == "KeyError":
        dict = {}
        dict["missing\\_plant"]


def test_error_types() -> None:
    """
    Manages testing of common exceptions, and multiple together.
    """
    errors = [
        "ValueError",
        "ZeroDivisionError",
        "FileNotFoundError",
        "KeyError",
    ]
    print("=== Garden Error Types Demo ===\n")
    for error in errors:
        try:
            print(f"Testing {error}...")
            garden_operations(error)
        except ValueError:
            print("Caught ValueError: invalid literal for int()\n")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero\n")
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'\n")
        except KeyError:
            print("Caught KeyError: 'missing\\_plant'\n")
    print("Testing multiple errors together...")
    try:
        garden_operations(errors[0])
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

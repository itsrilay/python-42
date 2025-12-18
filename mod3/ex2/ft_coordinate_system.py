#!/usr/bin/env python3

import sys
import math


def process_coordinates(coord_str: str) -> tuple[float, float, float] | None:
    """
    Splits str and converts each str in the array to a float.

    Returns a tuple containing floats, or None in case of an error.
    """
    try:
        str_x, str_y, str_z = coord_str.split(sep=",")

        coords = (float(str_x), float(str_y), float(str_z))

        display_coords = tuple(int(c) if c == int(c) else c for c in coords)

        print(f"Position created: {display_coords}")

        origin = (0, 0, 0)
        x1, y1, z1 = origin
        x2, y2, z2 = coords

        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        print(
            f"Distance between {origin} and {display_coords}: {distance:.2f}\n"
        )

        return coords
    except (IndexError, ValueError) as e:
        print(
            f"Error parsing coordinates: {e}\n"
            f"Error details - Type: {e.__class__.__name__}, Args: {e.args}"
        )


def unpack_coordinates(coords: tuple[float, float, float]) -> None:
    """
    Unpacks coordinate tuple and displays each coordinate.
    """
    x, y, z = coords

    d_x = int(x) if x == int(x) else x
    d_y = int(y) if y == int(y) else y
    d_z = int(z) if z == int(z) else z

    print(
        "Unpacking demonstration:\n"
        f"Player at x={d_x}, y={d_y}, z={d_z}\n"
        f"Coordinates: X={d_x}, Y={d_y}, Z={d_z}"
    )


def main() -> None:
    """
    Orchestrates the processing and displaying of coordinates.
    """
    print("=== Game Coordinate System ===\n")
    try:
        arg = sys.argv[1]
        coords = process_coordinates(arg)
        if coords:
            unpack_coordinates(coords)
    except IndexError:
        tests = [
            "10,20,5",
            "3,4,0",
            "abc,def,ghi"
        ]
        process_coordinates(tests[0])
        print(f'Parsing coordinates: "{tests[1]}"')
        coords = process_coordinates(tests[1])
        print(f'Parsing invalid coordinates: "{tests[2]}"')
        process_coordinates(tests[2])
        print()
        if coords:
            unpack_coordinates(coords)


if __name__ == "__main__":
    main()

"""
Matrix Analysis Tool.

This script demonstrates dependency management by checking for required
libraries (pandas, requests, matplotlib) before simulating and visualizing
Matrix system data.
"""

import importlib
from sys import stderr


def main() -> None:
    """
    Main entry point for the Matrix analysis.

    This function checks for dependencies (pandas, requests, matplotlib),
    handles any import errors by providing installation instructions, and
    analyzes simulated Matrix data to generate a visualization.
    """
    print("\nLOADING STATUS: Loading programs...")

    libs: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready"
    }

    missing_libs: list[str] = []

    print("\nChecking dependencies:")

    for lib_name, description in libs.items():
        try:
            lib = importlib.import_module(lib_name)

            version = lib.__version__

            print(f"[OK] {lib_name} ({version}) - {description}")

        except ImportError:
            print(f"[FAIL] {lib_name} is missing")
            missing_libs.append(lib_name)

    if missing_libs:
        print("\nPlease install these missing dependencies:", file=stderr)
        for lib_name in missing_libs:
            print(lib_name)

        print("\n- To install dependencies with pip run:", file=stderr)
        print("\tpip install -r requirements.txt", file=stderr)
        print("- And then run the script:", file=stderr)
        print("\tpython3 loading.py", file=stderr)

        print("\n- To install dependencies with Poetry run:", file=stderr)
        print("\tpoetry install", file=stderr)
        print("- And then run the script:", file=stderr)
        print("\tpoetry run python loading.py", file=stderr)
    else:
        import numpy
        import pandas
        import matplotlib.pyplot as plt

        print("\nAnalyzing Matrix data...")

        panda_dict: dict[str, object] = {
            "id": numpy.arange(1000),
            "level": numpy.random.randint(1, 100, size=1000),
            "status": numpy.random.choice(
                ["Active", "Corrupted"], size=1000, p=[0.5, 0.5]
            )
        }

        data = pandas.DataFrame(panda_dict)

        print(f"Processing {len(data)} data points...")
        status_counts = data["status"].value_counts()

        print("Generating visualization...")
        status_counts.plot(kind='bar')

        plt.savefig("matrix_analysis.png")

        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()

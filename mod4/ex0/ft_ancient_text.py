#!/usr/bin/env python3

def main() -> None:
    """
    Opens and reads file, prints content to standard output.

    Catches FileNotFoundError if file doesn't exist.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    filename = "ancient_fragment.txt"
    print(f"\nAccessing Storage Vault: {filename}")
    try:
        file = open(filename, "r")
        print("Connection established...")
        print("\nRECOVERED DATA:")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()

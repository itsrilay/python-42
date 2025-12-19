#!/usr/bin/env python3

def main() -> None:
    """
    Opens and reads file, prints content to standard output.

    Catches FileNotFoundError if file doesn't exist.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("\nAccessing Storage Vault: ancient_fragment.txt")
    try:
        file = open("ancient_fragment.txt", "r")
        print("Connection established...")
        print("\nRECOVERED DATA:")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()

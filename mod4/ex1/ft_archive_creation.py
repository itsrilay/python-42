#!/usr/bin/env python3

def main() -> None:
    """
    Writes to a new file in write mode.
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    filename = "new_discovery.txt"

    print(f"\nInitializing new storage unit: {filename}")

    file = open(filename, "w")

    print("Storage unit created successfully...")
    print("\nInscribing preservation data...")

    file.write("[ENTRY 001] New quantum algorithm discovered\n")
    file.write("[ENTRY 002] Efficiency increased by 347%\n")
    file.write("[ENTRY 003] Archived by Data Archivist trainee\n")

    print("[ENTRY 001] New quantum algorithm discovered")
    print("[ENTRY 002] Efficiency increased by 347%")
    print("[ENTRY 003] Archived by Data Archivist trainee")

    file.close()

    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main() -> None:
    """
    Reads from file and writes new data to another file.
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    filename_read = "classified_data.txt"
    filename_write = "security_protocols.txt"
    print("\nInitiating secure vault access...")
    with open(filename_read, "r") as file:
        print("Vault connection established with failsafe protocols")
        print("\nSECURE EXTRACTION:")

        print(file.read())

    with open(filename_write, "w") as file:
        print("\nSECURE PRESERVATION:")

        file.write("[CLASSIFIED] New security protocols archived")

        print("[CLASSIFIED] New security protocols archived")

    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()

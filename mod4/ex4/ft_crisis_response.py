#!/usr/bin/env python3

def main() -> None:
    """
    Reads multiple files from a list of str.

    Handles FileNotFoundError and PermissionError exceptions.
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    file_list = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]
    for file in file_list:
        try:
            if file == file_list[2]:
                print(f"\nROUTINE ACCESS: Attempting access to '{file}'...")
            else:
                print(f"\nCRISIS ALERT: Attempting access to '{file}'...")
            with open(file, "r") as curr_file:
                print(f"SUCCESS: Archive recovered - ''{curr_file.read()}''")
                print("STATUS: Normal operations resumed")
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()

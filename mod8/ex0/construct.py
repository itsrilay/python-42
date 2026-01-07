import sys
import os
import site

if __name__ == "__main__":
    print("\nMATRIX STATUS: ", end="")
    virtual = sys.prefix != sys.base_prefix
    if virtual:
        print("Welcome to the construct")
    else:
        print("You're still plugged in")

    print(f"\nCurrent Python: {sys.executable}")

    if virtual:
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        print("\nPackage installation path:")
        try:
            print(site.getsitepackages()[0])
        except IndexError:
            print("Couldn't get path.")
    else:
        print("Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\nScripts\nactivate    # On Windows")

        print("\nThen run this program again.")

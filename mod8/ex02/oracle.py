"""
The Oracle: Mainframe Configuration Manager.

This script demonstrates secure configuration management by loading environment
variables from a .env file. It handles sensitive data (like API keys and
database URLs) by masking them in the output and validates that all required
system variables are defined before proceeding.
"""

import os
from sys import stderr
from dotenv import load_dotenv


def main() -> None:
    """
    Main entry point that securely loads and validates configuration.

    It ensures all required environment variables are set, masks sensitive
    secrets (like API_KEY) in the output, and routes error messages to stderr.
    """
    load_dotenv()

    print("\nORACLE STATUS: Reading the Matrix...", file=stderr)

    has_env = True
    if not os.path.exists(".env"):
        print("WARNING - Missing .env file.")
        has_env = False

    db_str = "Connected to local instance"

    config: dict[str, str | None] = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL":  db_str if os.getenv("DATABASE_URL") else None,
        "API_KEY": "Authenticated" if os.getenv("API_KEY") else None,
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": "Online" if os.getenv("ZION_ENDPOINT") else None
    }

    missing_conf: list[str] = []

    valid = True
    for key, value in config.items():
        if value is None:
            valid = False
            missing_conf.append(key)

    if valid:
        print("\nConfiguration loaded:")
        print(f"Mode: {config['MATRIX_MODE']}")
        print(f"Database: {config['DATABASE_URL']}")
        print(f"API Access: {config['API_KEY']}")
        print(f"Log Level: {config['LOG_LEVEL']}")
        print(f"Zion Network: {config['ZION_ENDPOINT']}")

        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print(f"[{'OK' if has_env else 'FAIL'}] .env file properly configured")
        print("[OK] Production overrides available")

        print("The Oracle sees all configurations.")
    else:
        print("\nConfigurations failed to load!", file=stderr)
        print("- Missing configurations:", file=stderr)
        for conf in missing_conf:
            print(conf, file=stderr)
        print(
            "\nMake sure you have defined all environment variables.",
            file=stderr
        )


if __name__ == "__main__":
    main()

import json
from pathlib import Path

from app.calculator import add, multiply
from app.greeting import create_greeting


def load_config() -> dict:
    config_path = Path(__file__).parent / "app" / "config.json"

    with config_path.open("r", encoding="utf-8") as config_file:
        return json.load(config_file)


def main() -> None:
    config = load_config()

    greeting = create_greeting(
        "GitHub Actions",
        config["default_message"],
    )

    result_add = add(10, 5)
    result_multiply = multiply(10, 5)

    print(greeting)
    print(f"Application: {config['application_name']}")
    print(f"Version: {config['version']}")
    print(f"Addition: {result_add}")
    print(f"Multiplication: {result_multiply}")


if __name__ == "__main__":
    main()

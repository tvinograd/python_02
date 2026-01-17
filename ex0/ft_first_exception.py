#!/usr/bin/env python3
"""Temperature validation system with basic exception handling."""


def check_temperature(temp_str: str) -> int | None:
    """Validate if a temperature is within 0-40°C range."""
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
        if 0 <= temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!\n")
            return temp
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            return None
        else:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
            return None
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None


def test_temperature_input() -> None:
    """Test various inputs."""
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()

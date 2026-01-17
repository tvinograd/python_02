#!/usr/bin/env python3
"""Plant health validation system that raises errors for invalid input."""


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """Validate plant health parameters and return status message."""
    if plant_name is None or plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} "
                         f"is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} "
                         f"is too low (min 1)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         f"is too high (max 12)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         f"is too low (min 2)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Test plant health checker with various inputs."""
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    try:
        status = check_plant_health("tomato", 5, 5)
        print(status)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()

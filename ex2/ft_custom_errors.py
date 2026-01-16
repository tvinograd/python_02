#!/usr/bin/env python3

class GardenError(Exception):
    """Base exception for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-related problems."""
    pass


class WaterError(GardenError):
    """Exception raised for watering-related problems."""
    pass


def check_plant_health(plant_name: str, plant_age: int) -> None:
    """Simulate checking plant health and raise PlantError if unhealthy."""
    if plant_age >= 10:
        raise PlantError(f"The {plant_name} plant is wilting!")


def check_water_level(water_level: int) -> None:
    """Check water tank level and raise WaterError if insufficient."""
    if water_level < 10:
        raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant_health("tomato", 11)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        check_water_level(3)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        check_plant_health("tomato", 12)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water_level(4)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")

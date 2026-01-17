#!/usr/bin/env python3
"""Garden management system demonstrating error handling techniques."""


class GardenError(Exception):
    """Base exception for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-related problems."""
    pass


class WaterError(GardenError):
    """Exception raised for watering-related problems."""
    pass


class GardenManager:
    """Manages garden operations with error handling."""
    def __init__(self):
        """Initialize garden with empty plant list."""
        self.plants = []

    def add_plant(self, plant_name: str) -> None:
        """Add a plant to the garden with validation."""
        if plant_name is None or plant_name == "":
            raise PlantError("Plant name cannot be empty!")

        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self) -> None:
        """Water all plants with guaranteed cleanup."""
        try:
            print("Opening watering system")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str, water_level: int,
                           sunlight_hours: int) -> str:
        """Check plant health with validation."""
        if plant_name not in self.plants:
            raise PlantError(f"Plant '{plant_name}' not found in garden!")

        # Validate water level
        if water_level > 10:
            raise ValueError(f"Water level {water_level} "
                             f"is too high (max 10)")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} "
                             f"is too low (min 1)")

        # Validate sunlight hours
        if sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             f"is too high (max 12)")
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             f"is too low (min 2)")

        return (f"{plant_name}: healthy "
                f"(water: {water_level}, sun: {sunlight_hours})")

    def simulate_water_tank_error(self) -> None:
        """Simulate a water tank error for testing."""
        raise WaterError("Not enough water in tank")


def test_garden_management() -> None:
    """Test all garden management features with error handling."""
    print("=== Garden Management System ===\n")

    garden = GardenManager()

    # Test 1: Adding plants
    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato")
        garden.add_plant("lettuce")
        garden.add_plant("")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    # Test 2: Watering plants
    print("\nWatering plants...")
    try:
        garden.water_plants()
    except WaterError as e:
        print(f"Error watering: {e}")

    # Test 3: Checking plant health
    print("\nChecking plant health...")
    try:
        status = garden.check_plant_health("tomato", 5, 8)
        print(status)
    except (PlantError, ValueError) as e:
        print(f"Error checking tomato: {e}")

    try:
        status = garden.check_plant_health("lettuce", 15, 7)
        print(status)
    except (PlantError, ValueError) as e:
        print(f"Error checking lettuce: {e}")

    # Test 4: Error recovery
    print("\nTesting error recovery...")
    try:
        garden.simulate_water_tank_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()

#!/usr/bin/env python3

def water_plants(plant_list: list) -> None:
    """Water plants from list, ensuring cleanup with finally block."""
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None or plant == "":
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Test watering system with normal and error scenarios."""
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()

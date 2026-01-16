#!/usr/bin/env python3

def garden_operations(error_type: int) -> None:
    """Demonstrate different Python exception types."""
    if error_type == 1:
        try:
            int("Hello")
        except ValueError as e:
            print(f"Caught ValueError: {e}\n")

    if error_type == 2:
        try:
            10 / 0
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}\n")

    if error_type == 3:
        try:
            open("missing.txt")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}\n")

    if error_type == 4:
        try:
            plant = {"gladiolus": 5, "cactus": 10}
            plant["missing_plant"]
        except KeyError as e:
            print(f"Caught KeyError: {e}\n")

    if error_type == 5:
        try:
            int("Hello")
            10 / 0
            open("missing.txt")
        except (ValueError, ZeroDivisionError, FileNotFoundError):
            print("Caught an error, but program continues!")


def test_error_types():
    """Test exception types."""
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    garden_operations(1)
    print("Testing ZeroDivisionError...")
    garden_operations(2)
    print("Testing FileNotFoundError...")
    garden_operations(3)
    print("Testing KeyError...")
    garden_operations(4)
    print("Testing multiple errors together....")
    garden_operations(5)
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

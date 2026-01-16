#!/usr/bin/env python3

def garden_operations(error_type: int) -> None:
    """Demonstrate different Python exception types."""
    if error_type == 1:
        int("Hello")

    if error_type == 2:
        10 / 0
    
    if error_type == 3:
        open("missing.txt")
    
    if error_type == 4:
        plant = {"gladiolus": 5, "cactus": 10}
        plant["missing_plant"]
    
    if error_type == 5:
        int("Hello")
        10 / 0
        open("missing.txt")


def test_error_types():
    """Test exception types."""
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        garden_operations(1)
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations(2)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")
    
    print("Testing FileNotFoundError...")
    try:
        garden_operations(3)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    print("Testing KeyError...")
    try:
        garden_operations(4)
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    print("Testing multiple errors together....")
    try:
        garden_operations(5)
    except (ValueError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!")

if __name__ == "__main__":
    test_error_types()

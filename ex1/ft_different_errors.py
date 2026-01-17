#!/usr/bin/env python3
"""Demonstration of different Python exception types and error handling."""


def garden_operations(error_type: str) -> None:
    """Demonstrate different Python exception types."""
    if error_type == "value":
        int("Hello")

    if error_type == "zero":
        10 / 0

    if error_type == "file":
        open("missing.txt")

    if error_type == "key":
        plant = {"gladiolus": 5, "cactus": 10}
        plant["missing_plant"]

    if error_type == "all":
        int("Hello")
        10 / 0
        open("missing.txt")


def test_error_types() -> None:
    """Test exception types."""
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    print("Testing multiple errors together....")
    try:
        garden_operations("all")
    except (ValueError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!")


if __name__ == "__main__":
    test_error_types()

"""Test arithmetic."""
from pkg_shared.numbers import addition


def test_method_is_present() -> None:
    """Confirm that the methods are present."""
    assert "add_two_numbers" in dir(addition)


def test_add_two_numbers() -> None:
    """Confirm the total is correct."""
    first_number = 1
    second_number = 2
    total = addition.add_two_numbers(first_number, second_number)
    assert total == 3  # noqa: PLR2004


from validation.input_validation import (
    validate_positive_number,
    validate_non_negative_number,
    validate_project_name,
    validate_project_number
)


def test_positive_number_is_valid():
    result = validate_positive_number(10, "Length")

    assert result is None


def test_positive_number_cannot_be_zero():
    result = validate_positive_number(0, "Length")

    assert result == "Length must be greater than zero."


def test_positive_number_cannot_be_negative():
    result = validate_positive_number(-5, "Length")

    assert result == "Length must be greater than zero."


def test_non_negative_number_is_valid():
    result = validate_non_negative_number(5, "Doors")

    assert result is None


def test_non_negative_number_can_be_zero():
    result = validate_non_negative_number(0, "Doors")

    assert result is None


def test_project_name_is_required():
    result = validate_project_name("")

    assert result == "Project name is required."


def test_project_number_is_required():
    result = validate_project_number("")

    assert result == "Project number is required."


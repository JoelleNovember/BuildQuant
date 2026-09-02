
from calculations.quantity_calculations import (
    calculate_floor_area,
    calculate_perimeter,
    calculate_gross_wall_area,
    calculate_opening_area,
    calculate_net_wall_area
)


def test_floor_area():
    result = calculate_floor_area(10, 8)

    assert result == 80


def test_perimeter():
    result = calculate_perimeter(10, 8)

    assert result == 36


def test_gross_wall_area():
    result = calculate_gross_wall_area(36, 2.7)

    assert result == 97.2


def test_door_area():
    result = calculate_opening_area(0.9, 2.1, 6)

    assert result == 11.34


def test_window_area():
    result = calculate_opening_area(1.2, 1.2, 8)

    assert result == 11.52


def test_net_wall_area():
    result = calculate_net_wall_area(97.2, 11.34, 11.52)

    assert result == 74.34


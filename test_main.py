import pytest
from main import length_converter, weight_converter, temp_converter


def test_length_converter():
    assert length_converter(2000, "meters", "kilometers") == 2
    assert length_converter(1, "miles", "meters") == pytest.approx(1609.34, 0.01)
    assert length_converter(3, "foot", "yard") == pytest.approx(1, 0.01)
    assert length_converter(100, "centimeter", "meters") == 1
    assert length_converter(1, "inch", "millimeter") == pytest.approx(25.4, 0.01)
    assert length_converter(1, "nautical mile", "meters") == pytest.approx(1852, 0.01)

def test_weight_converter():
    assert weight_converter(1000, "grams", "kilograms") == 1
    assert weight_converter(1, "pounds", "grams") == pytest.approx(453.592, 0.01)
    assert weight_converter(16, "ounce", "pounds") == pytest.approx(1, 0.01)
    assert weight_converter(1, "ton", "grams") == 1e6

def test_temp_converter():
    assert temp_converter(0, "celsius", "fahrenheit") == 32
    assert temp_converter(32, "fahrenheit", "celsius") == 0
    assert temp_converter(0, "celsius", "kelvin") == 273.15
    assert temp_converter(273.15, "kelvin", "celsius") == 0
    assert temp_converter(32, "fahrenheit", "kelvin") == pytest.approx(273.15, 0.01)
    assert temp_converter(273.15, "kelvin", "fahrenheit") == 32

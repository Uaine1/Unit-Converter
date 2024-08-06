import pytest
from project import length_converter, weight_converter, temp_converter


def test_length_converter():
    assert length_converter(10, "meters", "kilometers") == 0.01
    assert length_converter(9, "centimeter", "meters") == 0.09
    assert length_converter(23, "miles", "meters") == pytest.approx(37014.8, 0.01)
    assert length_converter(13, "foot", "yard") == pytest.approx(4.33, 0.01)
    assert length_converter(24, "inch", "millimeter") == pytest.approx(609.6, 0.01)


def test_weight_converter():
    assert weight_converter(9, "ton", "grams") == 9000000
    assert weight_converter(10, "grams", "kilograms") == 0.01
    assert weight_converter(24, "kilograms", "grams") == 24000
    assert weight_converter(23, "pounds", "grams") == pytest.approx(10433.0, 0.01)
    assert weight_converter(13, "ounce", "pounds") == pytest.approx(0.8125, 0.01)
    

def test_temp_converter():
    assert temp_converter(10, "celsius", "fahrenheit") == 50
    assert temp_converter(13, "celsius", "kelvin") == 286.15
    assert temp_converter(9, "kelvin", "celsius") == -264.15
    assert temp_converter(24, "fahrenheit", "kelvin") == pytest.approx(268.7056, 0.01)
    assert temp_converter(23, "fahrenheit", "celsius") == pytest.approx(-5, 0.01)

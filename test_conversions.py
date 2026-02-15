import pytest
from conversions import convert


class TestTemperature:
    def test_celsius_to_fahrenheit(self):
        assert convert("temperature", 0, "celsius", "fahrenheit") == 32

    def test_fahrenheit_to_celsius(self):
        assert abs(convert("temperature", 212, "fahrenheit", "celsius") - 100) < 1e-10

    def test_celsius_to_kelvin(self):
        assert abs(convert("temperature", 0, "celsius", "kelvin") - 273.15) < 1e-10

    def test_kelvin_to_celsius(self):
        assert abs(convert("temperature", 273.15, "kelvin", "celsius")) < 1e-10

    def test_same_unit(self):
        assert convert("temperature", 50, "celsius", "celsius") == 50

    def test_unknown_unit(self):
        with pytest.raises(ValueError, match="Unknown temperature unit"):
            convert("temperature", 0, "celsius", "rankine")


class TestLength:
    def test_meters_to_feet(self):
        result = convert("length", 1, "meters", "feet")
        assert abs(result - 3.28084) < 0.001

    def test_miles_to_kilometers(self):
        result = convert("length", 1, "miles", "kilometers")
        assert abs(result - 1.60934) < 0.001

    def test_inches_to_meters(self):
        result = convert("length", 1, "inches", "meters")
        assert abs(result - 0.0254) < 1e-6

    def test_unknown_unit(self):
        with pytest.raises(ValueError, match="Unknown unit"):
            convert("length", 1, "meters", "lightyears")


class TestWeight:
    def test_kg_to_pounds(self):
        result = convert("weight", 1, "kilograms", "pounds")
        assert abs(result - 2.20462) < 0.001

    def test_pounds_to_ounces(self):
        result = convert("weight", 1, "pounds", "ounces")
        assert abs(result - 16) < 0.1

    def test_unknown_unit(self):
        with pytest.raises(ValueError, match="Unknown unit"):
            convert("weight", 1, "kilograms", "stones")


class TestInvalidCategory:
    def test_unknown_category(self):
        with pytest.raises(ValueError, match="Unknown category"):
            convert("volume", 1, "liters", "gallons")

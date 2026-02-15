"""
Unit conversion module.

Temperature uses special formulas. Length and weight use factor-based conversion
relative to a base unit (meters, kilograms).
"""

# Length factors: value in meters
_LENGTH = {
    "meters": 1,
    "kilometers": 1000,
    "feet": 0.3048,
    "inches": 0.0254,
    "miles": 1609.344,
}

# Weight factors: value in kilograms
_WEIGHT = {
    "kilograms": 1,
    "pounds": 0.453592,
    "ounces": 0.0283495,
}

CATEGORIES = {
    "temperature": {"celsius": None, "fahrenheit": None, "kelvin": None},
    "length": _LENGTH,
    "weight": _WEIGHT,
}


def _convert_temperature(value, from_unit, to_unit):
    # Convert to Celsius first
    if from_unit == "celsius":
        c = value
    elif from_unit == "fahrenheit":
        c = (value - 32) * 5 / 9
    elif from_unit == "kelvin":
        c = value - 273.15
    else:
        raise ValueError(f"Unknown temperature unit: {from_unit}")

    # Convert from Celsius to target
    if to_unit == "celsius":
        return c
    elif to_unit == "fahrenheit":
        return c * 9 / 5 + 32
    elif to_unit == "kelvin":
        return c + 273.15
    else:
        raise ValueError(f"Unknown temperature unit: {to_unit}")


def _convert_by_factor(factors, value, from_unit, to_unit):
    if from_unit not in factors:
        raise ValueError(f"Unknown unit: {from_unit}")
    if to_unit not in factors:
        raise ValueError(f"Unknown unit: {to_unit}")
    base_value = value * factors[from_unit]
    return base_value / factors[to_unit]


def convert(category, value, from_unit, to_unit):
    """Convert a value from one unit to another within a category."""
    if category == "temperature":
        return _convert_temperature(value, from_unit, to_unit)
    elif category == "length":
        return _convert_by_factor(_LENGTH, value, from_unit, to_unit)
    elif category == "weight":
        return _convert_by_factor(_WEIGHT, value, from_unit, to_unit)
    else:
        raise ValueError(f"Unknown category: {category}")

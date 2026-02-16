# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

- **Run all tests:** `pytest`
- **Run a single test file:** `pytest test_calculator.py`
- **Run a single test:** `pytest test_calculator.py::test_add`
- **Run the calculator:** `python calculator.py`

## Architecture

Python scientific calculator with four modules (no external dependencies beyond pytest):

- **calculator.py** — Math functions (arithmetic, trig, log, etc.) and the interactive CLI (`main()`). CLI imports from the other modules at runtime inside `main()`.
- **expression.py** — Recursive descent parser (`evaluate()` is the public entry point). Grammar: expr → term → power → unary → atom. `^` is right-associative. Functions (sin, cos, sqrt, etc.) are dispatched via the `_FUNCTIONS` dict.
- **conversions.py** — Unit conversions. Temperature uses special formulas (convert to Celsius as intermediate). Length/weight use factor-based conversion relative to a base unit (meters/kilograms). `CATEGORIES` dict defines available units.
- **history.py** — Simple in-memory list of `(expression, result)` tuples.

Each module has a corresponding `test_*.py` file. Tests use only pytest (no fixtures or plugins).

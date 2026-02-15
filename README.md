# Python Scientific Calculator

A command-line scientific calculator with expression parsing, unit conversions, and calculation history.

## Features

- **Basic arithmetic** — addition, subtraction, multiplication, division
- **Extended operations** — power, modulo, square root, factorial
- **Scientific functions** — sin, cos, tan, log (base 10), ln (natural log)
- **Expression evaluation** — parse and evaluate expressions like `2 + 3 * sin(1.5)` with proper operator precedence
- **Unit conversions** — temperature (C/F/K), length (m/km/ft/in/mi), weight (kg/lb/oz)
- **Calculation history** — view and clear past results

## Usage

```bash
python calculator.py
```

This opens an interactive menu:

```
=== Scientific Calculator ===

1. Basic/Scientific calculation
2. Expression evaluation
3. Unit conversion
4. History
5. Quit
```

### Expression examples

```
2 + 3 * 4          → 14
(2 + 3) * 4        → 20
2 ^ 3 ^ 2          → 512
sqrt(16) + sin(0)   → 4.0
factorial(5)        → 120
```

## Running tests

```bash
pytest
```

87 tests covering all modules: calculator functions, expression parser, unit conversions, and history.

## Project structure

```
calculator.py       — Core math functions and CLI interface
expression.py       — Recursive descent expression parser
conversions.py      — Unit conversion engine
history.py          — Calculation history tracker
test_calculator.py  — Tests for calculator functions
test_expression.py  — Tests for expression parser
test_conversions.py — Tests for unit conversions
test_history.py     — Tests for history module
```

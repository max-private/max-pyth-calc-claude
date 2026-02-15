import math


# Basic arithmetic
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Additional operations
def power(a, b):
    return a ** b


def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)


def factorial(a):
    if a < 0:
        raise ValueError("Cannot take factorial of a negative number")
    if a != int(a):
        raise ValueError("Cannot take factorial of a non-integer")
    return math.factorial(int(a))


# Scientific functions
def sin(a):
    return math.sin(a)


def cos(a):
    return math.cos(a)


def tan(a):
    return math.tan(a)


def log(a, base=10):
    if a <= 0:
        raise ValueError("Cannot take logarithm of a non-positive number")
    return math.log(a, base)


def ln(a):
    if a <= 0:
        raise ValueError("Cannot take logarithm of a non-positive number")
    return math.log(a)


def main():
    from expression import evaluate
    from history import History
    from conversions import convert, CATEGORIES

    hist = History()

    print("=== Scientific Calculator ===")

    while True:
        print("\n1. Basic/Scientific calculation")
        print("2. Expression evaluation")
        print("3. Unit conversion")
        print("4. History")
        print("5. Quit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            _menu_basic(hist)
        elif choice == "2":
            _menu_expression(hist, evaluate)
        elif choice == "3":
            _menu_conversion(CATEGORIES, convert)
        elif choice == "4":
            _menu_history(hist)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


def _menu_basic(hist):
    two_arg_ops = {
        "+": ("add", add),
        "-": ("subtract", subtract),
        "*": ("multiply", multiply),
        "/": ("divide", divide),
        "^": ("power", power),
        "%": ("modulo", modulo),
    }
    one_arg_ops = {
        "sqrt": ("square root", square_root),
        "fact": ("factorial", factorial),
        "sin": ("sin", sin),
        "cos": ("cos", cos),
        "tan": ("tan", tan),
        "log": ("log base 10", log),
        "ln": ("natural log", ln),
    }

    print("\nTwo-argument: +, -, *, /, ^, %")
    print("One-argument: sqrt, fact, sin, cos, tan, log, ln")
    op = input("Operation: ").strip()

    if op in two_arg_ops:
        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
        except ValueError:
            print("Invalid number.")
            return
        try:
            result = two_arg_ops[op][1](a, b)
            expr = f"{a} {op} {b}"
            print(f"{expr} = {result}")
            hist.add(expr, result)
        except ValueError as e:
            print(f"Error: {e}")

    elif op in one_arg_ops:
        try:
            a = float(input("Number: "))
        except ValueError:
            print("Invalid number.")
            return
        try:
            result = one_arg_ops[op][1](a)
            expr = f"{op}({a})"
            print(f"{expr} = {result}")
            hist.add(expr, result)
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Invalid operation.")


def _menu_expression(hist, evaluate):
    expr = input("Enter expression: ").strip()
    if not expr:
        return
    try:
        result = evaluate(expr)
        print(f"{expr} = {result}")
        hist.add(expr, result)
    except Exception as e:
        print(f"Error: {e}")


def _menu_conversion(categories, convert):
    print("\nCategories:")
    cat_names = list(categories.keys())
    for i, name in enumerate(cat_names, 1):
        print(f"  {i}. {name}")

    try:
        idx = int(input("Category number: ")) - 1
        cat = cat_names[idx]
    except (ValueError, IndexError):
        print("Invalid category.")
        return

    units = list(categories[cat].keys())
    print(f"\nUnits: {', '.join(units)}")

    from_unit = input("From unit: ").strip().lower()
    to_unit = input("To unit: ").strip().lower()

    try:
        value = float(input("Value: "))
    except ValueError:
        print("Invalid number.")
        return

    try:
        result = convert(cat, value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")


def _menu_history(hist):
    print("\n1. Show history")
    print("2. Clear history")
    sub = input("Choice: ").strip()
    if sub == "1":
        entries = hist.show()
        if not entries:
            print("No history yet.")
        else:
            for i, (expr, result) in enumerate(entries, 1):
                print(f"  {i}. {expr} = {result}")
    elif sub == "2":
        hist.clear()
        print("History cleared.")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()

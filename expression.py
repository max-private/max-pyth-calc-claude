"""
Recursive descent expression parser.

Supports:
  - Arithmetic: +, -, *, /, %, ^
  - Operator precedence: +/- < *//% < ^ (right-associative)
  - Parentheses
  - Unary minus
  - Functions: sin, cos, tan, sqrt, log, ln, factorial
"""

import math


class ParseError(Exception):
    pass


class _Tokenizer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.tokens = []
        self._tokenize()
        self.idx = 0

    def _tokenize(self):
        i = 0
        while i < len(self.text):
            ch = self.text[i]
            if ch.isspace():
                i += 1
            elif ch in "+-*/%^()":
                self.tokens.append(ch)
                i += 1
            elif ch.isdigit() or ch == ".":
                start = i
                while i < len(self.text) and (self.text[i].isdigit() or self.text[i] == "."):
                    i += 1
                self.tokens.append(float(self.text[start:i]))
            elif ch.isalpha() or ch == "_":
                start = i
                while i < len(self.text) and (self.text[i].isalnum() or self.text[i] == "_"):
                    i += 1
                self.tokens.append(self.text[start:i])
            else:
                raise ParseError(f"Unexpected character: '{ch}'")

    def peek(self):
        if self.idx < len(self.tokens):
            return self.tokens[self.idx]
        return None

    def consume(self):
        tok = self.peek()
        self.idx += 1
        return tok

    def expect(self, expected):
        tok = self.consume()
        if tok != expected:
            raise ParseError(f"Expected '{expected}', got '{tok}'")


_FUNCTIONS = {
    "sin": lambda x: math.sin(x),
    "cos": lambda x: math.cos(x),
    "tan": lambda x: math.tan(x),
    "sqrt": lambda x: math.sqrt(x) if x >= 0 else (_ for _ in ()).throw(
        ValueError("Cannot take square root of a negative number")),
    "log": lambda x: math.log10(x) if x > 0 else (_ for _ in ()).throw(
        ValueError("Cannot take logarithm of a non-positive number")),
    "ln": lambda x: math.log(x) if x > 0 else (_ for _ in ()).throw(
        ValueError("Cannot take logarithm of a non-positive number")),
    "factorial": lambda x: math.factorial(int(x)) if x >= 0 and x == int(x) else (_ for _ in ()).throw(
        ValueError("Invalid factorial argument")),
}


def _parse_expr(tok):
    """expr = term (('+' | '-') term)*"""
    left = _parse_term(tok)
    while tok.peek() in ("+", "-"):
        op = tok.consume()
        right = _parse_term(tok)
        if op == "+":
            left = left + right
        else:
            left = left - right
    return left


def _parse_term(tok):
    """term = power (('*' | '/' | '%') power)*"""
    left = _parse_power(tok)
    while tok.peek() in ("*", "/", "%"):
        op = tok.consume()
        right = _parse_power(tok)
        if op == "*":
            left = left * right
        elif op == "/":
            if right == 0:
                raise ValueError("Cannot divide by zero")
            left = left / right
        else:
            if right == 0:
                raise ValueError("Cannot modulo by zero")
            left = left % right
    return left


def _parse_power(tok):
    """power = unary ('^' power)?  (right-associative)"""
    base = _parse_unary(tok)
    if tok.peek() == "^":
        tok.consume()
        exp = _parse_power(tok)
        return base ** exp
    return base


def _parse_unary(tok):
    """unary = '-' unary | atom"""
    if tok.peek() == "-":
        tok.consume()
        return -_parse_unary(tok)
    return _parse_atom(tok)


def _parse_atom(tok):
    """atom = NUMBER | FUNC '(' expr ')' | '(' expr ')'"""
    token = tok.peek()

    if isinstance(token, float):
        tok.consume()
        return token

    if isinstance(token, str) and token in _FUNCTIONS:
        func_name = tok.consume()
        tok.expect("(")
        arg = _parse_expr(tok)
        tok.expect(")")
        return _FUNCTIONS[func_name](arg)

    if token == "(":
        tok.consume()
        result = _parse_expr(tok)
        tok.expect(")")
        return result

    raise ParseError(f"Unexpected token: '{token}'")


def evaluate(expression):
    """Evaluate a mathematical expression string and return the result."""
    tok = _Tokenizer(expression)
    result = _parse_expr(tok)
    if tok.peek() is not None:
        raise ParseError(f"Unexpected token after expression: '{tok.peek()}'")
    return result

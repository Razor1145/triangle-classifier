"""Triangle validation and classification."""

import math


def is_valid_triangle(a, b, c) -> bool:
    """Return True when three positive finite sides form a triangle."""
    try:
        sides = (a, b, c)
        return (all(math.isfinite(side) and side > 0 for side in sides)
                and a + b > c and a + c > b and b + c > a)
    except (TypeError, ValueError, OverflowError):
        return False


def classify_triangle(a, b, c) -> str:
    """Classify a triangle by sides and whether it has a right angle."""
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c:
        shape = "Equilateral"
    elif a == b or a == c or b == c:
        shape = "Isosceles"
    else:
        shape = "Scalene"

    x, y, hypotenuse = sorted((a, b, c))
    is_right = math.isclose(
        (x / hypotenuse) ** 2 + (y / hypotenuse) ** 2,
        1.0,
        rel_tol=1e-9,
        abs_tol=1e-12,
    )
    return f"Right {shape}" if is_right else shape

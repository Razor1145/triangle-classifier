"""Unit-test examples to review against actual GitHub Copilot suggestions."""
import math
from triangle import classify_triangle, is_valid_triangle


def test_nonpositive_sides():
    assert classify_triangle(0, 4, 5) == "Invalid"
    assert classify_triangle(-1, 4, 5) == "Invalid"


def test_triangle_inequality():
    assert classify_triangle(1, 2, 4) == "Invalid"


def test_degenerate_boundary():
    assert classify_triangle(1, 2, 3) == "Invalid"


def test_equilateral():
    assert classify_triangle(3, 3, 3) == "Equilateral"


def test_isosceles():
    assert classify_triangle(5, 5, 6) == "Isosceles"


def test_scalene():
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"


def test_right_triangle_noninteger():
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"


def test_validity_function():
    assert is_valid_triangle(3, 4, 5) is True
    assert is_valid_triangle(1, 2, 3) is False

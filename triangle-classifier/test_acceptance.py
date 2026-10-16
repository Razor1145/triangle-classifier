"""Customer-oriented end-to-end acceptance scenario (do not use Copilot)."""
from triangle import classify_triangle


def test_stained_glass_order_classification():
    # An unbuildable pane is rejected without an exception.
    assert classify_triangle(2, 3, 5) == "Invalid"
    # A normal buildable pane receives a shape label.
    assert classify_triangle(5, 5, 6) == "Isosceles"
    # A right-angle pane is marked for reinforced corners.
    assert classify_triangle(3, 4, 5) == "Right Scalene"

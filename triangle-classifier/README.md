# Triangle Classifier

A Python program that checks whether three lengths form a triangle, identifies its side-based shape, and flags right-angle triangles for a stained-glass studio.

## Running the tests

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

## Equivalence classes and boundaries

| Input class | Example | Expected output |
| --- | --- | --- |
| Zero or negative side | (0, 4, 5), (-1, 4, 5) | Invalid |
| Triangle inequality fails | (1, 2, 4) | Invalid |
| Degenerate boundary (two sides sum to third) | (1, 2, 3) | Invalid |
| Equilateral | (3, 3, 3) | Equilateral |
| Isosceles | (5, 5, 6) | Isosceles |
| Scalene | (4, 5, 6) | Scalene |
| Right scalene | (3, 4, 5) | Right Scalene |
| Right isosceles, non-integer hypotenuse | (5, 5, 5√2) | Right Isosceles |

A triangle must have three positive sides, and the sum of any two must be strictly greater than the third. Equality is the degenerate boundary and is invalid.

An equilateral triangle has three 60-degree angles because its angles are equal and sum to 180 degrees. It therefore cannot contain a 90-degree angle.

## Copilot Review Log

**Complete this log only after using GitHub Copilot autocomplete in VS Code and inspecting its actual suggestions. Do not report the example below as an event unless it really occurred.**

| Test | Copilot-suggested? | Kept / edited / rejected | Why |
| --- | --- | --- | --- |
| test_right_triangle | [Yes/No] | [Kept/Edited/Rejected] | [Describe the actual suggestion and verification] |
| test_degenerate_boundary | [Yes/No] | [Kept/Edited/Rejected] | [Describe the actual suggestion and verification] |
| test_right_triangle_noninteger | [Yes/No] | [Kept/Edited/Rejected] | [Describe the actual suggestion and verification] |

Example of a mistake to watch for: a suggestion using exact floating-point equality (`==`) for the Pythagorean theorem should be rejected or edited to use `math.isclose`. Record a real mistake that you caught.

## Customer acceptance criteria

1. For any entered lengths with a nonpositive side or a failed strict triangle inequality, classification returns `Invalid` without raising an exception.
2. For a valid triangle, classification returns its correct side-based category: `Equilateral`, `Isosceles`, or `Scalene`.
3. For a valid right triangle, classification begins with `Right ` to identify a piece needing reinforced corners.

The acceptance test checks one invalid order, one valid non-right order, and one valid right-angle order in a single customer-oriented scenario.

## AI-use disclosure

ChatGPT was used to draft the triangle implementation, example pytest tests, acceptance-test scenario, and README. **The unit-test examples are not evidence of Copilot use.** Before submission, use GitHub Copilot autocomplete to draft/review the unit tests, record actual accepted/edited/rejected suggestions above, and independently write and verify the acceptance test without Copilot, as required by the assignment. Verify all outputs against the assignment specification and run `python -m pytest -v`.

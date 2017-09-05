"""
TEST CASES:


Test.assert_equals(calc(""), 0, "Should work with empty string")
Test.assert_equals(calc("1 2 3"), 3, "Should parse numbers")
Test.assert_equals(calc("1 2 3.5"), 3.5, "Should parse float numbers")
Test.assert_equals(calc("1 3 +"), 4, "Should support addition")
Test.assert_equals(calc("1 3 *"), 3, "Should support multiplication")
Test.assert_equals(calc("1 3 -"), -2, "Should support subtraction")
Test.assert_equals(calc("4 2 /"), 2, "Should support division")
"""
import pytest


CALC_TEST_CASES = [
    ((""), 0),
    (("1 2 3"), 3),
    (("1 2 3.5"), 3.5),
    (("1 3 +"), 4),
    (("1 3 *"), 3),
    (("1 3 -"), -2),
    (("4 2 /"), 2),
    (("5 1 2 + 4 * + 3 -"), 14),
]

OP_TEST_CASES = [
    ((1, 2, '+'), 3),
    ((1, 2, '-'), 1),
    ((1, 2, '*'), 2),
    ((1, 2, '/'), 2),
    ((2, 3, '/'), 1.5),
]


@pytest.mark.parametrize('test_input, test_output', CALC_TEST_CASES)
def test_calc(test_input, test_output):
    from reverse_polish_notation_calculator import calc
    assert calc(test_input) == test_output


@pytest.mark.parametrize('test_input, test_output', OP_TEST_CASES)
def test__operation(test_input, test_output):
    from reverse_polish_notation_calculator import _operation
    assert _operation(*test_input) == test_output

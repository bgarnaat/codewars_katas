"""
TEST CASES:


# tests for mystery()
test.assert_equals(mystery(6), 5, "mystery(6) ")
test.assert_equals(mystery(9), 13, "mystery(9) ")
test.assert_equals(mystery(19), 26, "mystery(19) ")

# tests for mystery_inv()
test.assert_equals(mystery_inv(5), 6, "mystery_inv(5)")
test.assert_equals(mystery_inv(13), 9, "mystery_inv(13)")
test.assert_equals(mystery_inv(26), 19, "mystery_inv(26)")
"""
import pytest


MYSTERY_TEST_CASES = [
    (6, 5),
    (9, 13),
    (19, 26),
]

MYSTERY_INV_TEST_CASES = [
    (5, 6),
    (13, 9),
    (26, 19),
]


@pytest.mark.parametrize('test_input, test_output', MYSTERY_TEST_CASES)
def test_mystery(test_input, test_output):
    from mystery_function import mystery
    assert mystery(test_input) == test_output


@pytest.mark.parametrize('test_input, test_output', MYSTERY_INV_TEST_CASES)
def test_mystery_inv(test_input, test_output):
    from mystery_function import mystery_inv
    assert mystery_inv(test_input) == test_output

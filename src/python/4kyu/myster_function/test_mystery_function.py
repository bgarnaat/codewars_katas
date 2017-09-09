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
    (0, 0),
    (1, 1),
    (2, 3),
    (3, 2),
    (4, 6),
    (5, 7),
    (6, 5),
    (7, 4),
    (9, 13),
    (19, 26),
    (63, 32),
    (255, 128),
]

MYSTERY_INV_TEST_CASES = [
    (0, 0),
    (1, 1),
    (2, 3),
    (3, 2),
    (4, 7),
    (5, 6),
    (6, 4),
    (7, 5),
    (13, 9),
    (26, 19),
    (32, 63),
    (128, 255),
]


# tests for mystery
# test.assert_equals(mystery(6), 0, "mystery(6) ")

# tests for mystery_inv



@pytest.mark.parametrize('test_input, test_output', MYSTERY_TEST_CASES)
def test_mystery(test_input, test_output):
    from mystery_function import mystery
    assert mystery(test_input) == test_output


@pytest.mark.parametrize('test_input, test_output', MYSTERY_INV_TEST_CASES)
def test_mystery_inv(test_input, test_output):
    from mystery_function import mystery_inv
    assert mystery_inv(test_input) == test_output

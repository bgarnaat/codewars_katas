import pytest
"""
TEST CASES:

test.assert_equals(find_outlier([2,6,8,10,3]), 3)
"""

TEST_CASES = [
    ([2, 6, 8, 10, 3], 3)
]


@pytest.mark.parametrize('test_input, test_output', TEST_CASES)
def test_find_the_parity_outlier(test_input, test_output):
    from find_the_parity_outlier import find_outlier
    assert find_outlier(test_input) == test_output

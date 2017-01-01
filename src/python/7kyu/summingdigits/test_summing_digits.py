import pytest
"""
TEST CASES:

test.assert_equals(sumDigits(10), 1)
test.assert_equals(sumDigits(99), 18)
test.assert_equals(sumDigits(-32), 5)
"""


TEST_LIST = [
    [10, 1],
    [99, 18],
    [-32, 5],
]


@pytest.mark.parametrize('input, output', TEST_LIST)
def test_sumDigits(input, output):
    from summing_digits import sumDigits
    assert sumDigits(input) == output

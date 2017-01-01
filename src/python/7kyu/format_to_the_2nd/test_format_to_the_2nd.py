import pytest
"""
TEST CASES:


test.describe('Basic Tests')
test.assert_equals(print_nums(), '')
test.assert_equals(print_nums(2), '2')
test.assert_equals(print_nums(1, 12, 34), '01\n12\n34')
test.assert_equals(print_nums(1009, 2), '1009\n0002')
"""


# THESE TESTS NEED TO BE WRITTEN WITHOUT ().  also, try to pass allll the params through...
TEST_LIST = [
    [(), ''],
    [(2), '2'],
    [(1, 12, 34), '01\n12\n34'],
    [(1009, 2), '1009\n0002'],
]


@pytest.mark.parametrize('input, output')
def test_print_nums(input, output):
    from format_to_the_2nd import test_nums
    assert test_nums(input) == output

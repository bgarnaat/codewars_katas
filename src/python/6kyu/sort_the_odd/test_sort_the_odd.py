import pytest
"""
TEST CASES:

Test.assert_equals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
Test.assert_equals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
Test.assert_equals(sort_array([]),[])
"""


TEST_LIST = [
    [[5, 3, 2, 8, 1, 4], [1, 3, 2, 8, 5, 4]],
    [[5, 3, 1, 8, 0], [1, 3, 5, 8, 0]],
    [[], []],
]


@pytest.mark.parametrize('input, output', TEST_LIST)
def test_sort_array(input, output):
    from sort_the_odd import sort_array
    assert sort_array(input) == output

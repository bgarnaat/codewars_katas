import pytest
"""
TEST CASES:

test.assert_equals(last([1,2,3,4,5]), 5)
test.assert_equals(last("abcde"), "e")
test.assert_equals(last(1, "b", 3, "d", 5), 5)
"""

TEST_LIST = [
    [[1, 2, 3, 4, 5], 5],
    ["abcde", "e"],
]


@pytest.mark.parametrize('input, output', TEST_LIST)
def test_last(input, output):
    from last import last
    assert last(input) == output


def test_last_overload():
    from last import last
    assert last(1, "b", 3, "d", 5) == 5

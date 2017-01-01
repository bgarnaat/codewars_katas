import pytest
"""
TEST CASES:

test.describe("Basic Tests")

tests = [
    #[input, [expected]],
    ["Hi!", "Hi"],
    ["Hi!!!","Hi!!"],
    ["!Hi", "!Hi"],
    ["!Hi!", "!Hi"],
    ["Hi! Hi!", "Hi! Hi"],
    ["Hi", "Hi"],
]

for inp, exp in tests:
    test.assert_equals(remove(inp), exp)
"""


TEST_LIST = [
    ["Hi!", "Hi"],
    ["Hi!!!", "Hi!!"],
    ["!Hi", "!Hi"],
    ["!Hi!", "!Hi"],
    ["Hi! Hi!", "Hi! Hi"],
    ["Hi", "Hi"],
]


@pytest.mark.parametrize('test_input, test_output', TEST_LIST)
def test_remove(test_input, test_output):
    from remove_exclamation import remove
    assert remove(test_input) == test_output

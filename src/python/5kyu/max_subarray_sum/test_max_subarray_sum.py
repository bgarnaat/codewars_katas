"""
TEST CASES:


test.describe("Tests")
test.it('should work on an empty array')
test.assert_equals(maxSequence([]), 0)
test.it('should work on the example')
test.assert_equals(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
"""
import pytest


TEST_CASES = [
    ([], 0),
    ([1], 1),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
]


@pytest.mark.parametrize("test_input, test_output", TEST_CASES)
def test_max_sequence(test_input, test_output):
    from max_subarray_sum import max_sequence
    assert max_sequence(test_input) == test_output

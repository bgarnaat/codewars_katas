import pytest

"""
TEST CASES:

Test.describe("Basic tests")
Test.assert_equals(string_to_array("Robin Singh"), ["Robin", "Singh"])
Test.assert_equals(string_to_array("CodeWars"), ["CodeWars"])
Test.assert_equals(string_to_array("I love arrays they are my favorite"), ["I", "love", "arrays", "they", "are", "my", "favorite"])
Test.assert_equals(string_to_array("1 2 3"), ["1", "2", "3"])
Test.assert_equals(string_to_array(""), [""])
"""

TEST_LIST = [
    [("Robin Singh"), ["Robin", "Singh"]],
    [("CodeWars"), ["CodeWars"]],
    [("I love arrays they are my favorite"), ["I", "love", "arrays", "they", "are", "my", "favorite"]],
    [("1 2 3"), ["1", "2", "3"]],
    [(""), [""]],
]


@pytest.mark.parametrize('input, output', TEST_LIST)
def test_string_to_array(input, output):
    from string_to_array import string_to_array
    assert string_to_array(input) == output

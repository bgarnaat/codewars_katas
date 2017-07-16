"""
TEST CASES:


Test.describe("Basic tests")
Test.assert_equals(average_string("zero nine five two"), "four")
Test.assert_equals(average_string("four six two three"), "three")
Test.assert_equals(average_string("one two three four five"), "three")
Test.assert_equals(average_string("five four"), "four")
Test.assert_equals(average_string("zero zero zero zero zero"), "zero")
Test.assert_equals(average_string("one one eight one"), "two")
Test.assert_equals(average_string("one"), "one")
Test.assert_equals(average_string(""), "n/a")
Test.assert_equals(average_string("ten"), "n/a")
Test.assert_equals(average_string("pippi"), "n/a")
"""


import pytest


TEST_CASES = [
    ("zero nine five two", "four"),
    ("four six two three", "three"),
    ("one two three four five", "three"),
    ("five four", "four"),
    ("zero zero zero zero zero", "zero"),
    ("one one eight one", "two"),
    ("one", "one"),
    ("", "n/a"),
    ("ten", "n/a"),
    ("pippi", "n/a"),
]


@pytest.mark.parametrize('test_input, test_output', TEST_CASES)
def test_string_average(test_input, test_output):
    from string_average import average_string
    assert average_string(test_input) == test_output

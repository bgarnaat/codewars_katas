"""
TEST CASES:


test.assert_equals(reverseWords("hello world!"), "world! hello")
"""
import pytest


TEST_CASES = [
    ('hello world!', 'world! hello'),
    ('long string of words', 'words of string long'),
    ('word', 'word'),
]


@pytest.mark.parametrize('test_input, test_output', TEST_CASES)
def test_reverse_words(test_input, test_output):
    from reversed_words import reverse_words
    assert reverse_words(test_input) == test_output

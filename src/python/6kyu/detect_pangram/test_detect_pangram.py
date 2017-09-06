"""
TEST CASES:


pangram = "The quick, brown fox jumps over the lazy dog!"
Test.assert_equals(is_pangram(pangram), True)
"""
import pytest


TEST_CASES = [
    ('', False),
    ('0', False),
    ('A', False),
    ('The quick, brown fox jumps over the lazy dog!', True),
    ('he quick, brown fox jumps over the lazy dog!', True),
]


@pytest.mark.parametrize('test_input, test_output', TEST_CASES)
def test_is_pangram(test_input, test_output):
    from detect_pangram import is_pangram
    assert is_pangram(test_input) == test_output

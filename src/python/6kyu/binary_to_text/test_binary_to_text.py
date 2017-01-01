import pytest
"""
TEST CASES:

Test.assert_equals(binary_to_string('0100100001100101011011000110110001101111'), 'Hello')
Test.assert_equals(binary_to_string('00110001001100000011000100110001'), '1011')
"""


TEST_LIST = [
    ('0100100001100101011011000110110001101111', 'Hello'),
    ('00110001001100000011000100110001', '1011'),
]


@pytest.mark.parametrize('test_input, test__output', TEST_LIST)
def test_binary_to_string(test_input, test__output):
    from binary_to_text import binary_to_string
    assert binary_to_string(test_input) == test__output

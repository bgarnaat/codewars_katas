import pytest
"""
TEST CASES:

Test.assert_equals(pattern(1),"1")
Test.assert_equals(pattern(4),"   1   \n  121  \n 12321 \n1234321")
Test.assert_equals(pattern(0),"")
"""


TEST_LIST = [
    [1, '1'],
    [4, '   1   \n  121  \n 12321 \n1234321'],
    [0, ''],
]


@pytest.mark.parametrize('input, output', TEST_LIST)
def test_pattern(input, output):
    from number_pyramid import pattern
    assert pattern(input) == output

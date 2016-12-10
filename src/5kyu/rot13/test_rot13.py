import pytest
"""
TEST CASEs:

test.assert_equals(rot13("test"),"grfg")
test.assert_equals(rot13("Test"),"Grfg")
"""


TEST_LIST = [
    ['test', 'grfg'],
    ['Test', 'Grfg'],
]


@pytest.mark.parametrize('input, output', TEST_LIST)
def test_rot13(input, output):
    from rot13 import rot13
    assert rot13(input) == output

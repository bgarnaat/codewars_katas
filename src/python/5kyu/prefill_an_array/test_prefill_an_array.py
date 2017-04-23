"""
TEST CASES:

Test.assert_equals(prefill(3, 1),  [1, 1, 1])
Test.assert_equals(prefill(2, 'abc'),  ['abc', 'abc'])
Test.assert_equals(prefill('1', 1),  [1])
Test.assert_equals(prefill(3,  prefill(2, '2d')),  [['2d', '2d'], ['2d', '2d'], ['2d', '2d']])

try:
    prefill('xyz',  1)
except Exception as err:
    value=err
    Test.assert_equals(type(err),  TypeError, "prefill did not throw the correct error")
    Test.assert_equals(str(err),  "xyz is invalid", "prefill did not throw the correct error")
"""
import pytest
from prefill_an_array import prefill


TEST_CASES = [
    ((3, 1),  [1, 1, 1]),
    ((2, 'abc'),  ['abc', 'abc']),
    (('1', 1),  [1]),
    ((3,  prefill(2, '2d')),  [['2d', '2d'], ['2d', '2d'], ['2d', '2d']]),
]


@pytest.mark.parametrize("test_input, test_output", TEST_CASES)
def test_prefill(test_input, test_output):
    print(test_input)
    assert prefill(*test_input) == test_output


def test_TypeError():
    with pytest.raises(TypeError):
        prefill('xyz', 1)


def test_error_message():
    with pytest.raises(TypeError):
        prefill('xyz', 1) == 'xyz is invalid'

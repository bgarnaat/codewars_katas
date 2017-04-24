"""
TEST CASES:


Test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
"""


import pytest


TEST_CASES = [
    (("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
]


@pytest.mark.parametrize('test_input, test_output', TEST_CASES)
def test_order(test_input, test_output):
    from your_order_please import order
    assert order(test_input) == test_output

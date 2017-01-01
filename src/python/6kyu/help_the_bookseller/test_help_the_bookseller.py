import pytest
"""
TEST CASES:


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
res = "(A : 200) - (B : 1140)"
test.assert_equals(stock_list(b, c), res)
"""


TEST_LIST = [

]


@pytest.mark.parametrize('test_input, test_output', TEST_LIST)
def test_function(test_input, test_output):
    from help_the_bookseller import stock_list
    assert stock_list(test_input) == test_output

"""
TEST CASES:


Test.describe("Example test casess")
Test.it("Fixed tests")

Test.assert_equals(last_digit(4, 1), 4)
Test.assert_equals(last_digit(4, 2), 6)
Test.assert_equals(last_digit(9, 7), 9)
Test.assert_equals(last_digit(10, 1000000000), 0)
Test.assert_equals(last_digit(38710248912497124917933333333284108412048102948908149081409204712406, 226628148126342643123641923461846128214626), 6)
Test.assert_equals(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7)

"""
import pytest


TEST_CASES = [
    ((4, 1), 4),
    ((4, 2), 6),
    ((9, 7), 9),
    ((10, 1000000000), 0),
    ((38710248912497124917933333333284108412048102948908149081409204712406, 226628148126342643123641923461846128214626), 6),
    ((3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7),
]


@pytest.mark.parametrize('test_input, test_output', TEST_CASES)
def test_last_digit(test_input, test_output):
    from last_digit_large_number import last_digit
    assert last_digit(*test_input) == test_output

import pytest
"""
TEST CASES:


Test.describe("calculate_years")

Test.it("works for some examples")
Test.assert_equals(calculate_years(1000, 0.05, 0.18, 1100), 3)
Test.assert_equals(calculate_years(1000,0.01625,0.18,1200), 14)
Test.assert_equals(calculate_years(1000,0.05,0.18,1000), 0)
"""

TEST_LIST = [
    [1000, 0.05, 0.18, 1100, 3],
    [1000, 0.01625, 0.18, 1200, 14],
    [1000, 0.05, 0.18, 1000, 0],
]


@pytest.mark.parametrize('principal, interest, tax, desired, output', TEST_LIST)
def test_calculate_years(principal, interest, tax, desired, output):
    from moneymoneymoney import calculate_years
    assert calculate_years(principal, interest, tax, desired) == output

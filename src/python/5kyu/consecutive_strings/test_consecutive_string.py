import pytest
"""
TEST CASES:

def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe("longest_consec")
Test.it("Basic tests")
testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
testing(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
testing(longest_consec([], 3), "")
testing(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
testing(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
"""


TEST_CASES = [
    ((["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta"),
    ((["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh"),
    (([], 3), ""),
    ((["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"),
    ((["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu"),
    ((["zone", "abigail", "theta", "form", "libe", "zas"], -2), ""),
    ((["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz"),
    ((["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15), ""),
    ((["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0), ""),
]


@pytest.mark.parametrize('test_input, test_output', TEST_CASES)
def test_longest_consec(test_input, test_output):
    from consecutive_strings import longest_consec
    assert longest_consec(*test_input) == test_output

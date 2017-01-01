import pytest
"""
TEST CASES:

def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe("partlist")
Test.it("Basic tests")
testing(partlist(["I", "wish", "I", "hadn't", "come"]),
    [("I", "wish I hadn't come"), ("I wish", "I hadn't come"), ("I wish I", "hadn't come"), ("I wish I hadn't", "come")])
testing(partlist(["cdIw", "tzIy", "xDu", "rThG"]),
    [("cdIw", "tzIy xDu rThG"), ("cdIw tzIy", "xDu rThG"), ("cdIw tzIy xDu", "rThG")])
testing(partlist(["vJQ", "anj", "mQDq", "sOZ"]),
    [("vJQ", "anj mQDq sOZ"), ("vJQ anj", "mQDq sOZ"), ("vJQ anj mQDq", "sOZ")])
"""

TEST_LIST = [
    (["I", "wish", "I", "hadn't", "come"], [("I", "wish I hadn't come"), ("I wish", "I hadn't come"), ("I wish I", "hadn't come"), ("I wish I hadn't", "come")]),
    (["cdIw", "tzIy", "xDu", "rThG"], [("cdIw", "tzIy xDu rThG"), ("cdIw tzIy", "xDu rThG"), ("cdIw tzIy xDu", "rThG")]),
    (["vJQ", "anj", "mQDq", "sOZ"], [("vJQ", "anj mQDq sOZ"), ("vJQ anj", "mQDq sOZ"), ("vJQ anj mQDq", "sOZ")]),
]


@pytest.mark.parametrize('test_input, test_output', TEST_LIST)
def test_partlist(test_input, test_output):
    from parts_of_a_list import partlist
    assert partlist(test_input) == test_output

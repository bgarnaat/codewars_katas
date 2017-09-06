"""
TEST CASES:

Test.describe("Basic tests")
Test.assert_equals(de_nico("crazy", "cseerntiofarmit on  "), "secretinformation")
Test.assert_equals(de_nico("crazy", "cseerntiofarmit on"), "secretinformation")
Test.assert_equals(de_nico("abc", "abcd"), "abcd")
Test.assert_equals(de_nico("ba", "2143658709"), "1234567890")
Test.assert_equals(de_nico("a", "message"), "message")
Test.assert_equals(de_nico("key", "eky"), "key")
"""
import pytest


TEST_CASES = [
    (("crazy", "cseerntiofarmit on  "), "secretinformation"),
    (("crazy", "cseerntiofarmit on"), "secretinformation"),
    (("abc", "abcd"), "abcd"),
    (("ba", "2143658709"), "1234567890"),
    (("a", "message"), "message"),
    (("key", "eky"), "key"),
]


@pytest.mark.parametrize('test_input, test_output', TEST_CASES)
def test_de_nico(test_input, test_output):
    from basic_DeNico import de_nico
    assert de_nico(*test_input) == test_output

"""
TEST CASES:


Test.describe("Basic Tests")
Test.expect(ip_to_int32("128.114.17.104") == 2154959208, "wrong integer for ip: 128.114.17.104")
Test.expect(ip_to_int32("0.0.0.0") == 0, "wrong integer for ip: 0.0.0.0")
Test.expect(ip_to_int32("128.32.10.1") == 2149583361, "wrong integer for ip: 128.32.10.1")
"""
import pytest


TEST_CASES = [
    ("128.114.17.104", 2154959208),
    ("0.0.0.0", 0),
    ("128.32.10.1", 2149583361),
]


@pytest.mark.parametrize('test_input, test_output', TEST_CASES)
def test_ip_to_int32(test_input, test_output):
    from ipv4_to_int32 import ip_to_int32
    assert ip_to_int32(test_input) == test_output

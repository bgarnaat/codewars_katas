"""
TEST CASES:


s="Look mom, no hands"
h="4c6f6f6b206d6f6d2c206e6f2068616e6473"

Test.assert_equals(Converter.to_hex(s),h)
Test.assert_equals(Converter.to_ascii(h),s)
Test.assert_equals(Converter.to_hex(Converter.to_ascii(h)),h)
Test.assert_equals(Converter.to_ascii(Converter.to_hex(s)),s)
"""


S = "Look mom, no hands"
H = "4c6f6f6b206d6f6d2c206e6f2068616e6473"


TEST_CASES = [
    (S, H),
    (H, S),
    (H, H),
    (S, S),
]


def test_to_hex():
    from ascii_hex_converter import Converter
    assert Converter.to_hex(S) == H


def test_to_ascii():
    from ascii_hex_converter import Converter
    assert Converter.to_ascii(H) == S


def test_to_hex_to_ascii():
    from ascii_hex_converter import Converter
    assert Converter.to_ascii(Converter.to_hex(S)) == S


def test_to_ascii_to_hex():
    from ascii_hex_converter import Converter
    assert Converter.to_hex(Converter.to_ascii(H)) == H

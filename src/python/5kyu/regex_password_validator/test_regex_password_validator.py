"""
TEST CASES:


from re import search
Test.describe("Basic tests")
Test.assert_equals(bool(search(regex, 'fjd3IR9')), True)
Test.assert_equals(bool(search(regex, 'ghdfj32')), False)
Test.assert_equals(bool(search(regex, 'DSJKHD23')), False)
Test.assert_equals(bool(search(regex, 'dsF43')), False)
Test.assert_equals(bool(search(regex, '4fdg5Fj3')), True)
Test.assert_equals(bool(search(regex, 'DHSJdhjsU')), False)
Test.assert_equals(bool(search(regex, 'fjd3IR9.;')), False)
Test.assert_equals(bool(search(regex, 'fjd3  IR9')), False)
Test.assert_equals(bool(search(regex, 'djI38D55')), True)
Test.assert_equals(bool(search(regex, 'a2.d412')), False)
Test.assert_equals(bool(search(regex, 'JHD5FJ53')), False)
Test.assert_equals(bool(search(regex, '!fdjn345')), False)
Test.assert_equals(bool(search(regex, 'jfkdfj3j')), False)
Test.assert_equals(bool(search(regex, '123')), False)
Test.assert_equals(bool(search(regex, 'abc')), False)
Test.assert_equals(bool(search(regex, '123abcABC')), True)
Test.assert_equals(bool(search(regex, 'ABC123abc')), True)
Test.assert_equals(bool(search(regex, 'Password123')), True)
"""


import pytest


TEST_CASES = [
    ('fjd3IR9', True),
    ('ghdfj32', False),
    ('DSJKHD23', False),
    ('dsF43', False),
    ('4fdg5Fj3', True),
    ('DHSJdhjsU', False),
    ('fjd3IR9.;', False),
    ('fjd3  IR9', False),
    ('djI38D55', True),
    ('a2.d412', False),
    ('JHD5FJ53', False),
    ('!fdjn345', False),
    ('jfkdfj3j', False),
    ('123', False),
    ('abc', False),
    ('123abcABC', True),
    ('ABC123abc', True),
    ('Password123', True),
]


@pytest.mark.parametrize('test_input, test_output', TEST_CASES)
def test_re_search(test_input, test_output):
    from regex_password_validator import re_search
    assert re_search(test_input) == test_output

"""
TEST CASES:


Test.assert_equals(list([1,2,3,4,5]).even(), [2,4], "Nope")
Test.assert_equals(list([1,2,3,4,5]).odd(), [1,3,5], "Nope")
Test.assert_equals(list([1,2,3,4,5]).under(4), [1,2,3], "Nope")
Test.assert_equals(list([1,2,3,4,5]).over(4), [5], "Nope")
Test.assert_equals(list([1,2,3,4,5]).over(10), [], "Nope")
Test.assert_equals(list([1,2,3,4,5]).in_range(1, 3), [1,2,3], "Nope")
Test.assert_equals(list(["a", "b", "c"]).under(10), [], "Nope")
Test.assert_equals(list(["a", "b", "c"]).over(10), [], "Nope")
Test.assert_equals(list([1,2,3,4,5,6,7,8,9,10]).over(10), [], "Nope")
Test.assert_equals(list(list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]).even()).under(5), [2, 4], "Nope")
Test.assert_equals(list(["a", 1, "b", 300, "x", "q", 63, 122, 181, "z", 0.83, 0.11]).even(), [300, 122], "Nope")
"""


def test_even():
    from custom_array_filters import list
    assert list([1, 2, 3, 4, 5]).even() == [2, 4]


def test_odd():
    from custom_array_filters import list
    assert list([1, 2, 3, 4, 5]).odd() == [1, 3, 5]


def test_under():
    from custom_array_filters import list
    assert list([1, 2, 3, 4, 5]).odd() == [1, 3, 5]


def test_over():
    from custom_array_filters import list
    assert list([1, 2, 3, 4, 5]).odd() == [1, 3, 5]


def test_in_range():
    from custom_array_filters import list
    assert list([1, 2, 3, 4, 5]).odd() == [1, 3, 5]

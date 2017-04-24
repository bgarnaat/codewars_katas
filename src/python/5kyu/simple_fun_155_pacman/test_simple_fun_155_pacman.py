"""
TEST CASES:


Test.it("Basic Tests")
Test.assert_equals(pac_man(1,[0, 0],[]),0)
Test.assert_equals(pac_man(2,[0, 0],[]),3)
Test.assert_equals(pac_man(3,[0, 0],[]),8)
Test.assert_equals(pac_man(3,[1, 1],[]),8)
Test.assert_equals(pac_man(2,[0, 0],[[1,1]]),0)
Test.assert_equals(pac_man(3,[2, 0],[[1,1]]),0)
Test.assert_equals(pac_man(3,[2, 0],[[0,2]]),3)
Test.assert_equals(pac_man(10,[4, 6],[[0,2], [5,2], [5,5]]),15)
Test.assert_equals(pac_man(8,[1, 1],[[5,4]]),19)
Test.assert_equals(pac_man(8,[1, 5],[[5,4]]),14)
Test.assert_equals(pac_man(8,[6, 1],[[5,4]]),7)
"""
import pytest


TEST_CASE = [
    ((1, [0, 0], []), 0),
    ((2, [0, 0], []), 3),
    ((3, [0, 0], []), 8),
    ((3, [1, 1], []), 8),
    ((2, [0, 0], [[1, 1]]), 0),
    ((3, [2, 0], [[1, 1]]), 0),
    ((3, [2, 0], [[0, 2]]), 3),
    ((10, [4, 6], [[0, 2], [5, 2], [5, 5]]), 15),
    ((8, [1, 1], [[5, 4]]), 19),
    ((8, [1, 5], [[5, 4]]), 14),
    ((8, [6, 1], [[5, 4]]), 7),
]


@pytest.mark.parametrize('test_input, test_output', TEST_CASE)
def test_pac_man(test_input, test_output):
    from simple_fun_155_pacman import pac_man
    assert pac_man(*test_input) == test_output

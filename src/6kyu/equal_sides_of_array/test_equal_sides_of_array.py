import pytest
"""
Test.assert_equals(find_even_index([1,2,3,4,3,2,1]),3)
Test.assert_equals(find_even_index([1,100,50,-51,1,1]),1,)
Test.assert_equals(find_even_index([1,2,3,4,5,6]),-1)
Test.assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
Test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
Test.assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
Test.assert_equals(find_even_index(range(1,100)),-1)
Test.assert_equals(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
Test.assert_equals(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
Test.assert_equals(find_even_index(range(-100,-1)),-1)
"""


TEST_LIST = [
    [[1, 2, 3, 4, 3, 2, 1], 3],
    [[1, 100, 50, -51, 1, 1], 1, ],
    [[1, 2, 3, 4, 5, 6], -1],
    [[20, 10, 30, 10, 10, 15, 35], 3],
    [[20, 10, -80, 10, 10, 15, 35], 0],
    [[10, -80, 10, 10, 15, 35, 20], 6],
    [range(1, 100), -1],
    [[0, 0, 0, 0, 0], 0],
    [[-1, -2, -3, -4, -3, -2, -1], 3],
    [range(-100, -1), -1],
]


@pytest.mark.paramtrize("test_input, test_output", TEST_LIST)
def test_find_even_index(test_input, test_out):
    from equal_sides_of_array import find_even_index
    assert find_even_index(test_input) == test_input

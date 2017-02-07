import pytest
from tree_to_list import Node


"""
TEST CASE:

Test.assert_equals(tree_to_list(Node(1, [Node(2, [Node(3), Node(4), Node(5)]), Node(3, [Node(7)])])),
[1, 2, 3, 3, 4, 5, 7])
"""


TEST_CASE = [
    (Node(1, [
        Node(2, [
            Node(3),
            Node(4),
            Node(5)
        ]),
        Node(3, [
            Node(7)
        ])
    ]), [1, 2, 3, 3, 4, 5, 7]),
]


@pytest.mark.parametrize('test_input, test_output', TEST_CASE)
def test_tree_to_list(test_input, test_output):
    from tree_to_list import tree_to_list
    assert tree_to_list(test_input) == test_output

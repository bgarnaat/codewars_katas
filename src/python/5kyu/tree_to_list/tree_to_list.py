from collections import deque


"""
Description:

Given root of tree with arbitrary number of children nodes transform data from tree to list. Where data from neighbour nodes in tree located in neighbour position in list.

Example:

       1
      / \
     2   3  -> [1,2,3,4,5,6,7]
    /|\   \
   4 5 6   7
"""


class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes


def tree_to_list(tree_root):
    path = deque([tree_root])
    output = []
    while path:
        output.append(path.popleft())
        if output[-1].child_nodes:
            path.extend(output[-1].child_nodes)
    return [node.data for node in output]


"""
Try this with a recursive solution (using generators).
"""

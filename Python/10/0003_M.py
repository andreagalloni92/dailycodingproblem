#!/usr/bin/python
# coding=utf-8

"""
Problem #3.

This problem was asked by Google.

Given the root to a binary tree, implement `serialize(root)`, which serializes
the tree into a string, and `deserialize(s)`, which deserializesthe string
back into the tree.

For example, given the following Node class:
```
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
The following test should pass:
```
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```
"""

from collections.abc import Iterator


class Node:
    """Node Class."""

    def __init__(self, val, left=None, right=None):
        """Do instantiate the class."""
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        """Return a string representation of the node."""
        return f"<Node: ['{self.val}'] -> L: {self.left} | R: {self.right}>"

    def __str__(self) -> str:
        """Return a string representation of the node."""
        return self.__repr__()

    @staticmethod
    def deserialize(serialized: str) -> str:
        """Deserialize a string to an object."""
        value_list = serialized.split('|')[:-1]
        value_iter = (v for v in value_list)
        return Node._deserialize(value_iter)

    @staticmethod
    def _deserialize(value_list: list) -> object:
        """Deserialize a string to an object [First Approach]."""
        node = Node(value_list.pop(0))

        if value_list[0] != 'None':
            node.left = Node._deserialize(value_list)
        else:
            node.left = None
            value_list.pop(0)

        if value_list[0] != 'None':
            node.right = Node._deserialize(value_list)
        else:
            node.right = None
            value_list.pop(0)

        return node

    @staticmethod
    def _deserialize(value_iter: Iterator) -> object:
        """Deserialize a string to an object [Better Code]."""
        current_value = next(value_iter)

        if current_value == 'None':
            return None
        else:
            node = Node(current_value)
            node.left = Node._deserialize(value_iter)
            node.right = Node._deserialize(value_iter)

        return node

    def serialize(self, cum: str = "") -> str:
        """Serialize an object to string."""
        cum += f'{self.val}|'

        if self.left:
            cum = self.left.serialize(cum)
        else:
            cum += f"{None}|"

        if self.right:
            cum = self.right.serialize(cum)
        else:
            cum += f"{None}|"

        return cum


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    serialized = node.serialize()
    deserialized = Node.deserialize(serialized)
    print(node)
    print(serialized)
    print(deserialized)
    assert Node.deserialize(serialized).left.left.val == 'left.left'

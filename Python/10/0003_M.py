#!/usr/bin/python
# coding=utf-8
from __future__ import annotations

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
from io import StringIO


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
    def deserialize(serialized: str) -> Node:
        """Deserialize a string to a Node."""
        def nodeTokenizer(serialized: str):
            start = 0
            for i, c in enumerate(serialized):
                if c == "|":
                    yield serialized[start:i]
                    start = i + 1
            yield serialized[start:]

        tokens = nodeTokenizer(serialized)
        return Node._deserialize(tokens)

    @staticmethod
    def _deserialize(value_iter: Iterator) -> Node:
        current_value = next(value_iter)
        if current_value == '':
            return None

        node = Node(current_value)
        node.left = Node._deserialize(value_iter)
        node.right = Node._deserialize(value_iter)

        return node

    def serialize(self: Node) -> str:
        """Serialize a Node to string."""
        buf = StringIO()
        self._serialize(buf)
        return buf.getvalue()

    def _serialize(self, buf: StringIO):
        buf.write(f'{self.val}|')
        if self.left:
            self.left._serialize(buf)
        buf.write("|")

        if self.right:
            self.right._serialize(buf)
        buf.write("|")


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    serialized = node.serialize()
    deserialized = Node.deserialize(serialized)
    print(node)
    print(serialized)
    print(deserialized)
    assert Node.deserialize(serialized).left.left.val == 'left.left'

# Daily Coding Problems from [dailycodingproblem.com](https://dailycodingproblem.com)

Solutions by Andrea Galloni, please feel free to push a pull request if you feel like there might be an improvement or any mistake. Thanks in advance. 

**Languages**:
- Python
- ~~Julia~~ ?
- ~~ErLan~~ ?

## Problems:
### \#1 Easy

This problem was recently asked by Google.

Given a list of numbers and a number `k`, return whether any two numbers from the list add up to `k`.

For example, given `[10, 15, 3, 7]` and `k` of `17`, return true since `10 + 7` is `17`.

*Bonus: Can you do this in one pass?*

| [Python](Python/10/0001_E.py) | 

---

### \#2 Hard

Given an array of integers, return a new array such that each element at index `i` of the new array is the product of all the numbers in the original array except the one at `i`.

For example, if our input was `[1, 2, 3, 4, 5]`, the expected output would be `[120, 60, 40, 30, 24]`. If our input was `[3, 2, 1]`, the expected output would be `[2, 3, 6]`.

*Bonus:  what if you can't use division?*

| [Python](Python/10/0002_H.py) | 

---

### \#3 Medium

This problem was asked by Google.

Given the root to a binary tree, implement `serialize(root)`, which serializes the tree into a string, and `deserialize(s)`, which deserializesthe string back into the tree.

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
| [Python](Python/10/0003_M.py) | 

---

### \#4 Hard

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input `[3, 4, -1, 1]` should give `2`. The input `[1, 2, 0]` should
give `3`.

You can modify the input array in-place.

---

### \#5

---

### \#6

---

### \#7

---

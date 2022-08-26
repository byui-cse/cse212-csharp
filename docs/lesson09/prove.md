---
layout: default
title: "W09 Prove: Individual Assignment"
---

# W09 Prove: Individual Assignment
## Instructions
This assignment **must be completed individually** to ensure you are meeting all course outcomes. You should not complete this assignment within a group. If you obtain help from a tutor, the tutor should help you understand principles but should not help you answer these problems. It is an honor code violation to obtain answers for these problems from others including using the internet (i.e. sites that allow students to share their solutions).

As you solve the problems, remember to use the principles learned in the first five lessons of the course:
* Problem Solving Strategy: understand the problem, plan and design the solution, implement the solution, and evaluate the solution.
* Evaluate Performance of Alternative Solutions: use big O to determine the best solution.
* Understanding Code Using Reviews: analyze any code you have been given.
* Finding Defects Using Tests: write tests to determine if your solution is working.
* Articulating Answers for Technical Questions: imagine that you were asked one of these questions during an interview. Remember to ensure that you fully understand the problem and work through different scenarios manually. Consider how the data structure you are using will help you solve the problem. A notebook or a whiteboard can be very useful in this process.

Download [09-prove_trees.py]() to provide all your code solutions for the problems below.

### Problem 1 - Insert Unique Values Only
Update the `_insert` function of the BST class to only allow unique values to be added to the tree (thus creating a sorted set). The `_insert` function is already written to correctly insert values into the BST. However, the current implementation will cause duplicate values to be added to the tree.

### Problem 2 - Contains
Implement the `_contains` function in the BST class. This function is called by the `__contains__` function to search for a value in the BST. The `__contains__` function allows you to write code using the `in` operator like the following:

```python
if 5 in my_bst:
	print("5 is in the bst")
```

If the value is found, the `True` should be returned; otherwise return False. **Hint**: study the `_insert` function. You will need to use recursion to solve this problem.

### Problem 3 - Traverse Backwards
Implement the `_traverse_backward` function in the BST class. This function is called by the `__reversed__` function to loop through the tree backwards (largest value down to the smallest value). The `__reversed__` function allows you to write code using the `reversed` function like the following:

```python	
for value in reversed(my_bst):
	print(value)
```
		
**Hint**: study the `_traverse_forward` function to see how traversing forward is done using the `yield` keyword.

### Problem 4 - Tree Height
Implement the `_get_height` function to get the height of the BST. The height of any tree (or subtree) is defined as one plus the height of either the left subtree or the right subtree (whichever one is bigger). If the BST has only the root node, then this would be 1 plus the maximum height of either subtree which would be 0. Therefore, the height of a BST with only the root node is 1. You will need to use recursion to solve this problem.

### Problem 5 - Create Tree from Sorted List
Implement the `_insert_middle` function (note this function is defined outside the BST class) so that the `create_bst_from_sorted_list` function can successfully create a balanced BST from a sorted list of values. If we looped through the list of sorted values and added them (using the `insert` function in the BST class) one at a time in order, then the resulting BST would look like a linked list. This is not desirable because it results in O(n) instead of O(log n).

To achieve a balanced BST, the `_insert_middle` function should find the middle of the list (or sub-list ... notice that the function takes a `first` and `last` value to keep track of what part of the list you are working with) and add it to the BST. After adding the middle value, then the middle value from the first half and the middle value from the second half should be added. This process (which is recursive) will result in a balanced BST.

The purpose for having the `first` and `last` parameters is so that we do not need to create new sublists when we make recursive calls. Avoid using list slicing to create sublists to solve this problem.

Please note we are not using balanced algorithms like AVL or red/black trees in this problem.

## Submission
You need to submit the following files for this assignment:
* `09-prove_trees.py` - Your solution for all problems with useful comments added to the code.

---
layout: default
title: "W07 Prove: Individual Assignment"
---

# W07 Prove: Individual Assignment
## Instructions
This assignment **must be completed individually** to ensure you are meeting all course outcomes. You should not complete this assignment within a group. If you obtain help from a tutor, the tutor should help you understand principles but should not help you answer these problems. It is an honor code violation to obtain answers for these problems from others including using the internet (i.e. sites that allow students to share their solutions).

As you solve the problems, remember to use the principles learned in the first five lessons of the course:
* Problem Solving Strategy: understand the problem, plan and design the solution, implement the solution, and evaluate the solution.
* Evaluate Performance of Alternative Solutions: use big O to determine the best solution.
* Understanding Code Using Reviews: analyze any code you have been given.
* Finding Defects Using Tests: write tests to determine if your solution is working.
* Articulating Answers for Technical Questions: imagine that you were asked one of these questions during an interview. Remember to ensure that you fully understand the problem and work through different scenarios manually. Consider how the data structure you are using will help you solve the problem. A notebook or a whiteboard can be very useful in this process.

Download [07-prove_linked_list.py]() to provide all your code solutions for the problems below.

### Problem 1 - Insert Tail
Implement the `insert_tail` function in the LinkedList class. The function should add a new node (`LinkedList.Node`) at the end of the linked list. You will need to write code to test your solution. **Hint**: Consider the code already written for `insert_head`.

### Problem 2 - Remove Tail
Implement the `remove_tail` function in the LinkedList class. The function should remove the last node. You will need to write code to test your solution. **Hint**: Consider the code already written for `remove_head`.

### Problem 3 - Remove
Implement the `remove` function in the LinkedList class. The function will need to search for the node (starting at the head) that contains the value and then remove that one node. The function should not continue searching the list once a match has been found and the node has been deleted. You will need to write code to test your solution. **Hint**: You may be able to reuse the `remove_head` and `remove_tail` functions.

### Problem 4 - Replace
Implement the `replace` function in the LinkedList class. The function should search for all nodes that are equal to 'old_value' and then replace the value in those nodes with 'new_value'. Unlike the remove function, this function should continue searching through the list to replace all values that match 'old_value'. You will need to write code to test your solution.

### Problem 5 - Reversed Iterator
The `__iter__` function provides the ability to iterate forward through a LinkedList object using a `for` loop such as `for item in my_linkedlist`. When a `for` loop starts, the `__iter__` function will start. Each time the `yield` statement runs, it will provide a new value to the `for` loop and pause the `__iter__` function. When the `for` loop goes to the next iteration, it will continue running the `__iter__` function again until it gets to the next `yield` which will provide the next value to the `for` loop. You can use the following test code to see how the `__iter__` function works:

```python
for item in my_linkedlist:
	print(item)
```

The `__reversed__` function is used to iterate backwards. Implement the `__reversed__` function in the LinkedList class. **Hint**: Pattern your solution after the `__iter__` function that was already written for you and that was described above. To test the `__reversed__` function, you can use the following code:

```python
for item in reversed(my_linkedlist):
	print(item)

# Another option:

print(list(reversed(my_linkedlist)))
```

## Submission
You need to submit the following files for this assignment:
* `07-prove_linked_lists.py` - Your solution for all problems with useful comments added to the code.

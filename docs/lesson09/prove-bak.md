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

All the files for this assignment will be found in the GitHub classroom ***prove-09*** repository. You will commit changes to your own repository for your submission for this assignment.

#### Step 1: [Accept your assignment repository](prove-classroom-alt){:target="_blank"}

### Problem 1 - Insert Unique Values Only
Update the `Insert` operation to only allow unique values to be added to the tree (thus creating a sorted set). The `Insert` functions are already written to correctly insert values into the tree. However, the current implementation will cause duplicate values to be added to the tree.

### Problem 2 - Contains
Implement the `Contains` function in the Node class. This function is called by the `Contains` function in the BinarySearchTree to search for a value in the tree. If the value is found, `true` should be returned; otherwise return `false`. **Hint**: study the `Insert` function. You will need to use recursion to solve this problem.

### Problem 3 - Traverse Backwards
Implement the `TraverseBackward` function in the BinarySearchTree class. This function is called by the `Reversed` function to loop through the tree backwards (largest value down to the smallest value). The `Reversed` function allows you to write code using the `foreach` syntax like the following:

```csharp	
foreach(var value in myTree.Reversed()) {
	Console.WriteLine(value);
}
```
		
**Hint**: study the `TraverseForward` function to see how traversing forward is done.

### Problem 4 - Tree Height
Implement the `GetHeight` function to get the height of the BinarySearchTree. The height of any tree (or subtree) is defined as one plus the height of either the left subtree or the right subtree (whichever one is bigger). If the tree has only the root node, then this would be 1 plus the maximum height of either subtree which would be 0. Therefore, the height of a tree with only the root node is 1. You will need to use recursion to solve this problem.

### Problem 5 - Create Tree from Sorted List
Implement the `InsertMiddle` function (note this function is defined outside the BinarySearchTree class) so that the `CreateTreeFromSortedList` function can successfully create a balanced tree from a sorted list of values. If we looped through the list of sorted values and added them (using the `Insert` function in the BinarySearchTree class) one at a time in order, then the resulting tree would look like a linked list. This is not desirable because it results in O(n) instead of O(log n).

To achieve a balanced tree, the `InsertMiddle` function should find the middle of the list (or sub-list ... notice that the function takes a `first` and `last` value to keep track of what part of the list you are working with) and add it to the tree. After adding the middle value, then the middle value from the first half and the middle value from the second half should be added. This process (which is recursive) will result in a balanced tree.

The purpose for having the `first` and `last` parameters is so that we do not need to create new sublists when we make recursive calls. Avoid using list slicing to create sublists to solve this problem.

Please note we are not using balanced algorithms like AVL or red/black trees in this problem.

## Submission
You need to submit the following for this assignment:
* Make sure all of your changes are committed and pushed to the `main` branch of your **prove-09-[username]** repository
* Submit a link to your repository in I-Learn

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

All of the files for this assignment will be found in the GitHub classroom ***prove-07*** repository. You will commit changes to your own repository for your submission for this assignment.


### Problem 1 - Insert Tail
Implement the `InsertTail` function in the LinkedList class. The function should add a new node (`Node`) at the end of the linked list. You will need to write code to test your solution. **Hint**: Consider the code already written for `InsertHead`.

### Problem 2 - Remove Tail
Implement the `RemoveTail` function in the LinkedList class. The function should remove the last node. You will need to write code to test your solution. **Hint**: Consider the code already written for `RemoveHead`.

### Problem 3 - Remove
Implement the `Remove` function in the LinkedList class. The function will need to search for the node (starting at the head) that contains the value and then remove that one node. The function should not continue searching the list once a match has been found and the node has been deleted. You will need to write code to test your solution. **Hint**: You may be able to reuse the `RemoveHead` and `RemoveTail` functions.

### Problem 4 - Replace
Implement the `Replace` function in the LinkedList class. The function should search for all nodes that are equal to 'old_value' and then replace the value in those nodes with 'new_value'. Unlike the remove function, this function should continue searching through the list to replace all values that match 'old_value'. You will need to write code to test your solution.

### Problem 5 - Reversed Iterator
The `GetEnumerator` function provides the ability to iterate forward through a LinkedList object using a `foreach` loop such as `foreach (var item in myLinkedList)`. When a `foreach` loop starts, the `GetEnumerator` function will start. Each time the `yield return` statement runs, it will provide a new value to the `foreach` loop and pause the `GetEnumerator` function. When the `foreach` loop goes to the next iteration, it will continue running the `GetEnumerator` function again until it gets to the next `yield return` which will provide the next value to the `foreach` loop. You can use the following test code to see how the `GetEnumerator` function works:

```csharp
foreach(var item in myLinkedList) {
	Console.WriteLine(item);
}
```

The `Reverse` function is used to iterate backwards. Implement the `Reverse` function in the LinkedList class. **Hint**: Pattern your solution after the `GetEnumerator` function that was already written for you and that was described above. To test the `Reverse` function, you can use the following code:

```csharp
foreach(var item in myLinkedList.Reverse()) {
	Console.WriteLine(item);
}
```

## Submission
You need to submit the following for this assignment:
* Make sure all of your changes are committed and pushed to the `main` branch of your **prove-07-[username]** repository
* Submit a link to your repository in I-Learn

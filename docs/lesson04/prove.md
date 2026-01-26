---
layout: default
title: "W04 Prove: Individual Assignment"
---

# W04 Prove: Individual Assignment
## Instructions
This assignment **must be completed individually** to ensure you are meeting all course outcomes. You should not complete this assignment within a group. If you obtain help from a tutor, the tutor should help you understand principles but should not help you answer these problems. It is an honor code violation to obtain answers for these problems from others including using the internet (i.e. sites that allow students to share their solutions).

There is no response document for this assignment. All test cases and results should be placed within the test documentation in the test methods of each test file.

All the files for this assignment will be found in the GitHub classroom ***prove-04*** repository. You will commit changes to your own repository for your submission for this assignment.

#### Step 1: [Create your assignment repository](prove-classroom){:target="_blank"}

#### Step 2: [Accept repository invite to resolve Access Issues](https://github.com/settings/organizations){:target="_blank"}

### Part 1 - Taking Turns Queue
1. Examine the following test code file: `TakingTurnsTests.cs` (Note: Do not read through the referenced code first. Instead, proceed with the instructions below).
2. The `TakingTurnsQueue` class maintains a circular queue of people. When a person is added, they are assigned a number of turns (a value of 0 or fewer means that they have an infinite number of turns). When a person is removed from the queue, they are re-added to the queue if they still have turns left. Here are the detailed requirements (**which can not be changed**):
    1. The AddPerson function shall enqueue a person into the queue.
    2. The GetNextPerson function shall dequeue a person from the queue and display their name.
    3. When a person is dequeued and still has turns left, they shall be enqueued again.
    4. When a person is dequeued and has an infinite number of turns (defined as having number of turns of 0 or less), they shall be enqueued again.
    5. If the queue is empty, then an error message shall be displayed.
3. Test cases are already written for you in the code. Run the tests and find the errors. You should summarize the results of the tests and the errors found within the test case documentation at the end of the code file.
4. Fix the code so that all requirements are implemented correctly. You know that you are done because the test cases will all pass. The tests do not need to be modified.

### Part 2 - Priority Queue
1. Examine the following test code file: `PriorityTests.cs` (Note: Do not read through the referenced code first. Instead, proceed with the instructions below).
2. The `PriorityQueue` class maintains a queue where each value put in the queue also has a priority (higher numbers have a higher priority). When you add to the queue, it goes to the back as expected. When you remove from the queue, the highest priority item is removed. If there are multiple values with the same high priority, then the first one (following the FIFO strategy) is removed first. Here are the detailed requirements (**which can not be changed**):
    1. The Enqueue function shall add an item (which contains both data and priority) to the back of the queue.
    2. The Dequeue function shall remove the item with the highest priority and return its value.
    3. If there are more than one item with the highest priority, then the item closest to the front of the queue will be removed and its value returned.
    4. If the queue is empty, then an error message will be displayed.
3. Write your own test cases based on these requirements within the test case documentation in `PriorityTests.cs`. Ensure that your tests cover all the software requirements. You will probably need to add more tests the initial code provides.
4. Run your test cases and find the errors. If your tests were not sufficient, you might not find all the errors in the code. You should summarize the results of the tests and the errors found within the test case documentation at the end of each test.
5. Fix the code so that all requirements are implemented correctly. You know that you are done because the test cases will all pass (assuming your test cases were sufficient).

## Submission
You need to submit the following for this assignment:
* Make sure all of your changes are committed and pushed to the `main` branch of your **prove-04-[username]** repository
* Submit a link to your repository in I-Learn

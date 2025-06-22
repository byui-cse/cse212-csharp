---
layout: default
title: "W10 Prove: Individual Assignment"
---

# W10 Prove: Individual Assignment
## Instructions
This assignment **must be completed individually** to ensure you are meeting all course outcomes. You should not complete this assignment within a group. If you obtain help from a tutor, the tutor should help you understand principles but should not help you answer these problems. It is an honor code violation to obtain answers for these problems from others including using the internet (i.e. sites that allow students to share their solutions).

As you solve the problems, remember to use the principles learned in the first five lessons of the course:
* Problem Solving Strategy: understand the problem, plan and design the solution, implement the solution, and evaluate the solution.
* Evaluate Performance of Alternative Solutions: use big O to determine the best solution.
* Understanding Code Using Reviews: analyze any code you have been given.
* Finding Defects Using Tests: write tests to determine if your solution is working.
* Articulating Answers for Technical Questions: imagine that you were asked one of these questions during an interview. Remember to ensure that you fully understand the problem and work through different scenarios manually. Consider how the data structure you are using will help you solve the problem. A notebook or a whiteboard can be very useful in this process.

All the files for this assignment will be found in the GitHub classroom ***prove-09*** repository. You will commit changes to your own repository for your submission for this assignment.

#### Step 1: [Accept your assignment repository](prove-classroom-heap){:target="_blank"}

### Problem 1 - Using a heap to build a priority queue
Look at the `PriorityQueue` class. Using the pattern found in the `MinHeap` class, make the `Enqueue` and `Dequeue` functions work using a heap rather than loops. You may need to modify the `PriorityItem` class. You will also need to add additional tests in `PriorityTests.cs` to verify that your heap-based implementation works properly. Once you have made all your changes so that it uses a heap, remove the `TestPriorityQueueForHeapImplementation` method.

### Problem 2 - Phone Switch with 911 Priority
The phone switch has been working so far using a list to implement the priority queue. Your company has just won a contract for providing phone switching beyond your small town of 900 people to being the phone switch used across the states of Washington, Idaho, and Oregon. You are tasked with updating the working phone switch code to handle that new load using the heap-based priority queue. Check out `MinHeap.cs` for an existing implementation and modify your phone switch to use a heap. The existing tests are there to make sure you don't break the current functionality. Once you have made all your changes so that it uses a heap, remove the `TestPhoneSwitchForHeapImplementation` method.

## Submission
You need to submit the following for this assignment:
* Make sure all of your changes are committed and pushed to the `main` branch of your **prove-10-[username]** repository
* Submit a link to your repository in I-Learn

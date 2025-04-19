---
layout: default
title: "W05 Prove: Individual Assignment"
---

# W05 Prove: Individual Assignment
## Instructions
This assignment **must be completed individually** to ensure you are meeting all course outcomes. You should not complete this assignment within a group. If you obtain help from a tutor, the tutor should help you understand principles but should not help you answer these problems. It is an honor code violation to obtain answers for these problems from others including using the internet (i.e. sites that allow students to share their solutions).

All the code files for this assignment will be found in the GitHub classroom ***prove-05*** repository - including the 05-prove-response.md. You will commit changes to your own repository for your submission for this assignment.

#### Step 1: [Accept your assignment repository](prove-classroom){:target="_blank"}

### Part 1 - Response Document
Examine the `05-prove-response.md` document to provide your answers to questions asked in the steps below. You will commit this document back to your repository for submission.

### Part 2 - Set Operations
1. Assume you have been asked in an interview to describe how you would write a function to find the intersection of two sets and a function to find the union of two sets. An intersection will return a set containing items that are common between the two sets. A union will return a set containing all items from both sets.
2. Write down an answer to the question in your response document as if you were giving a verbal response with an emphasis on the purposes, behavior, and/or performance of a set. Your response should be no more than a 30-second answer if spoken out loud.
3. Open the following code file: `SetOperations.cs`
4. Implement both the `Intersection` and the `Union` functions in the code file provided only using the basic set functions:
    * `Add`
    * `Remove`
    * `Contains` (checking membership)
    * Iterate through the set
5. Do not use the built-in functions for C# Collections such as `IntersectWith`, `UnionWith`, etc.
6. Run the tests to verify that `Intersection` and `Union` work. You should not modify the tests.

### Part 3 - Find Pairs
1. Assume you have been asked in an interview to describe how you would find symmetric pairs of two-letter words in a list in O(n) time using a set. You should assume that the words are lower case, two characters long, and contain no duplicates. As an example, if the word list was `[am, at, ma, if, fi]` then the result would be `am & ma, if & fi`. The order of the results would not matter. Note that the `at` would not be included because `ta` was not in the list. As a special case, if the letters are the same (example: `aa`) then it would not match anything else (remember the assumption above that there were no duplicates) and therefore should not be included with the results.
2. Write down an answer to the question in your response document as if you were giving a verbal response with an emphasis on the purpose, behavior, and/or performance of a set. Your response should be no more than a 30-second answer if spoken out loud.
3. Open the following code file: `SetOperations.cs`
4. Implement the `FindPairs` function with **O(n)** time using sets in the code file provided above.
5. Run the tests to verify that `FindPairs` works. You should not modify the tests.


## Submission
You need to submit the following for this assignment:
* Make sure all of your changes are committed and pushed to the `main` branch of your **prove-05-[username]** repository
* Submit a link to your repository in I-Learn

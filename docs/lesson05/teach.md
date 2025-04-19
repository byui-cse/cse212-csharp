---
layout: default
title: "W05 Teach: Group Practice"
---

# W05 Teach: Group Practice

## Instructions

These problems should be completed and discussed as a group. Answers are provided below.

All the files for this assignment will be found in the GitHub classroom ***teach-05*** repository.

#### Step 1: [Accept your assignment repository](teach-classroom){:target="_blank"}

### Problem 1 - Unique Letters

1. Download the repository and load the `teach-05.sln` in your code editor, and open the file `SetProblems.cs` to the `AreUniqueLetters(...)` function.
2. This code will determine if a string has all unique letters. For example, "abcdefg" has unique letters but "abccdefg" does not because the "c" is repeated more than once. The code is implemented using loops which results in an O(n<sup>2</sup>) performance.
3. Answer the question together: how can unique letter method be written with O(n) performance using a set? As you answer this question, talk about the behavior, purpose and/or performance of a set to help you arrive at an answer.
4.  When you think you know how to solve the problem (take no more than five minutes), [read the answer to the question](teach-part1-answer){:target="_blank"} and compare with your initial answer.
5. Based on your understanding, replace the code in the `AreUniqueLetters` method, so it achieves O(n) using a set. Run the tests is `Tests.cs` to verify that it works.
6. When you are done, check out the `AreUniqueLettersSolution.cs` file, examine the 2 different solutions, and discuss them together.

### Problem 2 - Find Sum Pairs

1. `SetProblems.cs` to the `FindSumPairs(...)` function
2. Your goal is to write a program that will find all pairs of numbers in a list that sum up to 10. No duplicates should be displayed. This could be done in O(n^2) with a loop within a loop. However, using a set, this can be done in O(n) time. You should assume that the list of numbers provided has no duplicates.
3. Answer this question together: how can you solve the problem using a set data structure? As you answer this question, talk about the behavior, purpose, and/or performance of a set to help you arrive as the answer.
4. When you think you know how to solve the problem (take no more than five minutes), [read the answer to the question](teach-part2-answer){:target="_blank"} and compare with your initial answer.
5. Based on your understanding, implement the `FindSumPairs` function. Run the tests is `Tests.cs` to verify that it works.
6. When you are done, check out the `FindSumPairsSolution.cs` file and discuss the solution together.

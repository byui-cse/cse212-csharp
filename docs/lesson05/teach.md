---
layout: default
title: "W05 Teach: Group Practice"
---

# W05 Teach: Group Practice

## Instructions

These problems should be completed and discussed as a group. Answers are provided below.

All of the files for this assignment will be found in the GitHub classroom ***teach-05*** repository.

### Problem 1 - Unique Letters

1. Download the repository and load the `teach-05.csproj` in your code editor, and open the file **UniqueLetters.cs**
2. This code will determine if a string has all unique letters. For example, "abcdefg" has unique letters but "abccdefg" does not because the "c" is repeated more than once. The code is implemented using loops which results in an O(n<sup>2</sup>) performance.
3. Answer the question together: how can unique letter method be written with O(n) performance using a set? As you answer this question, talk about the behavior, purpose and/or performance of a set to help you arrive at an answer.
4.  When you think you know how to solve the problem (tale no more than five minutes), [read the answer to the question](teach-part1-answer){:target="_blank"} and compare with your initial answer.
5. Based on your understanding, replace the code in the AreUniqueLetters method, so it achieves O(n) using a set.
6. When you are done, uncomment the lines in **Program.cs** to include running the UniqueLettersSolution and take a look at the **UniqueLettersSolution.cs** file and discuss it together.

### Problem 2 - Display Sums

1. Open the file **DisplaySums.cs**
2. Your goal is to write a program that will find and display all pairs of numbers in a list that sum up to 10. No duplicates should be displayed. This could be done in O(n^2) with a loop within a loop. However, using a set, this can be done in O(n) time. You should assume that the list of numbers provided has no duplicates.
3. Answer this question together: how can you solve the problem using a set data structure? As you answer this question, talk about the behavior, purpose, and/or performance of a set to help you arrive as the answer.
4. When you think you know how to solve the problem (take no more than five minutes), [read the answer to the question](teach-part2-answer){:target="_blank"} and compare with your initial answer.
5. Based on your understanding, implement the DisplaySumPairs function.
6. When you are done, uncomment the lines in **Program.cs** to include running the DisplaySumsSolution and take a look at the **DisplaySumsSolution.cs** file and discuss it together.

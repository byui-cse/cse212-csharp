---
layout: default
title: "W08 Prove: Individual Assignment"
---

# W08 Prove: Individual Assignment
## Instructions
This assignment **must be completed individually** to ensure you are meeting all course outcomes. You should not complete this assignment within a group. If you obtain help from a tutor, the tutor should help you understand principles but should not help you answer these problems. It is an honor code violation to obtain answers for these problems from others including using the internet (i.e. sites that allow students to share their solutions).

As you solve the problems, remember to use the principles learned in the first five lessons of the course:
* Problem Solving Strategy: understand the problem, plan and design the solution, implement the solution, and evaluate the solution.
* Evaluate Performance of Alternative Solutions: use big O to determine the best solution.
* Understanding Code Using Reviews: analyze any code you have been given.
* Finding Defects Using Tests: write tests to determine if your solution is working.
* Articulating Answers for Technical Questions: imagine that you were asked one of these questions during an interview. Remember to ensure that you fully understand the problem and work through different scenarios manually. Consider how the data structure you are using will help you solve the problem. A notebook or a whiteboard can be very useful in this process.

All the files for this assignment will be found in the GitHub classroom ***prove-08*** repository. You will commit changes to your own repository for your submission for this assignment.

#### Step 1: [Accept your assignment repository](prove-classroom){:target="_blank"}

### Problem 1 - Recursive Squares Sum
Implement the `SumSquaresRecursive` function in the `SumSquares` class to find the sum `1^2 + 2^2 + 3^2 + ... + n^2` using recursion. Remember to both express the solution in terms of recursive call on a smaller problem and to identify a base case (terminating case). If the value of `n <= 0`, just return 0. A loop should not be used.

### Problem 2 - Permutations Choose
In the `Mutator.PermutationsChoose` method, use recursion to calculate permutations of length `size` from a list of `letters`. This function should assume that each letter is unique (i.e. the function does not need to deduplicate letters). In mathematics, we can calculate the number of permutations using the formula:

`letters.Length! / (letters.Length - size)!`

For example, if `letters` was `['A','B','C']` and size was 2 then the following would be added to `Results`: AB, AC, BA, BC, CA, CB (might be in a different order). You can assume that the size specified is always valid (between 1 and the length of the letters list).

### Problem 3 - Climbing Stairs
Imagine that there was a staircase with `s` stairs. We want to count how many ways there are to climb the stairs. If the person could only climb one stair at a time, then the total would be just one. However, if the person could choose to climb either one, two, or three stairs at a time (in any order), then the total possibilities become much more complicated. If there were just three stairs, the possible ways to climb would be four as follows:
* 1 step, 1 step, 1 step
* 1 step, 2 step
* 2 step, 1 step
* 3 step

With just one step to go, the ways to get to the top of `s` stairs is to either:
* Take a single step from the second to last step
* Take a double step from the third to last step
* Take a triple step from the fourth to last step

We don't need to think about scenarios like taking two single steps from the third to last step because this is already part of the first scenario (taking a single step from the second to last step).

These final leaps give us a sum:

`CountWaysToClimb(s) = CountWaysToClimb(s-1) + CountWaysToClimb(s-2) + CountWaysToClimb(s-3)`

To run this function for larger values of `s`, you will need to update this function to use memoization. The parameter `remember` has already been added as an input parameter to the function for you to complete this task.

Examine the code in `StairClimber.cs` to see how the version without memoization is already implemented.

### Problem 4 - Wildcard Binary Patterns
A binary string is a string consisting of just `1`'s and `0`'s. For example, `1010111` is a binary string. If we introduce a wildcard symbol `*` into the string, we can say that this is now a pattern for multiple binary strings. For example, `101*1` could be used to represent `10101` and `10111`. A pattern can have more than one `*` wildcard. For example, `1**1` would result in 4 different binary strings: `1001`, `1011`, `1101`, and `1111`.

Using recursion, determine all possible binary strings for a given pattern. You might find some of the `string` functions like `IndexOf` and `myStr[..X]` or `myStr[X..]`  to be useful in solving this problem.

Examine the comments in `WildcardBinary.ExpandPattern()` to see how to save each result.

### Problem 5 - Maze
A maze is defined as an array of integer values. The array is defined for an *n* x *n* maze, the first *n* elements of the array represents the first row in the maze. The next *n* elements define the 2nd row and so on. You can assume that the maze will be square (same number of rows and columns). The values of the array define each maze position as:
* 0 = Wall (You can't go through this)
* 1 = Open Path (You can go through this)
* 2 = End (You want to get to this point to win)

In the code, there are two sample mazes. Each maze shows 0, 1, or 2 in each box. The blue boxes are walls and the white boxes are pathways. The solution to each maze is highlighted in red. Note that the small maze has two possible solutions and the big maze has only one possible solution.

{% include image.html url="small_maze.jpg" description="Shows a 3 by 3 maze (indices 0 to 2) populated as described in the code for the small_maze test.  The expected output shown in the code for this maze is highlighted in the picture." caption="Small Maze Example" %}

{% include image.html url="big_maze.jpg" description="Shows a 20 by 20 maze (indices 0 to 19) populated as described in the code for the small_maze test.  The expected output shown in the code for this maze is highlighted in the picture." caption="Big Maze Example" %}

The `IsEnd` and the `IsValidMove` functions are already written for you. These functions assume that the first square in the maze is `(0,0)`. These functions also assume that you can't leave the boundaries of the maze and that you can't visit the same square in the same path (no circles). The `IsEnd` will return `true` if the `x` and `y` coordinate represent the end of the maze. The `IsValidMove` will return `true` if the movement to `x` and `y` is within the maze boundaries, does not represent a wall, and is not someplace we have already been.

The `currPath` variable is a list of (x,y) tuples that represent the path we are currently on. If you add a new position to the path, make sure that you add the tuple to the list so that the `IsValidMove` function works properly.

The goal is to implement the `Solve` function to display all paths to the end square using recursion. When you find a path to the solution, call the `MarkSolution(currPath)` method to store the result for verification.

## Submission
You need to submit the following for this assignment:
* Make sure all of your changes are committed and pushed to the `main` branch of your **prove-08-[username]** repository
* Submit a link to your repository in I-Learn

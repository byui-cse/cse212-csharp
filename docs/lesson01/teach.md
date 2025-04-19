---
layout: default
title: "W01 Teach: Group Practice"
---

# W01 Teach: Group Practice

## Instructions

These problems should be completed and discussed as a group.  Answers are provided below.

All the code files for this assignment will be found in the GitHub classroom ***teach-01*** repository.

#### Step 1: [Accept your assignment repository](teach-classroom){:target="_blank"}

### Problem 1 - Using Dynamic Arrays: Lists

1. To ensure you have enough time for this activity, spend no more than 20 minutes implementing this method before looking at the solution to discuss.
  
2. Download the repository and load the `teach-01.sln` in your code editor, and open the file `Divisors.cs`

3. Implement the `FindDivisors()` method in the Divisors class.
    * The method should create and return a list of divisors of the number provided into the method. The list should include the value 1 but should not include the actual number. If the number was 12, then the resulting list would be `[1, 2, 3, 4, 6]`. If the number was 17, then the resulting list would be just `[1]` because 17 is a prime number. When implementing the method, use a for loop, an if statement, and call `Add`.

4. Compare your answer with the code found in `solutions/DivisorsSolution.cs` and discuss together.

### Problem 2 - Solving a Complicated Problem
  1. Open up the file:  `ArraySelector.cs`

  2. Implement the int version of the `ListSelector()` method in the ArraySelector class.

  3. Come up with a plan (up to 10 minutes) on how to implement the integer version the `ListSelector()` method. The function takes two arrays and a selector array. The two arrays are combined into a new array according to the selector array. The selector array only contains 1's and 2's. A value of 1 means that you should select the next number from the first array. A value of 2 means that you should select the next number from the second array. For example, if array 1 is `[1, 2, 3, 4]` and if array 2 is `[10, 20, 30, 40]` and if the selector array is `[1, 1, 2, 2, 1, 1, 2, 2]`, then the resulting array would be `[1, 2, 10, 20, 3, 4, 30, 40]`.
   
  4. Compare your plan with the following plan and discuss together: [Array Selector Approach](teach-approach)
   
  5. Implement the `ListSelector()` method for both integers and characters.
   
  6. Compare your answer with the code found in `solutions/ArraySelectorSolution.cs` and discuss together.


---
layout: default
title: "W01 Teach: Group Practice"
---

# W01 Teach: Group Practice

## Instructions
These problems should be completed and discussed as a group.  Answers are provided below.

### Problem 1 - List Comprehension

  01.  To ensure you have enough time for this activity, spend no more than 15 minutes implementing this method before looking at the solution to discuss.
   
  2. Open up the following code:  [Link to file]()

  3. Implement the FindDivisorFixedArray() method in the Divisors class. The method should create and return a list of divisors of the number provided into the method. The list should include the value 1 but should not include the actual number. If the number was 12, then the resulting list would be [1, 2, 3, 4, 6]. If the number was 17, then the resulting list would be just [1] because 17 is a prime number. When implementing the first method, use a for loop, an if statement, and call append.

  4. Re-implement the function using only a list comprehension in find_divisors_2

  5. Compare your answer with the [solution]() and discuss together.

### PROBLEM 2 - SOLVING A COMPLICATED PROBLEM
  01. Open up the following code: [file here]()
   
  2. Come up with a plan (up to 10 minutes) on how to implement the FindDivisorsDynamicArray() method. The function takes two lists and a selector list. The two lists are combined together into a new list according to the selector list. The selector list only contains 1's and 2's. A value of 1 means that you should select the next number from the first list. A value of 2 means that you should select the next number from the second list. For example, if list 1 is [1, 2, 3, 4] and if list 2 is [10, 20, 30, 40] and if the selector list is [1, 1, 2, 2, 1, 1, 2, 2], then the resulting list would be [1, 2, 10, 20, 3, 4, 30, 40].
   
  3. Compare your plan with the following plan and discuss together: [file here]()
   
  4. Implement the list_selector method.
   
  5. Compare your answer with the [solution]() and discuss together.


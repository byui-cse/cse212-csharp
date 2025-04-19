---
layout: default
title: "W01 Prove: Individual Assignment"
---

# W01 Prove: Individual Assignment
## Instructions

This assignment **must be completed individually** to ensure you are meeting all course outcomes. You should not complete this assignment within a group. If you obtain help from a tutor, the tutor should help you understand principles but should not help you answer these problems. It is an honor code violation to obtain answers for these problems from others including using the internet (i.e. sites that allow students to share their solutions).

All the files for this assignment will be found in the GitHub classroom ***prove-01*** repository - including the 01-prove_response.docx. You will commit changes to your own repository for your submission for this assignment.

#### Step 1: [Accept your assignment repository](prove-classroom){:target="_blank"}

### Response Document
Examine the `01-prove_response.docx` document to provide your answers to questions asked in the steps below. You will commit this document back to your repository for submission.

### Part 1 - Arrays
1. Open up the following code file: `Lists.cs`
2. Implement the `MultiplesOf` function. The function should create and return a list of multiples of a number. The starting number and the number of multiples are provided as inputs to the function. For example, `MultiplesOf(3,5)`, where the 3 is the starting number and 5 is the number of multiples, would result in `[3, 6, 9, 12, 15]`.
3. You should **NOT** modify the tests

### Part 2 - Solving a Complicated Problem Using a List
1. Come up with a plan on how to implement the `RotateListRight` function. This function receives a list of `data` and an `amount` to rotate to the right. For example, if the `data` is `[1, 2, 3, 4, 5, 6, 7, 8, 9]` and an `amount` is 5 then the list returned should be `[5, 6, 7, 8, 9, 1, 2, 3, 4]`. If the `data` is `[1, 2, 3, 4, 5, 6, 7, 8, 9]` and an `amount` is 3 then the list returned should be `[7, 8, 9, 1, 2, 3, 4, 5, 6]`. The value of `amount` will be in the range of 1 and `data.Count`. Remember the suggestion to "solve the problem manually." Write down a process for doing this step by step before you write the code.
    * **Hint**: There are multiple ways to solve this problem. Don't worry about trying to find the most elegant solution this week. Your solution could use modulo (%) to deal with wrapping around the index number back to 0. Your solution alternatively could use a technique called list slicing. While you can use the syntax `array[3..]` for arrays, `List` in C# uses methods that include the word `__Range` to get the slice. For example, if you had a list `data = [1,2,3,4,5]` then `data.GetRange(0, 3)` will give you a new list `[1,2,3]` which goes from the beginning of the list (index 0) up for 3 values. If you wrote the slice as `data.GetRange(3, data.Count - 3)` then you would get the list `[4,5]` which is index 3 to the end. Other helpful methods you might find helpful are:
        * `GetRange(index, count)`
        * `RemoveRange(index, count)`
        * `AddRange(list or array)`
        * `InsertRange(index, list or array)`
        * `Add(value)`
        * `Insert(index, value)`
        * `RemoveAt(index)`
    * See the [documentation for a C# List](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-6.0#methods){:target="_blank"} to see all the methods available.
2. Implement the `RotateListRight` function. Remember to add useful comments to your code.
3. You should **NOT** modify the tests
4. In your response document, give a description (including a picture) of how the code is solving the problem. For the picture, you may use the computer or a white board and just snap a picture with your phone.

## Submission
You need to submit the following for this assignment:
* Make sure all of your changes are committed and pushed to the `main` branch of your **prove-01-[username]** repository
* Submit a link to your repository in I-Learn

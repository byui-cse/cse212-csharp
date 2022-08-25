---
layout: default
title: "W01 Prove: Individual Assignment"
---

# W01 Prove: Individual Assignment
## Instructions

This assignment **must be completed individually** to ensure you are meeting all course outcomes. You should not complete this assignment within a group. If you obtain help from a tutor, the tutor should help you understand principles but should not help you answer these problems. It is an honor code violation to obtain answers for these problems from others including using the internet (i.e. sites that allow students to share their solutions).

Download the [01-prove_response.docx](01-prove_response.docx) document to provide your answers to questions asked in the steps below.

### Part 1 - List Comprehension
1. Open up the following code: [01-prove_multiples_of.py]()
2. Implement the `multiples_of` function. The function should create and return a list of multiples of a number. The starting number and the number of multiples are provided as inputs to the function. For example, `multiples_of(3,5)`, where the 3 is the starting number and 5 is the number of multiples, would result in `[3, 6, 9, 12, 15]`. You must implement this using a single list comprehension. You may want to write it first without a list comprehension and then modify it.

### Part 2 - Solving a Complicated Problem
1. Open up the following code: [01-prove_rotate_list_right.py]()
2. Come up with a plan on how to implement the `rotate_list_right` function. This function receives a list of `data` and an `amount` to rotate to the right. For example, if the `data` is `[1, 2, 3, 4, 5, 6, 7, 8, 9]` and an `amount` is 5 then the list returned should be `[5, 6, 7, 8, 9, 1, 2, 3, 4]`. The value of `amount` will be in the range of 1 and `len(data)`. Remember the suggestion to "solve the problem manually." Write down a process for doing this step by step before you write the code.
3. **Hint**: There are multiple ways to solve this problem. Don't worry about trying to find the most elegant solution this week. Your solution could use module (%) to deal with wrapping around the index number back to 0. Your solution alternatively could use a technique called list slicing. For example, if you had a list `data = [1,2,3,4,5]` then `data[:3]` will give you a new list `[1,2,3]` which goes from the beginning of the list up to but not including index 3. If you wrote the slice as `data[3:]` then you would get the list `[4,5]` which is index 3 to the end.
4. Implement the `rotate_list_right` function. Remember to add useful comments to your code.
5. In your response document, give a description (including a picture) of how the code is solving the problem.

## Submission
You need to submit the following files for this assignment:

* `01-prove_response.docx` - All answers should be provided.
* `01-prove_multiples_of.py` - Your solution from Part 1.
* `01-prove_rotate_list_right.py` - Your solution from Part 2.

Please submit each file separately. Do not use a compression tool (e.g., zip, rar) to combine the files.
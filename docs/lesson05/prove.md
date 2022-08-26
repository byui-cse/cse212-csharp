---
layout: default
title: "W05 Prove: Individual Assignment"
---

# W05 Prove: Individual Assignment
## Instructions
This assignment **must be completed individually** to ensure you are meeting all course outcomes. You should not complete this assignment within a group. If you obtain help from a tutor, the tutor should help you understand principles but should not help you answer these problems. It is an honor code violation to obtain answers for these problems from others including using the internet (i.e. sites that allow students to share their solutions).

Download the [05-prove_response.docx](05-prove_response.docx) document to provide your answers to questions asked in the steps below.

### Part 1 - Set Operations
1. Assume you have been asked in an interview to describe how you would write a function to find the intersection of two sets and a function to find the union of two sets. An intersection will return a set containing items that are common between the two sets. A union will return a set containing all items from both sets. Do not use the set operators (+, -, *, &, \|) and functions (intersection, union) that are built-in to Python. You will need to use a set to to implement these functions.
2. Write down an answer to the question in your response document as if you were giving a verbal response with an emphasis on the purposes, behavior, and/or performance of a set. Your response should be no more than a 30 second answer if spoken out loud.
3. Download the following code file: [05-prove_set_operations.py]()
4. Implement both the `intersection` and the `union` functions in the code file provided above without using the & and \| operators. Remember to add useful comments to your code.

### Part 2 - Find Pairs
1. Assume you have been asked in an interview to describe how you would find symmetric pairs of two letter words in a list in O(n) time using a set. You should assume that the the words are lower case, two characters long, and contain no duplicates. As an example, if the word list was `[am, at, ma, if, fi]` then the result would be `am & ma, if & fi`. The order of the display would not matter. Note that the `at` would not be displayed because `ta` was not in the list. As a special case, if the letters are the same (example: `aa`) then it would not match anything else (remember the assumption above that there were no duplicates) and therefore should not be displayed.
2. Write down an answer to the question in your response document as if you were giving a verbal response with an emphasis on the purpose, behavior, and/or performance of a set. Your response should be no more than a 30 second answer if spoken out loud.
3. Download the following code file: 05-prove_find_pairs.py
4. Implement the `find_pairs` function with O(n) time using sets in the code file provided above.

## Submission
You need to submit the following files for this assignment:
* `05-prove_response.docx` - All answers should be provided.
* `05-prove_taking_turns_queue.py` - Code from Part 1 with all errors fixed.
* `05-prove_priority_queue.py` - Code form Part 2 with all errors fixed.

Please submit each file separately. Do not use a compression tool (e.g., zip, rar) to combine the files.

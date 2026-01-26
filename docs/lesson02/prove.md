---
layout: default
title: "W02 Prove: Individual Assignment"
---

# W02 Prove: Individual Assignment
## Instructions
This assignment **must be completed individually** to ensure you are meeting all course outcomes. You should not complete this assignment within a group. If you obtain help from a tutor, the tutor should help you understand principles but should not help you answer these problems. It is an honor code violation to obtain answers for these problems from others including using the internet (i.e. sites that allow students to share their solutions).

Download the [02-prove_response.docx](02-prove_response.docx) document to provide your answers to questions asked in the steps below.

All the files for this assignment will be found in the GitHub classroom ***prove-02*** repository. You will not need to modify the repository for this assignment.

#### Step 1: [Create your assignment repository](prove-classroom){:target="_blank"}

#### Step 2: [Accept repository invite to resolve Access Issues](https://github.com/settings/organizations){:target="_blank"}

### Part 1 - Analyze Code
In this section, you will be asked several questions that need to be answered in your response document:

1. Open up the following code and determine the big O notation for the `SortArray` function: **Sorting.cs**
2. Open up the following code and determine the big O notation for the three implementations of calculating the standard deviation from a list of numbers: **StandardDeviation.cs**
3. There are several other common big O notations that occur in various algorithms including
    * Merge Sort Algorithm - O(n log n) - Logarithmic Linear Time
    * Traveling Salesman Algorithm - O(2 ^ n) - Exponential Time
4. Using either a graphing calculator or a graphing website (e.g. [desmos.com](https://www.desmos.com/calculator)), put the following in order (best performance, ..., worst performance) for when ***n*** is large:
    * O(n^2), O(1), O(2^n), O(n log n), O(log n), O(n)

### Part 2 - Predicting, Measuring, and Comparing - Two Sorting Algorithms
1. Open up the following code: **Search.cs**
2. This file contains two different functions called `SearchSorted1` and `SearchSorted2`. Both of these functions will search for an item in a sorted list. Predict the performance of each function using big O notation and provide your answer in the response document.
3. Run the code and observe the outputs. Here is what the columns in the table represent:
    * `n` - The size of the data given to the functions in this test
    * `sort1-count` - The number of loop iterations (i.e. work) done by SearchSorted1
    * `sort2-count` - The number of loop iterations (i.e. work) done by SearchSorted2
    * `sort1-time` - The time in milliseconds it took to complete SearchSorted1
    * `sort2-time` - The time in milliseconds it took to complete SearchSorted2
4. While the `sort#-count` value should be the same in every execution, the `sort#-time` will vary every time it is executed on the same or different computers. For the timing numbers, the code ran the test one hundred times and took the average. This was done since there are some operating system conditions that could affect timing in some cases. To ensure worst case, each test tried to find a number that was not in the list.
5. Answer the following questions in your response document:
    * What is the performance using big O notation for each function (based on both your predictions and the actual results)?
    * Which function has the better performance in the worst case?
    * For both functions, explain in detail how you determined the big O notation by just looking at the structure of the code without the benefit of observing actual execution results.
    * It is possible, in the best case, for each of these functions as already written to complete in O(1) time even if the size of the list was very large. What scenario would give this best case result for both functions?

## Submission
You need to submit the following files for this assignment:
* `02-prove_response.docx` - All answers should be provided.
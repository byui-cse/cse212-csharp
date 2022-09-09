---
layout: default
title: "W01 Teach: Problem 2 Approach"
---

# W01 Teach: Problem 2 Approach

To solve the Array Selector problem, we will need to do the following as we loop through the selector array:

* If the current value in the selector array is a 1, then we want to get the next item from the first array
* If the current value in the selector array is a 2, then we want to get the next item from the second array
* We need to append the value we just selected to the new array

We will need a way to determine what the next item is in either array 1 or array 2. We will need variables to keep track of where we are (i.e. the index) in both arrays:

* **array1Index** - We will use this to keep track of the index of the next item in the first array
* **array2Index** - We will use this to keep track of the index of the next item in the second array

We will initialize both of these variables to 0. When we select an item from one of the arrays (per the selector array) we will add one to either **array1Index** or **array2Index** depending on which one was selected.

{% include image.html url="merge_arrays_plan.jpg" description="Shows array1, array2, and a selectorArray as described in the example from W01-Teach. Arrows are drawn from the selectorArray to either array1 or array2 depending on the value in the selectorArray (1 goes to array1 and 2 goes to array2).  A table is shown for each loop through the selector array (0 to 7) and the values of array1Index (0, 1, 1, 1, 2, 3, 3, 3) and array2Index (0, 0, 0, 1, 1, 1, 2, 3) as we go through the array.  The building of the result_array based on the array1Index and array2Index is shown as: [1], [1,2], [1,2,10], [1,2,10,20], [1,2,10,20,3], [1,2,10,20,3,4], [1,2,10,20,3,4,30], [1,2,10,20,3,4,30,40]." caption="Solving the Problem Manually on Paper" %}

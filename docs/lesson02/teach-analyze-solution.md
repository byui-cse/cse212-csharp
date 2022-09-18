---
layout: default
title: "W02 Teach - Part 1 Answer"
---

# W02 Teach - Part 1 Answer

* **Question**: What is the big O notation for `CalculateFactorial`?
* **Answer**: The `CalculateFactorial` function has a single for loop. This implies O(n).

--------

* **Question**: What is the big O notation for `CalculateStats`?
* **Answer**: The `CalculateStats` function has a single for loop followed by another single for loop. This implies O(n) + O(n) = O(2n). With big O notation, the coefficient is dropped and we can simplify this to be O(n).

--------

* **Question**: What is the big O notation for `PrintTriangle`?
* **Answer**: The `PrintTriangle` function has a for loop within another for loop. The outer for loop is based on the size of the data (in this case `size`). The inner for loop is based on the size of the outer loop. During the first iteration of the outer loop, the inner loop will only run 1 time. However, on the last iteration of the outer loop, the inner loop will run `size` times. Since the inner loop is based on the size (even though its decreasing), this implies O(n<sup>2</sup>). To see this better, we can count how many times the inner loop runs. The first time the inner loop runs 1 times, the second time 2 times, and so forth up until size times. Adding this up we get: 1 + 2 + 3 + ... + (`size`-1) + (`size`) = 0.5 * `size`(`size` + 1) = 0.5*`size`<sup>2</sup> + 0.5*`size`. This simplifies down to O(n<sup>2</sup>) since lower order exponents and coefficients are dropped with big O notation.

--------

* **Question**: What is the big O notation for `DisplayLettersInNames`?
* **Answer**: The `DisplayLettersInNames` function has a for loop within another for loop. The outer for loop is based on the size of the data (in this case the number of names in the list). The inner for loop is based on the length of each name and not the size of the data. This implies O(n). Imagine the list of names had 1,000,000 names. The average name size might be less than 10 letters long. This has the affect of running O(10n) which reduces to O(n). Note that sometimes you may see a problem like this have a solution of O(mn) where n represents the number of names and m represents the max name size.

--------

* **Question**: What is the big O notation for `numbers.Sum()`?
* **Answer**: The `Sum` function in C# LINQ syntax will loop through all the numbers in the array (technically `IEnumerable`) and add them together. This will be O(n).

--------

* **Question**: What is the big O notation for `numbers.Average()`?
* **Answer**: The `Average` function first executes the `Sum` function and then divides the sum by the length. The length is stored as part of the array, and so the retrieval of the length and the division operation are both O(1). Therefore, the total cost is O(n).

--------

* **Question**: What is the order of O(n<sup>2</sup>), O(log n), and O(n) (best performance first and worst performance last)?
* **Answer**: The first graph below shows the 3 graphs displayed for small values of n and the second graph shows the same 3 graphs zoomed out for larger values of n. By looking at the graph, O(n<sup>2</sup>) is worst performance because it increases faster as the data size increases. In contrast, O(log n) has the best performance because it increases slower as the data size increases. This is seen even more in the second graph where y=x<sup>2</sup> is approaching the y-axis and y=log x is approaching the x-axis. The order is: O(log n), O(n), O(n<sup>2</sup>).


{%
include image.html url="graph_close_up.jpg"
description="Shows the graph y=x^2, y=x, and y=log x on the same graph for x in the range from 0 to  6.  As x gets bigger, y=x^2 goes up faster than y=x and y=x goes up faster than y=log x."
caption="Representation of O(n), O(n<sup>2</sup>), & O(log n) zoomed in"
%}

{%
include image.html url="graph_zoomed_out.jpg"
description="Shows the same graph but with x in the range from 0 to 200.  The y=x^2 line is approaching the y-axis and the y=log x is approaching the x-axis."
caption="Representation of O(n), O(n<sup>2</sup>), & O(log n) zoomed out"
%}


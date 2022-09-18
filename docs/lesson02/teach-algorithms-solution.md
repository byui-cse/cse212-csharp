---
layout: default
title: "W02 Teach - Part 2 Answer"
---

# W02 Teach - Part 2 Answer

* **Question**: Do the actual results agree with the big O predictions made earlier? If not, what do you think the big O should be?
* **Answer**: The `Algorithm1` function has a single for loop. This implies O(n). If we look at the actual results, we see that count is the same value as the size of the list. The `Algorithm2` function has a loop within a loop. This implies O(n^2). If we look at the actual results, we see that the count is the square of the size of the data. The `Algorithm3` functions finds the center of the list and then looks at the 2nd half the list. This process is repeated in which each iteration of the while loop the list is cut in half again. This implies O(log n). If we look at the actual results, we see that the count is approximately the base 2 logarithm of the size.

--------

* **Question**: Which function (`Algorithm1`, `Algorithm2`, `Algorithm3`) has the best performance and which one the worst performance?
* **Answer**: Based on the timing data, `Algorithm3` is much faster and `Algorithm2` is much slower. Note that `Algorithm3` is barely increasing (if at all) and `Algorithm2` is growing by larger amounts as the size of the data increases. This result agrees with the big O notation from above. O(log n) is better than O(n), and O(n) is better than O(n<sup>2</sup>) when `n` is "large".

--------

* **Question**: Looking at the results, why do we say that big O only applies when `n` is "large"
* **Answer**: When `n` is small, the time for all three algorithms is very close to each other. Realizing that these are in milliseconds, the amount of time to see the result for `Algorithm2` when `n` is large will start to approach 1 second unlike the other 2 functions. However, when `n` is small, no difference is seen by the user.

---
layout: default
title: "W05 Teach - Part 2 Answer"
---

# W05 Teach - Part 2 Answer

* **Question**: How can find pairs of numbers in a list (assume no duplicates) that sum to a value of 10 and display them in O(n) time using a set data structure?
* **Answer**: We could do two embedded for loops looking for pairs but this would be O(n^2). A set gives us O(1) for lookup. If we knew the value we were looking for and if those values were put in a set, then we could get O(1). We could add all the numbers into a set. Then we could loop through the original list again (call each number x) and then lookup quickly in the set for 10-x. However, we might get duplicate answers (such as 3+7 and 7+3)

    We could avoid the duplication and the two sequential loops. Suppose my list was `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`. While building the set from the list, I could actively check to see if 10-x is in my set yet. If I was currently looking at the '2', then 10-2 (or 8) would not be in the set yet. However, eventually we will get to the '8' and then '2' will be in set by that time. This is O(n).

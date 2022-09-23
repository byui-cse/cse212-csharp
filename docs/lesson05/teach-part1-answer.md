---
layout: default
title: "W05 Teach - Part 1 Answer"
---

# W05 Teach - Part 1 Answer

* **Question**: How can the unique letter function be written with better performance using a set data structure?
* **Answer**: A set has the property that all items must be unique. If the letters in the input text do not form a set, then the function should return False. To determine if the letters in the word form a set, I can loop through each of the letters in the input text and add them one at a time to a set. Looping through each of the letters will be O(n). Before I add a letter to the set, I will check to see if the letter is already in the set. This check will be O(1). I can exit the loop as soon as I find a duplicate letter.
* **Alternative Answer**: A set has a property that all items must be unique. If we copied letters from a string into a set (an O(n) operation), then one of two things would happen. If the letters were all unique, then the size of the set would be equal to the size of the string. However, if the letters were not all unique, the then size of the set would be smaller than the size of the string. We could create the set of unique letters from the string and then compare the sizes to get the answer in O(n) time.

---
layout: default
title: "W11 Prove: Playlist Final Project FAQ"
---

# Playlist Final Project – Student FAQ
This FAQ addresses common questions and pitfalls students often encounter while working on the Playlist Final Project.

## General Questions
### 1. Do all three playlist implementations need to support the exact same features?
Yes. All three implementations must support the same playlist operations and meet the same functional requirements. The only difference between them should be the underlying data structure used.

### 2. Can I reuse code between implementations?
You may reuse ideas and logic, but each implementation should be written as a separate class that clearly demonstrates how the chosen data structure works. Excessive copy-pasting that hides structural differences is discouraged.

### 3. How should I determine if two songs “match”?
Unless otherwise specified, two songs should be considered a match if their title and artist are the same. You may implement this by overriding `Equals()` or by explicitly comparing fields.

## Playlist Behavior
### 4. What happens when `PlayNext()` reaches the end of the playlist?
Once all songs have been played, `PlayNext()` should return `null`. To start playback again from the beginning, you must call `Reset()`.

### 5. What does it mean if a song is “currently playing” when moving songs up or down?
If a song is moved and it was the song most recently returned by `PlayNext()`, playback should continue logically at the same playlist position, even though the song itself may have changed.

### 6. What format should `ShowPlayList()` use?
The exact format is flexible, but it must be clear and consistent. A recommended format is:

`Title - Artist (Length)`

If the playlist is empty, display an `Empty Playlist` message.

## Edge Cases and Exceptions
### 7. When should I throw an `InvalidOperationException`?
You should throw an exception when an operation cannot logically be performed, including:

1. Calling `PlayNext()` or `Reset()` on an empty playlist
2. Moving a song up when it is already at the top
3. Moving a song down when it is already at the end

### 8. What should `RemoveSong()` do if the song is not found?
If the playlist is not empty and the song is not found, `RemoveSong()` should return `false` and make no changes to the playlist.

## Dictionary Implementation
### 9. How can I use a dictionary for an ordered playlist?
Dictionaries do not preserve order by default. You must explicitly manage song order. Common approaches include:

1. Storing an index or position value with each song
2. Maintaining a separate ordered list of keys
3. Using a custom structure that tracks order and lookup separately

Your design choice should be clearly explained in your paper.

## Performance Testing
### 10. Do I need to test every method at every playlist size?
Yes. For valid comparisons, you should measure all core playlist operations at the same playlist sizes for each implementation.

### 11. My timing results are inconsistent. Is that okay?
Yes. This is normal. You should discuss sources of inconsistency in your paper, such as:

1. JIT warm-up effects
2. Garbage collection
3. Caching

Explain what steps you took to improve measurement reliability.

## Final Paper
### 12. Which implementation do you expect to perform best?
There is no single “correct” answer. Your grade is based on the quality of your reasoning, how well your conclusions are supported by data, and how accurately you apply Big-O analysis.

### 13. Do I need to measure memory usage in code?
No. You are not required to measure memory usage programmatically. However, your memory analysis must be technically accurate and grounded in how each data structure allocates and manages memory.

### 14. What matters most in grading the final paper?
Clarity, correctness, and reasoning matter more than writing style. Well-organized explanations supported by data will score higher than vague or unsupported claims.

If you are unsure about a design decision, make a reasonable choice, document it clearly, and justify it in your paper. Thoughtful explanation is a key part of this project.

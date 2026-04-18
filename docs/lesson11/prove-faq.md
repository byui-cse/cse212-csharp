---
layout: default
title: "W11 Prove: Playlist Final Project FAQ"
---

# Playlist Final Project – Student FAQ
This FAQ addresses common questions and pitfalls students often encounter while working on the Playlist Final Project.

## General Questions
#### 1. Do all three playlist implementations need to support the exact same features?
Yes. All three implementations must support the same playlist operations and meet the same functional requirements. The only difference between them should be the underlying data structure used.

#### 2. Where do I write up my Report?
The ***report.md*** file is in your repository you may need to switch to from the `Solution` view to the `File System` view in the Explorer tab:

{% include image.html url="solution-files.png" description="Shows switching to the Files view" caption="Select Files to view the markdown files in the solution" %}

If you want help writing and formatting your report, see [Using Markdown Language](prepare-markdown).

#### 3. Which files should I work in for Week 11?
For Week 11, your main implementation should go in `Playlist1`. Add or update your tests in `PlaylistTests`, and record your Week 11 write-up in `report.md`.

The provided `Menu` is mainly for informal manual testing. It is helpful, but your grade is based on your `IPlaylist` implementation, tests, performance results, and write-up.

If you do not see `report.md` in your solution view, switch to the repository/files view in your editor.

#### 4. Can I reuse code between implementations?
You may reuse ideas and logic, but each implementation should be written as a separate class that clearly demonstrates how the chosen data structure works. Excessive copy-pasting that hides structural differences is discouraged.

#### 5. How should I determine if two songs “match”?
For the main playlist requirements, songs are considered equivalent when **title and artist** match.

With duplicate songs, `RemoveSong`, `MoveSongUp`, and `MoveSongDown` should act on the **first matching song** in playlist order.

## Playlist Behavior
#### 6. What happens when `PlayNext()` reaches the end of the playlist?
If the playlist is not empty and all songs have already been played, `PlayNext()` should return `null`.

It should continue returning `null` until either:

1. `Reset()` is called, or
2. A new song is added

If the playlist is empty, see [When should I throw an `InvalidOperationException`?](#when-should-i-throw-an-invalidoperationexception).

#### 7. What does it mean if a song is “currently playing” when moving songs up, moving songs down, or removing songs?
Think of playback as a cursor between songs. After `PlayNext()` returns a song, the cursor sits immediately after that song.

If the most recently played song is moved, the cursor should move with it. If songs are removed or moved elsewhere, keep playback consistent with that cursor rather than restarting from the beginning.

This means the next song may change if the playlist around the cursor changes.

#### 8. What format should `ShowPlaylist()` use?
The exact format is flexible, but it must be clear and consistent. A recommended format is:

`Title - Artist (Length)`

If the playlist is empty, display an `Empty Playlist` message.

## Edge Cases and Exceptions
#### 9. When should I throw an `InvalidOperationException`?
You should throw an exception when an operation cannot logically be performed, including:

1. Calling `PlayNext()` or `Reset()` on an empty playlist
2. Moving a song up when it is already at the top
3. Moving a song down when it is already at the end

#### 10. What should `RemoveSong()`, `MoveSongUp()`, or `MoveSongDown()` do if the song is not found?
If the song is not found, these methods should return `false` and make no changes to the playlist.

This includes the empty-playlist case for `RemoveSong()`, `MoveSongUp()`, and `MoveSongDown()`.

#### 11. Are duplicate songs allowed?
Yes. Duplicate songs are allowed.

With duplicate songs, `RemoveSong`, `MoveSongUp`, and `MoveSongDown` should act on the **first matching song** in playlist order.

## Dictionary Implementation
#### 12. How can I use a dictionary for an ordered playlist?
Dictionaries do not preserve order by default. You must explicitly manage song order. Common approaches include:

1. Storing an index or position value with each song
2. Maintaining a separate ordered list of keys
3. Using a custom structure that tracks order and lookup separately

Your design choice should be clearly explained in your paper.

## Performance Testing
#### 13. Do I need to test every method at every playlist size?
For the final comparison, use the same playlist sizes across implementations so your results are comparable.

For the Week 11 prove checkpoint, follow the prove page requirements and measure at least the listed operations for multiple playlist sizes.

#### 14. My timing results are inconsistent. Is that okay?
Yes. This is normal. You should discuss sources of inconsistency in your paper, such as:

1. JIT warm-up effects
2. Garbage collection
3. Caching

Explain what steps you took to improve measurement reliability.

#### 15. Are the starter tests complete?
No. The starter tests are examples, not a complete solution.

You are expected to add your own functional tests for all required methods and edge cases, and to add the performance measurements required for each week.

## Final Paper
#### 16. Which implementation do you expect to perform best?
There is no single “correct” answer. Your grade is based on the quality of your reasoning, how well your conclusions are supported by data, and how accurately you apply Big-O analysis.

#### 17. Do I need to measure memory usage in code?
No. You are not required to measure memory usage programmatically. However, your memory analysis must be technically accurate and grounded in how each data structure allocates and manages memory.

#### 18. What matters most in grading the final paper?
Clarity, correctness, and reasoning matter more than writing style. Well-organized explanations supported by data will score higher than vague or unsupported claims.

If you are unsure about a design decision, make a reasonable choice, document it clearly, and justify it in your paper. Thoughtful explanation is a key part of this project.

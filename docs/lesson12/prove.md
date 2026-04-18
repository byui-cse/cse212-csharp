---
layout: default
title: "W12 Prove: Final Project - Part 2"
---

# W12 Prove: Final Project - Part 2
## Instructions
For this prove assignment, submit progress on **Week 12** of the Playlist Final Project.

This week focuses on a **linked-list-based playlist implementation** in `Playlist2`, extending your functional unit tests to cover both versions, and adding the first round of performance comparisons. Although not required, it is highly recommended to use the built in `LinkedList<>` class.

Use this page for the specific Week 12 checkpoint expectations. For the full project description and timeline, see the [Final Project Overview](../lesson11/overview). Before you begin, read the [Playlist Final Project FAQ](../lesson11/prove-faq). It defines the official rules for matching songs, exceptions, playback behavior, duplicates, and starter-template questions.

## Week 12 Scope (Linked List)
For Week 12, implement `IPlaylist` in `Playlist2` using a linked list internally.

Your Week 12 class must support all methods required by `IPlaylist`:

1. `AddSong(Song song)`
2. `RemoveSong(Song song)`
3. `PlayNext()`
4. `Reset()`
5. `MoveSongUp(Song song)`
6. `MoveSongDown(Song song)`
7. `ShowPlaylist()`
8. `Length()`

## What Week 12 Should Demonstrate
By the end of Week 12, you should have enough progress to show that:

1. `Playlist2` compiles and implements the full `IPlaylist` contract.
2. Your linked-list version works for the same normal cases and edge cases as your array/list version.
3. Your functional unit tests clearly cover both `Playlist1` and `Playlist2`.
4. You have performance tests that compare the array/list and linked-list implementations using the same operations and playlist sizes.
5. You have updated `report.md` with what changed in Week 12 and what your first comparison results suggest.

This is still a progress checkpoint, not the final comparison report. You do **not** need the third implementation yet. That begins in Week 13.

## What to Submit
Submit one link to your GitHub repository (or the specific folder/file set) that contains:

1. Your Week 12 linked-list playlist implementation in `Playlist2`
2. Functional unit tests that cover both `Playlist1` and `Playlist2`
3. Performance tests that compare the array/list and linked-list implementations using the same operations and playlist sizes
4. An updated Week 12 write-up in `report.md` with:
   * what changed in your linked-list implementation
   * how your tests verify the second implementation
   * what your first performance comparison suggests so far

The starter repository already includes `report.md`. If you do not see it in your solution view, switch to the repository/files view in your editor.

## Where to Work in the Starter Code
- Put your Week 12 implementation in `Playlist2`.
- Keep `Playlist1` available as your Week 11 array/list version.
- Use `IPlaylist` in `Common` as the required contract.
- Add or update tests in `PlaylistTests`.
- Use `report.md` for your Week 12 reflection and results.
- Use `Menu` if you want manual testing, but do not rely on it as your only validation.

## Required Functional Coverage
Your functional tests should explicitly verify that both `Playlist1` and `Playlist2` handle:

1. `PlayNext()` on an empty playlist
2. `Reset()` on an empty playlist
3. `RemoveSong()` when the song is not found
4. `MoveSongUp()` when the song is already first
5. `MoveSongDown()` when the song is already last
6. `MoveSongUp()` or `MoveSongDown()` when the song is not found
7. `PlayNext()` returning `null` after the final song has been played
8. Adding a new song after `PlayNext()` has started returning `null`
9. Duplicate songs (allowed)

See the [FAQ](../lesson11/prove-faq) for the expected exceptions and return values for these cases.

## Performance Checkpoint
For Week 12, add performance tests that compare `Playlist1` and `Playlist2`.

Use the same operations and playlist sizes for both implementations so the comparison is fair. A good starting point is to compare at least:

- `AddSong`
- `RemoveSong`
- `MoveSongUp`

You may test more operations if you want, but keep the comparison consistent between implementations.

## What Good Evidence Looks Like
A strong Week 12 submission usually includes:

- Clear evidence that `Playlist2` matches the external behavior of `Playlist1`
- Functional tests that run against both implementations
- Performance results collected with the same operations and sizes for both implementations
- A short write-up that explains what changed and what the first comparison suggests
- Code and tests that are organized clearly enough to extend to the third implementation next week

## Looking Ahead to Week 13
In Week 13, you will:

- Implement the third version in `Playlist3`
- Extend your functional tests so they also verify the third implementation
- Add the third implementation to your performance comparisons

## Reminder
All three implementations (Weeks 11-13) must keep the **same external behavior**. Only the internal data structure should change.

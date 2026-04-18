---
layout: default
title: "W11 Prove: Final Project - Part 1"
---

# W11 Prove: Final Project - Part 1
## Instructions
For this prove assignment, submit progress on **Week 11** of the Playlist Final Project.

This week focuses on an **array/list-based playlist implementation** in `Playlist1` and on building the functional unit tests that will support the rest of the project.

Use this page for the specific Week 11 checkpoint expectations. For the full project description and timeline, see the [Final Project Overview](overview). Before you begin, read the [Playlist Final Project FAQ](prove-faq). It defines the official rules for matching songs, exceptions, playback behavior, duplicates, and starter-template questions.

## Week 11 Scope (Array/List)
For Week 11, implement `IPlaylist` using a built-in array or list internally.

Your Week 11 class must support all methods required by `IPlaylist`:

1. `AddSong(Song song)`
2. `RemoveSong(Song song)`
3. `PlayNext()`
4. `Reset()`
5. `MoveSongUp(Song song)`
6. `MoveSongDown(Song song)`
7. `ShowPlaylist()`
8. `Length()`

## What Week 11 Should Demonstrate
By the end of Week 11, you should have enough progress to show that:

1. `Playlist1` compiles and implements the full `IPlaylist` contract.
2. Your array/list version works for normal cases and edge cases.
3. You have meaningful functional unit tests, not just a couple of example tests.
4. Your tests are organized so you can reuse or extend them for the later implementations.
5. You have started documenting your work in `report.md`.

This is a progress checkpoint, not the final comparison report. You do **not** need performance comparisons yet. Those begin in Week 12 after you have a second implementation.


## What to Submit
Submit one link to your GitHub repository (or the specific folder/file set) that contains:

1. Your Week 11 array/list playlist implementation in `Playlist1`
2. Functional unit tests for all required operations and key edge cases
3. A brief Week 11 write-up in `report.md` with:
   * which edge cases you handled
   * any assumptions you made
   * one challenge you hit and how you solved it

The starter repository already includes `report.md`. If you do not see it in your solution view, switch to the repository/files view in your editor.

## Where to Work in the Starter Code
- Put your Week 11 implementation in `Playlist1`.
- Use `IPlaylist` in `Common` as the required contract.
- Add or update tests in `PlaylistTests`.
- Use `report.md` for your Week 11 reflection and results.
- Use `Menu` if you want manual testing, but do not rely on it as your only validation.

## Required Edge Cases
Your implementation/tests should explicitly cover:

1. `PlayNext()` on an empty playlist
2. `Reset()` on an empty playlist
3. `RemoveSong()` when the song is not found
4. `MoveSongUp()` when the song is already first
5. `MoveSongDown()` when the song is already last
6. `MoveSongUp()` or `MoveSongDown()` when the song is not found
7. `PlayNext()` returning `null` after the final song has been played
8. Duplicate songs (allowed)

See the [FAQ](prove-faq) for the expected exceptions and return values for these cases.

## Matching Rules
For the main playlist requirements, songs are considered equivalent when **title and artist** match.

With duplicate songs, `RemoveSong`, `MoveSongUp`, and `MoveSongDown` should act on the **first matching song** in playlist order.

## What Good Evidence Looks Like
A strong Week 11 submission usually includes:

- Tests for both normal cases and edge cases
- Clear evidence that `PlayNext()`, `Reset()`, and song movement work together correctly
- Functional tests that are organized clearly enough to reuse for later implementations
- A short write-up that explains your assumptions and what you learned
- Code that is organized clearly enough that you can build the Week 12 and Week 13 versions from it

## Looking Ahead to Week 12
In Week 12, you will:

- Implement the linked-list version in `Playlist2`
- Make sure your functional unit tests also cover that version
- Add performance tests comparing the array/list and linked-list implementations

## Reminder
All three implementations (Weeks 11-13) must keep the **same external behavior**. Only the internal data structure should change.

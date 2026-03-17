---
layout: default
title: "W11 Prove: Final Project - Status Report 1"
---

# W11 Prove: Final Project - Status Report 1
## Instructions
For this prove assignment, submit progress on **Week 11** of the Playlist Final Project.

This week focuses on an **array/list-based playlist implementation** in `Playlist1` and evidence that your implementation is correct and testable.

Before you begin, read the [Playlist Final Project FAQ](prove-faq). It defines the official rules for matching songs, exceptions, playback behavior, duplicates, and starter-template questions.

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

## Matching Rules
For the main playlist requirements, songs are considered equivalent when **title and artist** match.

To support the provided `Menu` for manual testing, your code should also behave reasonably when only a title is provided. In that case, operate on the **first matching title** in playlist order.

If multiple songs match, `RemoveSong`, `MoveSongUp`, and `MoveSongDown` should act on the **first matching song** in playlist order.

## What to Submit
Submit one link to your GitHub repository (or the specific folder/file set) that contains:

1. Your Week 11 array/list playlist implementation in `Playlist1`
2. Unit tests for all required operations
3. Short performance measurements for at least:
   * `AddSong`
   * `RemoveSong`
   * `MoveSongUp`
4. A brief Week 11 write-up in `report.md` with:
   * which edge cases you handled
   * any assumptions you made
   * one challenge you hit and how you solved it

The starter repository already includes `report.md`. If you do not see it in your solution view, switch to the repository/files view in your editor.

## Required Edge Cases
Your implementation/tests should explicitly cover:

1. `PlayNext()` on an empty playlist
2. `Reset()` on an empty playlist
3. `RemoveSong()` when the song is not found
4. `MoveSongUp()` when the song is already first
5. `MoveSongDown()` when the song is already last
6. `MoveSongUp()` or `MoveSongDown()` when the song is not found
7. `PlayNext()` returning `null` after the final song has been played
8. Adding a new song after `PlayNext()` has started returning `null`
9. Duplicate songs (allowed)

See the [FAQ](prove-faq) for the expected exceptions and return values for these cases.

## Performance Checkpoint
Collect timing data for your Week 11 implementation at multiple playlist sizes (for example: 10, 100, 1,000, 10,000).

You do not need a full final-paper analysis yet, but you should include enough data to show early trends and prepare for later comparison with linked-list and dictionary versions. Reuse the same playlist sizes again in later weeks when possible.

## Reminder
All three implementations (Weeks 11-13) must keep the **same external behavior**. Only the internal data structure should change.

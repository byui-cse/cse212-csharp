---
layout: default
title: "W11 Prove: Final Project - Status Report 1"
---

# W11 Prove: Final Project - Status Report 1
## Instructions
For this prove assignment, submit progress on **Week 11** of the Playlist Final Project.

This week focuses on an **array/list-based playlist implementation** and evidence that your implementation is correct and testable.

## Week 11 Scope (Array/List)
Your Week 11 class must support these core methods:

1. `AddSong(Song song)`
2. `RemoveSong(Song song)`
3. `PlayNext()`
4. `Reset()`
5. `MoveSongUp(Song song)`
6. `ShowPlayList()`
7. `Length()`

Use song **title + artist** as the match criteria unless you clearly document a different approach.

## What to Submit
Submit one link to your GitHub repository (or the specific folder/file set) that contains:

1. Your Week 11 array/list playlist implementation
2. Unit tests for all required operations
3. Short performance measurements for at least:
   * `AddSong`
   * `RemoveSong`
   * `MoveSongUp`
4. A brief write-up (in your README or submission notes) with:
   * which edge cases you handled
   * any assumptions you made
   * one challenge you hit and how you solved it

## Required Edge Cases
Your implementation/tests should explicitly cover:

1. Empty playlist behavior (`PlayNext`, `Reset`, `RemoveSong`, `MoveSongUp`)
2. Song-not-found behavior for `RemoveSong`
3. `MoveSongUp` when the song is already first
4. `PlayNext` returning `null` after the final song until `Reset()` is called
5. Duplicate songs (allowed)

## Performance Checkpoint
Collect timing data for your Week 11 implementation at multiple playlist sizes (for example: 10, 100, 1,000, 10,000).

You do not need a full final-paper analysis yet, but you should include enough data to show early trends and prepare for later comparison with linked-list and dictionary versions.

## Reminder
All three implementations (Weeks 11-13) must keep the **same external behavior**. Only the internal data structure should change.

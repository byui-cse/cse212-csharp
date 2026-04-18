---
layout: default
title: "W13 Prove: Final Project - Part 3"
---

# W13 Prove: Final Project - Part 3
## Instructions
Week 13 is the final work week for the Playlist Final Project.

There is **no separate Week 13 draft submission**. Instead, use this week to finish the **third playlist implementation** in `Playlist3`, extend your functional tests to cover all three versions, update your performance comparisons so all three implementations are measured the same way, and prepare your final project submission for the beginning of **Week 14**.

Use this page for the specific Week 13 checkpoint expectations. For the full project description and timeline, see the [Final Project Overview](../lesson11/overview). Before you begin, read the [Playlist Final Project FAQ](../lesson11/prove-faq). It defines the official rules for matching songs, exceptions, playback behavior, duplicates, and starter-template questions.


## Week 13 Scope (Third Implementation)
For Week 13, implement `IPlaylist` in `Playlist3` using a BST or dictionary.

Your Week 13 class must support all methods required by `IPlaylist`:

1. `AddSong(Song song)`
2. `RemoveSong(Song song)`
3. `PlayNext()`
4. `Reset()`
5. `MoveSongUp(Song song)`
6. `MoveSongDown(Song song)`
7. `ShowPlaylist()`
8. `Length()`

## What Week 13 Should Demonstrate
By the end of Week 13, you should have enough progress to show that:

1. `Playlist3` compiles and implements the full `IPlaylist` contract.
2. Your third implementation works for the same normal cases and edge cases as the first two versions.
3. Your functional unit tests clearly cover `Playlist1`, `Playlist2`, and `Playlist3`.
4. Your performance tests compare all three implementations using the same operations and playlist sizes.
5. You have updated `report.md` with what changed in the third implementation, what your three-way comparison suggests, and the direction of your final recommendation.

This is the final implementation checkpoint before the final submission. By the end of this week, you should have all three versions working, reviewed, and ready for final polishing.

## What to Complete This Week
There is no separate Week 13 draft to turn in. By the end of this week, your repository should be ready for the final submission and should contain:

1. Your Week 13 playlist implementation in `Playlist3`
2. Functional unit tests that cover `Playlist1`, `Playlist2`, and `Playlist3`
3. Performance tests that compare all three implementations using the same operations and playlist sizes
4. An updated Week 13 write-up in `report.md` with:
   * what changed in your third implementation
   * how your tests verify all three implementations
   * what your three-way performance comparison suggests so far
   * the direction of your current recommendation

The starter repository already includes `report.md`. If you do not see it in your solution view, switch to the repository/files view in your editor.

## Where to Work in the Starter Code
- Put your Week 13 implementation in `Playlist3`.
- Keep `Playlist1` and `Playlist2` available as your first two versions.
- Use `IPlaylist` in `Common` as the required contract.
- Add or update tests in `PlaylistTests`.
- Use `report.md` for your Week 13 reflection and comparison notes.
- Use `Menu` if you want manual testing, but do not rely on it as your only validation.

## Required Functional Coverage
Your functional tests should explicitly verify that `Playlist1`, `Playlist2`, and `Playlist3` all handle:

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
For Week 13, extend your performance tests so `Playlist1`, `Playlist2`, and `Playlist3` are all measured using the same operations and playlist sizes.

Reuse the same operations and sizes from Week 12 if possible so the comparison stays consistent. A good starting point is to compare at least:

- `AddSong`
- `RemoveSong`
- `PlayNext`
- `MoveSongUp`
- `MoveSongDown`

You may test more operations if you want, but keep the comparison consistent across all three implementations.

## What Good Evidence Looks Like
A strong Week 13 submission usually includes:

- Clear evidence that `Playlist3` matches the external behavior of the first two implementations
- Functional tests that run against all three implementations
- Performance results collected with the same operations and sizes for all three implementations
- A short write-up that explains what changed and what the three-way comparison suggests
- Code, tests, and report notes that are ready to polish for final submission

## Peer Review This Week
During Week 13, you will go through a review process with another student.

Use that review to:

- Check whether your tests and performance comparisons are clear and complete
- Find missing edge cases or unclear report explanations
- Catch project organization problems before the final due date
- Improve your final recommendation using outside feedback

Use the [Peer Review Guide](review) during the in-class review activity.

## Looking Ahead to the Final Submission
Before the final submission, you should:

- Review your code, tests, and report after any peer feedback
- Finish your recommendation in `report.md`
- Make sure your final repository clearly shows all three implementations and the final comparison

The only submission after Week 13 is the **final project submission** at the beginning of **Week 14**.

## Reminder
All three implementations (Weeks 11-13) must keep the **same external behavior**. Only the internal data structure should change.

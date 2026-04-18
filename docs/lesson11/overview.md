---
layout: default
title: "W11 Final Project"
---

# Final Project: Playlist Feature with Multiple Data Structures

## Overview

In this final project, you will implement the same **playlist feature** three times using different data structures. The goal is to compare how the underlying structure affects code design, correctness, and performance.

You will:
- **Implement** the feature for each data structure.
- **Write functional unit tests** to verify that each implementation works correctly.
- **Measure and compare performance** once you have multiple implementations to compare.
- Write a final **recommendation report** explaining which data structure you would choose if you were developing this feature at a real company.

Use this page for the big-picture project description. For the Week 11 checkpoint, see [W11 Prove: Final Project - Part 1](prove). For official behavior rules and edge cases, see the [Playlist Final Project FAQ](prove-faq).

---

## Project Context

You are working for a company developing a simple music application. You have been tasked with adding a **playlist** feature. Your playlist should allow you to:

- Add a song to the playlist.
- Remove a song from the playlist.
- Play the next song.
- Reset playback back to the beginning.
- Move a song up or down in the playlist order.
- Display the full playlist in order.
- Report the current playlist length.

All three implementations must keep the **same external behavior**. Only the internal data structure should change from week to week.

---

## Repository

#### Step 1: [Create your assignment repository](prove-classroom){:target="_blank"}

#### Step 2: [Accept repository invite to resolve Access Issues](https://github.com/settings/organizations){:target="_blank"}

---

## Starter Code

The starter repository includes:

- `Playlist1` for the Week 11 array/list version
- `Playlist2` for the Week 12 linked-list version
- `Playlist3` for the Week 13 BST/dictionary version
- `PlaylistTests` for your functional and performance tests
- `report.md` for your weekly reflections and final recommendation report
- `Common` for shared types such as `IPlaylist`, `Song`, and `Menu`
- `PlaylistExample` for an example of implementing the `IPlaylist` interface and running the `Menu`

---

## Timeline & Weekly Roadmap

### ✅ Week 11: Playlist using an Array/List

**Goal:** Implement `IPlaylist` in `Playlist1` using a built-in array or list.

**Tasks:**
- Build the first working version of the playlist feature.
- Build functional unit tests for the required behavior and edge cases.
- Make sure your tests verify the array/list version through the `IPlaylist` behavior.
- Record a short Week 11 write-up in `report.md` describing your implementation, edge cases, and any important assumptions.
- Submit Draft 1 / the Week 11 prove.

For detailed Week 11 expectations, see [W11 Prove: Final Project - Part 1](prove).

- 📌 **Draft submission due at the end of Week 11**

---

### ✅ Week 12: Playlist using a Linked List

**Goal:** Implement the same external behavior in `Playlist2` using a linked list.

**Tasks:**
- Rebuild the playlist with a linked-list-based approach.
- Keep the same visible behavior as Week 11.
- Make sure your functional unit tests also cover the linked-list version.
- Add performance tests that compare the array/list version and the linked-list version using the same operations and playlist sizes.
- Update `report.md` with what changed between the first two implementations and what your first performance results suggest.
- Submit Draft 2.
- 📌 **Draft submission due at the end of Week 12**

---

### ✅ Week 13: Playlist using a Binary Search Tree (BST) or Dictionary

**Goal:** Implement the same external behavior in `Playlist3` using a BST or dictionary.

**Tasks:**
- Design the final version of the playlist feature.
- Keep the same visible behavior as the first two versions.
- Add the third implementation to your functional tests to verify it works the same as the other two versions.
- Add the third implementation to your performance tests so all three versions are measured using the same operations and sizes.
- Update `report.md` to include all three implementations and prepare your final recommendation.

---

## Final Write-Up (Due Monday of Week 14)

In addition to your code, tests, and performance results, you will write a final recommendation report in `report.md` that includes:

- A **comparison table or chart** showing the performance of the three data structures for key operations (add, remove, search, move).
- A **short discussion** of trade-offs you observed (speed, simplicity, etc.).
- A clear **recommendation**:
  > *If you were working at a real company building this music application, which data structure would you use for the playlist feature?*  
  > Explain why your choice would be appropriate in a professional setting (consider performance, code maintainability, real user needs, and expected usage patterns).

---

## Final Deliverables Checklist

- [ ] All source code with clear structure and comments.
- [ ] Unit tests for all three implementations.
- [ ] Performance tests and results comparing all three implementations.
- [ ] Draft 1 for Week 11: array/list implementation plus functional tests.
- [ ] Draft 2 for Week 12: linked-list implementation plus performance comparison of the first two versions.
- [ ] Peer review on each other's results and report (in-class on Week 13).
- [ ] Final write-up with performance comparison and recommendation.
- [ ] Submit the link to your repository in Canvas by Week 14 Monday night

---

## Tips for Success

- Use clear class and method names.
- Build your functional tests early so you can reuse them across implementations.
- Keep your performance tests simple but repeatable once you begin them in Week 12.
- Keep your three implementations behaviorally consistent.
- Cite any sources if you reuse code snippets.
- Use clear visuals (tables or charts) in your final report.
- If you need help formatting `report.md`, see [Using Markdown Language](prepare-markdown).
- Use the [FAQ](prove-faq) whenever you are unsure about exact behavior.

---

**Have fun exploring!**  
See how much your data structure choices matter in real-world software design.

---
layout: default
title: "W11 Final Project"
---

# Final Project: Playlist Feature with Multiple Data Structures

## Overview

In this final project, you will implement the same **playlist feature** three times — each time using a different data structure we’ve discussed in class. This will help you understand the trade-offs between different data structures when solving real-world problems.

You will:
- **Implement** the feature for each data structure.
- **Write functional unit tests** to verify that it works.
- **Measure and compare performance** (using Big O notation) for key operations.
- Write a final **recommendation report** explaining which data structure you would choose if you were developing this feature at a real company.

---

## Project Context

You are working for a company developing a simple music application. You have been tasked with adding a **playlist** feature. Your playlist should allow you to:

- Add a song to the playlist.
- Remove a song from the playlist.
- Play the next song.
- Move a song up or down in the playlist order.
- Display the full playlist in order.

---

## Repository

#### Step 1: [Create your assignment repository](prove-classroom){:target="_blank"}

#### Step 2: [Accept repository invite to resolve Access Issues](https://github.com/settings/organizations){:target="_blank"}

---

## Timeline & Weekly Expectations

### ✅ Week 11: Playlist using an Array/List

**Goal:** Implement the playlist using a built-in array or list.

**Tasks:**
- Design a `Playlist` class that uses a list or array internally.
- Implement:
  - `AddSong(song)`
  - `RemoveSong(song)`
  - `PlayNext()`
  - `MoveSongUp(song)`
  - `MoveSongDown(song)`
  - `ShowPlaylist()`
- Write unit tests for each operation.
- Write a short performance test:
  - Measure time to add, remove, and move songs for small vs. large playlists (e.g., 10 vs. 10,000 songs).
- Write a brief reflection in [report.md](report.md) for this version.
- 📌 **Draft submission due at the end of Week 11**

---

### ✅ Week 12: Playlist using a Linked List

**Goal:** Implement the playlist using a **linked list**.

**Tasks:**
- Design a `Playlist` class that uses a custom linked list.
- Implement the same operations as Week 11.
- Write unit tests for each operation.
- Write performance tests comparing:
  - Insert/removal speed at various positions.
  - How does it compare to the list-based version?
- Write a brief reflection in [report.md](report.md) for this version.
- 📌 **Draft submission due at the end of Week 12**

---

### ✅ Week 13: Playlist using a Binary Search Tree (BST) or Dictionary

**Goal:** Implement the playlist using a **BST** or **Dictionary**, to support faster search or ordering by song title or ID.

**Tasks:**
- Design a `Playlist` class that uses a BST or Dictionary.
- Think creatively: maybe the BST orders songs alphabetically, or by play count.
- Implement the same core operations, adjusting for the new structure.
- Write unit tests.
- Write performance tests:
  - How fast can you find, add, and remove songs?
  - How does search performance compare to the other structures?
- Write a short reflection in [report.md](report.md) for this version.

---

## 📝 Final Write-Up (Due Monday of Week 14)

In addition to your code, tests, and performance results, you will write a **final recommendation report** in [report.md](report.md) that includes:

- A **comparison table or chart** showing the performance of the three data structures for key operations (add, remove, search, move).
- A **short discussion** of trade-offs you observed (speed, memory usage, simplicity).
- A clear **recommendation**:
  > *If you were working at a real company building this music application, which data structure would you use for the playlist feature?*  
  > Explain why your choice would be appropriate in a professional setting (consider performance, code maintainability, real user needs, and expected usage patterns).

---

## 📌 Final Deliverables Checklist (Due Monday of Week 14)

- [ ] All source code with clear structure and comments.
- [ ] Unit tests for all three implementations.
- [ ] Performance tests and results.
- [ ] Draft submissions for the first 2 implementations (Weeks 11 & 12).
- [ ] Peer review on each other's results and report (in-class on Week 13).
- [ ] Final write-up with performance comparison and recommendation.
- [ ] Submit the link to your repository in Canvas by Week 14 Monday night

---

## ✨ Tips for Success

- Use clear class and method names.
- Keep your performance tests simple but repeatable.
- Feel free to add extra features (shuffle, repeat) if you have time.
- Cite any sources if you reuse code snippets.
- Use clear visuals (tables or charts) in your final report.
- See [Hints & Helps](prepare-hints) for additional guidance.

---

## 📊 Grading

##### Points Breakdown

| Area                            | Criteria            |         Points |
|---------------------------------|---------------------|---------------:|
| Week 11 Draft                   | 90% Completed       |     **50 pts** |
| Week 12 Draft                   | 90% Completed       |     **50 pts** |
| Week 13 In-class Peer Review    | Reviewed a Peer     |     **50 pts** |
| Array / List Implementation     | Feature Implemented |    **100 pts** |
|                                 | Functional Tests    |     **50 pts** |
|                                 | Performance Tests   |     **50 pts** |
|                                 | Write-up Summary    |     **50 pts** |
| Linked List Implementation      | Feature Implemented |    **100 pts** |
|                                 | Functional Tests    |     **50 pts** |
|                                 | Performance Tests   |     **50 pts** |
|                                 | Write-up Summary    |     **50 pts** |
| BST / Dictionary Implementation | Feature Implemented |    **100 pts** |
|                                 | Functional Tests    |     **50 pts** |
|                                 | Performance Tests   |     **50 pts** |
|                                 | Write-up Summary    |     **50 pts** |
| Final Write Up                  | Recommendations     |    **100 pts** |
|                                 | ***Total***         | ***1000 pts*** |

---

**Have fun exploring!**  
See how much your data structure choices matter in real-world software design.

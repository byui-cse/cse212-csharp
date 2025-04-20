---
layout: default
title: "W10 Prepare: Reading"
---

# W10 Prepare: Reading

## Table of Contents

* [Heaps](#Heaps)
* [Heap Organization](#heap-organization)
	* [Complete Binary Tree](#binary-search-trees)
	* [Parents Come First](#balanced-binary-search-trees)
* [Heap Operations ](#bst-operations)
* [Uses](#uses)
* [Key Terms](#key-terms)

## Heaps

A heap is another data structure built using a **binary tree**; however, it is organized differently than a **binary search tree**. The heap relies on data that can be sorted to provide the first item from the collection of items. Usually, this item is either the minimum or maximum value. A heap that provides the minimum value item is called a **min-heap** while a heap that provides the maximum value item is called a **max-heap**.

{% include plain-image.html url="heap-header.jpg"
description="Shows a Min Heap where the value of the root node is 3 and all children nodes have higher values than their parent nodes."
caption="Min Heap"
%}

## Heap Organization

There are two rules for a binary tree to be a heap:

1. The binary tree must be a **complete** binary tree.
2. Parent nodes must come before child nodes when comparing the two.

### Complete Binary Tree

A complete binary tree means that each level of the tree must be filled before adding a new level. The level must be filled from left to right.

<!--- Figure 1 -->
{% include image.html url="complete_binary_tree.png"
description="Shows two trees, the one on the left is incomplete, while the one on the right is complete."
caption="Incomplete vs Complete Binary Tree"
%}


### Parents Come First

This rule applies to every node individually. The children of every parent node must come after the parent in sorted order. The level of the tree does not indicate any ordering other than the first item in the heap is at the root and that every child comes after its parent.

For a **min-heap**, if a child node exists, the child node must contain a value that is greater than or equal to the parent node. In a **min-heap**, the minimum value has the comes first and will therefore always be found in the root node of the tree. Conversely, a **max-heap** will have the highest value come first and all children will be lower than the root node's value.


#### Example

All examples will be shown using a **min-heap**, but they will apply to a **max-heap** by simply applying the reverse of the less than or greater than comparison.

<!--- Figure 2 -->
{% include image.html url="min_heap.png"
description="Shows a Min Heap where the value of the root node is 3 and all children nodes have higher values than their parent nodes."
caption="Min Heap"
%}

This **min-heap** follows both rules where each child has a higher value than its parent, and the binary tree is complete by filling in each level from left to right.

## Heap Operations

The heap data structure operations are:

* Bubble Up
* Bubble Down
* Add
* Remove
* Peek
* Size

To understand how these operations work, two recursive sub-operations need to be introduced: **bubble-up** and **bubble-down**

### Bubble Up

The bubble up operation is to evaluate if a child node is following the rule that it must come after its parent. This recursive operation will check if the child comes before the parent and if so, it will swap the parent and the child positions. Now that same child node is either the root or has a new parent. Repeat until there are no parents who come after this node. At most, this will swap every node from the bottom of the tree all the way to the root, which will be a function of the height of the tree which will result in **log(n)** operations.

Conceptually, if the first item was at the bottom of the tree, the bubble up operation will cause that first node to swap positions with each parent until it is at the root of the tree.

<!--- Figure 3 -->
{% include image.html url="bubble_up.png"
description="Shows a bubble up operation of the 8-node swapping places with the 33-node, then the 15-node so that the tree follows rule 1."
caption="Bubble Up of the 8-Node"
%}

```c#
private void BubbleUp(Node node)
{
    // TODO finish this
}
```

### Bubble Down

Bubble down is the opposite of bubble up. If a parent comes after either child, swap the parent and child positions. If both children come before the parent, it doesn't matter which child is swapped. Many implementations will swap with the child who comes first. The operation then recurses to check the new children if a swap occurred. At most, this will swap every node from the top of the tree all the way to one of the leaf nodes, which will be a function of the height of the tree which will result in **log(n)** operations.

Conceptually, this is where an item that sorts towards the end will sink down the tree until it reaches the bottom.

<!--- Figure 4 -->
{% include image.html url="bubble_down.png"
description="Shows a bubble down operation of the 33-node swapping places with the 3-node, then the 8-node, then the 15-node so that the tree follows rule 1."
caption="Bubble Down of the 33-Node"
%}

```c#
private void BubbleDown(Node node)
{
    // TODO finish this
}
```

### Add

The `Add` operation must follow both rules. We start by following rule 1 to make he tree complete, adding the new value at the bottom of the tree in the next available position. We then call `BubbleUp` on the newly added node to make the tree follow rule 2 so that the new value ends up at the correct spot in the heap.

<!--- Figure 5 -->
{% include image.html url="bubble_up.png"
description="Shows a bubble up operation of the 8-node swapping places with the 33-node, then the 15-node so that the tree follows rule 1."
caption="Adding the 8-Node"
%}

The `Add` operation takes one operation to add the new node, and then calls `BubbleUp`, so the overall efficiency is **O(log n)**.

```c#
private void Add(int value)
{
    // TODO finish this
}
```

### Remove

The `Remove` operation also must follow both rules. We start by removing the first node, which is always the root node. To follow rule 1 to make sure our binary tree stays complete, we replace the root node with the last node in the complete tree. This ensures we still follow rule 1 of having a complete tree. We then call `BubbleDown` on the new root node to make the tree follow rule 2 that every parent comes before its children.

<!--- Figure 6 -->
{% include image.html url="remove.png"
description="Shows a remove operation of the 2-node, replacing the root with the last node of the tree (33-node)."
caption="Removing the 2-Node"
%}

<!--- Figure 7 -->
{% include image.html url="bubble_down.png"
description="Shows a bubble down operation of the 33-node swapping places with the 3-node, then the 8-node, then the 15-node so that the tree follows rule 1."
caption="Bubble Down of the 33-Node"
%}

The `Remove` operation takes only a few operations to remove the node and replace it with the node from the bottom of the heap, but because it relies on `BubbleDown`, the overall efficiency is **O(log n)**.

```c#
private int Remove()
{
    // TODO finish this
}
```

### Peek

The `Peek` operation will return the first item of the heap found at the root node. Reading the root value will always be **O(1)** regardless of the size of the tree.

```c#
private int Peek()
{
    // return the root value
    return _root.Data;
}
```

### Size

The `Size` operation returns the number of nodes in the tree. As this value can be incremented when a value is added, the efficiency is **O(1)**

### Performance Summary

The table below shows the common functions of a Heap.

| Common Heap Operation | Description                                               | Performance                                                                             |
|-----------------------|-----------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Add(value)            | Adds a value into the heap in the correct place.          | O(log n) - Recursively swap values until the value is in the right spot.                |
| Remove()              | Remove the first value from the heap and return it.       | O(log n) - Recursively swap so the tree stays complete and all values follow the rules. |
| Peek()                | Return the first value from the heap without removing it. | O(1) - Looking at the root node only.                                                   |
| Size()                | Return the size of the Heap.                              | O(1) - The size is maintained within the Heap class.                                    |

## Uses

Heaps are efficient data structures that can order data as they receive data. Because of this characteristic, they are most commonly used for **Priority Queues**. If you used a linked list for a priority queue, you can append to it in O(1), but it would take O(n) to identify and return the highest priority item (first when sorting by priority). The heap would take O(log n) to add the item, but it could remove the next item from the queue in O(log n) as well.

One downside to heaps is that they are not ordered. The first item is known, but any of the leaf nodes could be the last item. This also creates a challenge when creating a priority queue because you need to keep track of the order the items were entered in addition to the priority of each item. By default, a heap would treat two items with the same priority as equivalent - either one could come first.

## Key Terms

<dl>
<dt>binary search tree</dt>
<dd>A binary tree that puts data less than the root to the left and greater than the root to the right. This type of tree enables searching algorithms to be efficient.</dd>
<dt>binary tree</dt>
<dd>A tree that has up to two children for each node.</dd>
<dt>complete binary tree</dt>
<dd>A binary tree that fills every available place for a node before starting a new level.</dd>
<dt>child</dt>
<dd>A child is a node connected from a parent node.</dd>
<dt>heap</dt>
<dd>A tree where each parent node comes before either of their children in sorted order.</dd>
<dt>leaf</dt>
<dd>A leaf is a node that has no children.</dd>
<dt>max heap</dt>
<dd>A heap where the root node is the maximum value.</dd>
<dt>min heap</dt>
<dd>A heap where the root node is the minimum value.</dd>
<dt>node</dt>
<dd>An entry in a tree that contains both the value and pointers to any children nodes.</dd>
<dt>parent</dt>
<dd>A parent is a node that connects to children nodes.</dd>
<dt>priority queue</dt>
<dd>A queue that returns data in order it was received according to priority</dd>
<dt>root</dt>
<dd>The first parent in a tree.</dd>
<dt>subtree</dt>
<dd>Subset of a tree made by selecting a node to be the root and including all the children from that node.</dd>
<dt>trees</dt>
<dd>A data structure that starts with a root node and is subsequently connected to multiple nodes according to a relationship between the nodes. The tree does not have any circular loops or unconnected nodes.</dd>
</dl>

---
layout: default
title: "W09 Prepare: Reading"
---

# W10 Prepare: Reading

## Table of Contents
* [Trees](#trees)
	* [Binary Trees](#binary-trees)
	* [Binary Search Trees](#binary-search-trees)
	* [Balanced Binary Search Trees](#balanced-binary-search-trees)
* [BST Operations ](#bst-operations)
	* [Inserting into a BST](#inserting-into-a-bst)
	* [Traversing a BST](#traversing-a-bst)
	* [BST in C#](#bst-in-c)
* [Key Terms](#key-terms)

## Heaps

A heap is another data structure built using a binary tree; however, it is organized differently than a **binary search tree**. The heap provides the highest priority item from the collection of items. Usually this item is either the minimum or maximum value. A heap that provides the minimum value item is called a **min-heap** while a heap that provides the maximum value item is called a **max-heap**.

### Heap Organization

There are two rules for a binary tree to be a heap:

1. The binary tree must be a **complete** binary tree.
2. Each node's children must be a lower priority than the node.

#### Rule 1—Complete Binary Tree

A complete binary tree means that each level of the tree must be filled before adding a new level. The level must be filled from left to right.

#### Rule 2—Lower Priority Children

Each node contains a value. For a **min-heap**, if a child node exists, the child node must contain a value that is greater than or equal to the parent node. In a **min-heap**, the minimum value has the highest priority and will therefore always be found in the root node of the tree. Conversely, a **max-heap** will have the highest value as its highest priority and all children will be lower than the root node's value.

This rule applies to every node individually. The level of the tree does not indicate the priority of a particular item—only that the highest priority item is at the root and that every child has a lower priority than its parent.

#### Example

All examples will be shown using a **min-heap**, but they will apply to a **max-heap** by simply applying the reverse of the less than or greater than comparison.

<!--- Figure 1-->
{% include image.html url="min_heap.png"
description="Shows a Min Heap where the value of the root node is 3 and all children nodes have higher values than their parent nodes."
caption="Min Heap"
%}

This **min-heap** follows both rules where each child has a higher value than its parent, and the binary tree is complete by filling in each level from left to right.

## Heap Operations

The heap data structure operations are:

* Insert
* Remove
* Peek
* Size

To understand how these operations work, two recursive sub-operations need to be introduced: **bubble-up** and **bubble-down**

#### Bubble Up

Bubble up means that if a child node has a higher priority than its parent, you swap the parent and child positions. Then, reevaluate by looking at the next parent until [Rule #2](#rule-2lower-priority-children) is obeyed. At most, this will swap every node from the bottom of the tree all the way to the root, which will be **log(n)** operations.

Conceptually, if the highest priority item was at the bottom of the tree, the bubble up operation will cause that high priority node to swap positions with each parent until it is at the root of the tree.

<!--- Figure 2-->
{% include image.html url="bubble_up.png"
description="Shows a bubble up operation of the 8-node swapping places with the 33-node, then the 15-node so that the tree follows rule #1."
caption="Bubble Up of the 8-Node"
%}

```c#
private void BubbleUp(Node node)
{
    // TODO finish this
}
```

#### Bubble Down

Bubble down is the opposite of bubble up. If a parent has a lower priority than either child, swap the parent and child positions. Then reevaluate by looking at the new children until [Rule #2](#rule-2lower-priority-children) is obeyed. At most, this will swap every node from the top of the tree all the way to the leaf node, which will be **log(n)** operations.

Conceptually, this is where a low priority item sinks down the tree until it reaches the bottom.

<!--- Figure 3-->
{% include image.html url="bubble_down.png"
description="Shows a bubble down operation of the 33-node swapping places with the 3-node, then the 8-node, then the 15-node so that the tree follows rule #1."
caption="Bubble Down of the 33-Node"
%}

```c#
private void BubbleDown(Node node)
{
    // TODO finish this
}
```

### Insert

The `Insert` operation must follow both rules. We start by following [Rule #1](#rule-1complete-binary-tree), inserting the new value at the bottom of the tree in the next available position. We then call `BubbleUp` on the newly inserted node to make the tree follow [Rule #2](#rule-2lower-priority-children) as well. The tree is now balanced.

<!--- Figure 4-->
{% include image.html url="bubble_up.png"
description="Shows a bubble up operation of the 8-node swapping places with the 33-node, then the 15-node so that the tree follows rule #1."
caption="Inserting the 8-Node"
%}

The `Insert` operation relies on `BubbleUp`, so the efficiency is **O(log n)**.

```c#
private void Insert(int value)
{
    // TODO finish this
}
```

### Remove

The `Remove` operation also must follow both rules. We start by removing the highest priority node, which is always the root node. To follow [Rule #1](#rule-1complete-binary-tree), we replace the root node with the last node in the complete tree. This ensures we still follow [Rule #1](#rule-1complete-binary-tree). We then call `BubbleDown` on the new root node to make the tree follow [Rule #2](#rule-2lower-priority-children) as well. The tree is now balanced.

<!--- Figure 5-->
{% include image.html url="remove.png"
description="Shows a remove operation of the 2-node, replacing the root with the last node of the tree (33-node)."
caption="Removing the 2-Node"
%}

<!--- Figure 6-->
{% include image.html url="bubble_down.png"
description="Shows a bubble down operation of the 33-node swapping places with the 3-node, then the 8-node, then the 15-node so that the tree follows rule #1."
caption="Bubble Down of the 33-Node"
%}

The `Remove` operation relies on `BubbleDown`, so the efficiency is **O(log n)**.

```c#
private int Remove()
{
    // TODO finish this
}
```

### Peek

The `Peek` operation will simply return the value of the root node as that is the highest priority item. Reading the root value will always be **O(1)** regardless of the size of the tree.

```c#
private int Peek()
{
    // return the root value
    return _root.Data;
}
```

### Size

The `Size` operation returns the number of nodes in the tree. As this value can be incremented when a value is inserted, the efficiency is **O(1)**

## Performance Summary

The table below shows the common functions of a Heap.

| Common BST Operation | Description                                                                               | Performance                                                              |
|----------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| insert(value)        | Insert a value into the heap.                                                             | O(log n) - Recursively swap values until the tree is balanced            |
| remove()             | Remove the highest priority value from the heap and return it.                            | O(log n) - Rebalance the tree so that it's ready for the next operation. |
| size()               | Return the size of the Heap.                                                              | O(1) - The size is maintained within the Heap class.                     |
| empty()              | Returns true if the root node is empty. This can also be done by checking the size for 0. | O(1) - The comparison of the root node or the size.                      |

## Key Terms

<dl>
<dt>AVL Tree</dt>
<dd>Adelson-Velskii and Landis Tree. A balanced binary search tree that is checked unbalanced height after every modification to the tree. If the tree is unbalanced, then pre-determined algorithms are used to balance the tree.</dd>
<dt>balanced</dt>
<dd>A tree is balanced if the height of the tree from the root to each leaf is consistent for all subtrees. The measure of consistency will vary between algorithms but usually does not exceed a height difference of 1.</dd>
<dt>balanced binary search tree</dt>
<dd>A binary search tree which is balanced or restructured to be balanced. A balanced binary search tree has O(log n) performance when searching.</dd>
<dt>binary search tree</dt>
<dd>A binary tree that puts data less than the root to the left and greater than the root to the right. This type of tree enables searching algorithms to be efficient.</dd>
<dt>binary tree</dt>
<dd>A tree that has up to two children for each node.</dd>
<dt>child</dt>
<dd>A child is a node connected from a parent node.</dd>
<dt>leaf</dt>
<dd>A leaf is a node that has no children.</dd>
<dt>node</dt>
<dd>An entry in a tree that contains both the value and pointers to any children nodes.</dd>
<dt>parent</dt>
<dd>A parent is a node that connects to children nodes.</dd>
<dt>Red Black Tree</dt>
<dd>A self-balancing binary search tree.</dd>
<dt>root</dt>
<dd>The first parent in a tree.</dd>
<dt>subtree</dt>
<dd>Subset of a tree made by selecting a node to be the root and including all the children from that node.</dd>
<dt>traverse</dt>
<dd>The process of visiting all nodes (and subsequently their values) in a tree. Used frequently with a binary search tree using recursion to start at the leaf node that contains the smallest value and going to the leaf node that contains the largest value.</dd>
<dt>trees</dt>
<dd>A data structure that starts with a root node and is subsequently connected to multiple nodes according to a relationship between the nodes. The tree does not have any circular loops or unconnected nodes.</dd>
</dl>

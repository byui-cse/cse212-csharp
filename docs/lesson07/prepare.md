---
layout: default
title: "W07 Prepare: Reading"
---


# W07 Prepare: Reading
## Table of Contents
* [Linked Lists]()
    * [Linked List Structure](#linked-list-structure)
    * [Adding to a Linked List](#adding-to-a-linked-list)
    * [Removing from a Linked List](#removing-from-a-linked-list)
    * [Accessing from a Linked List](#accessing-from-a-linked-list)
    * [Linked Lists in C#](#linked-lists-in-c)
    * [Comparing Dynamic Array and Linked List](#comparing-dynamic-array-and-linked-list)
* [Key Terms](#key-terms)

## Linked Lists

### Linked List Structure
When we learned about the dynamic array, we saw that it was characterized by contiguous memory. Each item in a dynamic array is right next to the next item in memory. This allowed for very quick access to items in the dynamic array because memory addresses of each item could be calculated from a formula (address = startingAddress + (index * itemSize)). The queue, stack, set, and map were all based on memory organized in this way.


<!--- Figure 1 -->
{% include image.html url="dynamic_array_not_full.jpg"
description="Shows a dynamic array with capacity 8 and size 7.  Indices 0 through 6 are populated with 8, 12, 31, 15, 4, 42, and 27."
caption="Dynamic Array"
%}

A collection of data can also be stored in a random way within memory. A **linked list** is organized in this way. With a linked list, each element in the list is at some location in memory. There is no guarantee that one element will be next to another element. In order to keep our list together, each element (which we will call a **node**) will contain both the **value** and a link to the **next** node in the list. Specifically, the link will be a **pointer** to the location in memory that contains our next element.


<!--- Figure 2 -->
{% include image.html url="linked_list.jpg"
description="Shows a linked list made up of 5 nodes.  Each node has a value and a NEXT that points to the next node.  The HEAD is pointing to the first node.  The nodes have the following values in order: 8, 12, 31, 15, 4."
caption="Linked List"
%}

In the linked list shown above, the first node is called the **head**. If you know where the head is, then you can traverse the entire linked list by following the pointers. Most linked lists maintain a bi-directional linking between nodes. Bi-directional means that each node will maintain a pointer to both the next node and **previous node**. The **doubly-linked list** shown below has both a head and a **tail**.

<!--- Figure 3 -->
{% include image.html url="linked_list_double.jpg"
description="Shows a doubly linked list made up of 5 nodes.  Each node has a value, a NEXT that points to the next node, and a PREV that points to the previous node.  The HEAD is pointing to the first node and the TAIL is pointing to the last node.  The nodes have the following values in order: 8, 12, 31, 15, 4."
caption="Doubly-Linked List"
%}

## Adding to a Linked List

Unlike inserting into a dynamic array where we had to worry about moving items over towards the end to maintain contiguous memory, the act of inserting into a linked list only has an effect on its neighboring elements. Additionally, since we are going to use pointers to connect the nodes together, there is no need to think about things such as capacity or growing the list like we did with a dynamic array. There are three scenarios to consider: adding at the first, the last, and somewhere in the middle.

Adding to the first usually requires a four step process:

1. Create a new node (we will call it `newNode`)
2. Set the "next" of the new node to the current head (`newNode.Next = head`)
3. Set the "prev" of the current head to the new node (`head.Prev = newNode`)
4. Set the head equal to the new node (`head = newNode`)

<!--- Figure 4 -->
{% include image.html url="linked_list_add_first.jpg"
description="Shows a doubly linked list made up of 5 nodes with values of 8, 12, 31, 15, and 4.  The four step process to add 42 to the beginning (HEAD) is shown: 1) Create a new node with value 42; 2) Connect NEXT of the new node to the node with value 8 (the HEAD); 3) Connect PREV from the node containing 8 to the new node; 4) Set HEAD equal to the new node."
caption="Inserting at the Head of Linked List"
%}

There is a special case that exists for inserting at the head (and also inserting at the tail). If the linked list is empty (`head == null`) then all we have to do is set both the head and the tail to the new node we created.

Inserting at the tail is similar to inserting at the head. The same four steps are followed but with respect to the tail the following should happen:

1. Create a new node (we will call it `newNode`)
2. Set the "prev" of the new node to the current tail (`newNode.Prev = tail`)
3. Set the "next" of the current tail to the new node (`tail.Next = newNode`)
4. Set the tail equal to the new node (`tail = newNode`)

<!--- Figure 5 -->
{% include image.html url="linked_list_add_last.jpg"
description="Shows a doubly linked list made up of 5 nodes with values of 8, 12, 31, 15, and 4.  The four step process to add 23 to the end (TAIL) is shown: 1) Create a new node with value 23; 2) Connect PREV of the new node to the node with value 4 (the TAIL); 3) Connect NEXT from the node containing 4 to the new node; 4) Set TAIL equal to the new node."
caption="Inserting at the Tail of a Linked List"
%}

The process for inserting into the middle is a little more complicated. In the picture below, we are trying to insert after node `current`. The process involves five steps as follows:

1. Create a new node (we will call it `newNode`)
2. Set the "prev" of the new node to the current node (`newNode.Prev = current`)
3. Set the "next" of the new node to the next node after current (`newNode.Next = current.Next`)
4. Set the "prev" of the "next" node after current to the new node (`current.Next.Prev = newNode`)
5. Set the next of the current node to the new node (`current.Next = newNode`)

<!--- Figure 6  -->
{% include image.html url="linked_list_add_after.jpg"
description="Shows a doubly linked list made up of 5 nodes with values of 8, 12, 31, 15, and 4.  The four step process to add 50 after the node with 31 (called CURRENT NODE) is shown: 1) Create a new node with value 50; 2) Connect PREV of the new node to the CURRENT NODE; 3) Connect NEXT from the new node to the node after CURRENT NODE (15); 4) Set the PREV of the node after CURRENT NODE to the new node; 5) Set the NEXT of the CURRENT NODE to the new node."
caption="Inserting in the Middle of a Linked List"
%}

## Removing from a Linked List

Removing the first (the head) or the last (this tail) node from a linked list is similar and involve setting updating the second node (or the second to last node in the case of removing from the tail). The process for removing the first node is as follows:

1. Set the "prev" of the second node (`head.Next`) to nothing (`head.Next.Prev = null`)
2. Set the head to be the second node (`head = head.Next`)

As a special case, if there was only one node in the linked list, the head and tail would need to be set to `null` thus creating an empty linked list.

<!--- Figure 7  -->
{% include image.html url="linked_list_remove_first.jpg"
description="Shows a doubly linked list made up of 5 nodes with values of 8, 12, 31, 15, and 4.  The two step process to remove 8 (HEAD): 1) Set the PREV of the second node (12) to nothing; 2) Set the HEAD to the second node."
caption="Remove the first element from the Linked List"
%}

The process for removing the last node is as follows:

1. Set the "next" of the second to last node (`tail.Prev`) to nothing (`tail.Prev.Next = null`)
2. Set the tail to be the second to last node (`tail = tail.Prev`)

<!--- Figure 8-->
{% include image.html url="linked_list_remove_last.jpg"
description="Shows a doubly linked list made up of 5 nodes with values of 8, 12, 31, 15, and 4.  The two step process to remove 4 (TAIL): 1) Set the NEXT of the second to last node (15) to nothing; 2) Set the TAIL to the second to last node."
caption="Remove the last element from the Linked List"
%}

The process to remove from the middle is not as complicated as inserting from the middle. In the picture below, we are trying to remove the node `current`. The process involves two steps:

1. Set the prev of the node after current to the node before current (`current.Next.Prev = current.Prev`)
2. Set the next of the node before current to the node after current (`current.Prev.Next = current.Next`)

<!--- Figure 9-->
{% include image.html url="linked_list_remove_middle.jpg"
description="Shows a doubly linked list made up of 5 nodes with values of 8, 12, 31, 15, and 4.  The two step process to remove the node with 31 (called the CURRENT NODE): 1) Set the PREV of the node after the CURRENT NODE (15) to the node before the CURRENT NODE (12); 2) Set the NEXT of the node before the CURRENT NODE to the node after the CURRENT NODE."
caption="Remove from the middle of the Linked List"
%}

## Accessing from a Linked List

If we want to find a value in the linked list or if we want to find a specific node (e.g. the 3rd node or the 10th node), we are required to loop through the linked list. We can start at either the head (if we want to go forward through the list) or we can start at the tail (if we want to go backward through the list). To loop through the list, we will follow the "next" (or the "prev" if going backwards from tail) links until we get to the end. The following code shows the way to implement a basic traversal through a linked list by moving from node to node until you reach the `null` end.

```csharp
    private void GoForward() {
        // Start at the beginning (the head)
        var current = _head;
        
        // Loop until we have reached the end (null)
        while (current != null) {
            // Do something with the current node
            Console.WriteLine(current.Data);
            
            // Follow the pointer to the next node
            current = current.Next;
        }
    }
```

## Linked Lists in C#

In your assignment this week you will be writing your own linked list class. However, C# does include a linked list class `LinkedList<T>`. The table below shows the common functions in the `LinkedList`.

| Common Linked List Operation | Description                                          | C# Code | Performance |
|------------------------------|------------------------------------------------------|---------|-------------|
| InsertHead(value)            | Adds "value" before the head.                        | `linkedList.AddFirst(value)` | O(1) - Just need to adjust the pointers near the head. |
| InsertTail(value)            | Adds "value" after the tail.                         | `linkedList.AddLast(value)` | O(1) - Just need to adjust the pointers near the tail. |
| Insert(node, value)          | Adds "value" after node "node".                      | `linkedList.AddAfter(node, value)` | O(n) - It's not complicated to adjust the pointers to insert, but it takes a loop to find the node to insert after. |
| RemoveHead()                 | Removes the first item (the head).                   | `linkedList.RemoveFirst()` | O(1) - Just need to adjust the pointers near the head. |
| RemoveTail()                 | Removes the last item (the tail).                    | `linkedList.RemoveLast()` | O(1) - Just need to adjust the pointers near the tail. |
| Remove(node)                 | Removes node "node".                                 | `linkedList.Remove(node)` | O(n) - It's not complicated to adjust the pointers to remove, but it takes a loop to find the node to remove. |
| Size()                       | Return the size of the linked list.                  | `linkedList.Count` | O(1) - The size is maintained within the linked list class. |
| Empty()                      | Returns true if the size of the linked list is zero. | `linkedList.Count == 0` | O(1) - The comparison of the length with 0 is all that is needed. |

## Comparing Dynamic Array and Linked List

The dynamic array and linked list look the same to the user but because the memory is managed differently, the performance numbers are different. The table below compares these two data structures:

| Operation     | Dynamic Array | Linked List |
|---------------|---------------|-------------|
| Insert Front  | O(n)          | O(1)        |
| Insert Middle | O(n)          | O(n)        |
| Insert End    | O(1)          | O(1)        |
| Remove Front  | O(n)          | O(1)        |
| Remove Middle | O(n)          | O(n)        |
| Remove End    | O(1)          | O(1)        |

We can conclude the following:

* The dynamic array has good performance at the end.
* The linked list has good performance at the beginning and the end.

Thinking back about stacks and queues, the stack did the push and pop operations from the end. Therefore, a stack can use either a dynamic array or linked list equally well. However, since a queue did the enqueue and dequeue operations from the end and the front, a queue should always be implemented with a linked list.  This strong statement only applies when the size of the data is "large" (recall discussions earlier about big O). If we only have a small number of items in my queue, then both a dynamic array and linked list will run fast enough.

## Key Terms

<dl>
<dt>doubly-linked list</dt>
<dd>A linked list that is bi-directional. The linked list will maintain both a head and a tail. To traverse in either direction, the node will have both a pointer to the next node and the previous node. Access to both the head and tail is O(1).</dd>
<dt>head</dt>
<dd>A pointer to the first node in the linked list.</dd>
<dt>linked list</dt>
<dd>A data structure that keeps data in order but is not in contiguous memory. To get to the next (or previous) item in the list, pointers are maintained and followed. Access to the head is O(1).</dd>
<dt>next</dt>
<dd>A pointer in each node of the linked list that points to the next node.</dd>
<dt>node</dt>
<dd>The combination of the value and the pointers representing one item in the linked list.</dd>
<dt>pointer</dt>
<dd>Refers to an address in the computer memory. Also called a reference.</dd>
<dt>tail</dt>
<dd>A pointer to the last node in the linked list. If the list has only one item, then the head and tail are the same.</dd>
<dt>value</dt>
<dd>The actual data stored in the linked list as part of the node.</dd>
<dt>previous</dt>
<dd>A pointer in each of the linked list nodes that points to the previous node.</dd>
</dl>

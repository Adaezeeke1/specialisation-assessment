### Question 1.1:

The 'deque' class is part of the *collections* Python library.

### Question 1.2:

1. **Structure Cycle**

A tree is a type of graph that is connected, has no cycles or loops, and has a single root node. 
On the other hand, a graph can be connected or disconnected from other nodes, can have cycles or loops,
and does not necessarily have a root node.

2. **Node Relationships**

Trees have a hierarchical structure. In a tree, each node can have zero or more child nodes, 
and every node has exactly one parent, except the root node (which has no parent). On the other hand, 
graphs do not necessarily have a hierarchical structure. They can represent more complex relationships 
without the constraint of a single root node or a strict parent-child relationship. 
Thus, nodes can have any number of connections to other nodes 
(in various ways, including one-to-one, one-to-many, and many-to-many relationships.)

### Question 1.3:

**Time Complexity**

This refers to the amount of time an algorithm takes to complete as a function of the input size. 
It measures the number of basic operations (such as comparisons, assignments, arithmetic operations, etc.) 
performed by an algorithm relative to the size of the input data.

**Space Complexity**

This refers to the amount of memory space an algorithm requires to complete as a function of the input size. 
It measures the amount of memory used by the algorithm to store variables, data structures, and other information during its execution.

### Question 1.4:

Bubble Sort is a simple sorting algorithm that repeatedly steps through the elements of a list, 
compares adjacent elements, and swaps them if they are in the wrong order. 
The pass through the list is repeated until the list is sorted.
---
![Bubble Sort](http://www.computersciencebytes.com/wp-content/uploads/2016/10/bubble_sort.png)

---

Image Source: https://www.computersciencebytes.com/sorting-algorithms/bubble-sort/

The image above visually describes the bubble sort algorithm.

---

**Complexity**

The worst-case time complexity of the Bubble Sort algorithm is O(n^2), where "n" is the number of elements in the list. 
This is because in the worst case, you'll need to perform n passes, each requiring n comparisons and swaps.

The best-case time complexity is O(n) when the list is already sorted. However, in the average case, 
Bubble Sort still takes O(n^2), making it inefficient for large lists.

Its space complexity is O(1) as it does not require additional space apart from a temporary variable used for swapping.

**End of the First Pass**

At the end of the first pass, the largest element in the array is guaranteed to have moved to its correct position at the end of the array. 
This is because in each comparison, if the current element is greater than the next element, they are swapped. 
The largest element *"bubbles up"* to its correct place after each pass. 

However, only one element is guaranteed to be in its correct position after the first pass. 
The rest of the array might still be out of order, and further passes are needed to fully sort the array.

### Question 1.5:

LIFO and FIFO are two common methods for managing data in computer science, particularly in the context of data structures like stacks and queues. 
They determine how data is accessed and removed from these structures.

1. **LIFO (Last-In-First-Out)**:

LIFO, an abbreviation for *last in, first out*, is a method for handling data structures where the first element is processed last and the last element is processed first.
I think of it like a stack of plates: you place new plates on top and take them off the top as well. 
This behavior is implemented using a data structure called a **stack**. Stacks can be created using arrays or linked lists.
---
![LIFO](https://media.geeksforgeeks.org/wp-content/uploads/LIFO.jpg)

---
Image source: https://www.geeksforgeeks.org/lifo-last-in-first-out-approach-in-programming/

The image above visually describes the LIFO approach.

---

* **How LIFO Works with a Stack**:

**Push (Add)**: When you push an item onto the stack, it becomes the top item. This means it's the most recent addition and will be the first to be removed.

**Pop (Remove)**: Popping an item from the stack removes the top item, revealing the item that was added before it. 
The process continues in reverse chronological order, mimicking the LIFO behavior.

*Practical example*: Imagine a scenario where you are processing a list of web pages for an internet browser's "back" button.
As you navigate through different web pages, the URLs of these pages are added to a stack. 
If you press the "back" button, the most recent URL (last one added) is popped off the stack and used to load the previous page.


2. **FIFO (First-In-First-Out)**:

FIFO, an abbreviation for *first in, first out*, is a method for handling data structures where the first element is processed first and the newest element is processed last.
I think of it like a line of people waiting; the person who joined the line first will be the first to reach the front. 
This behavior is implemented using a data structure called a *queue*. Similar to stacks, queues can be created using arrays or linked lists.
---

![FIFO](https://media.geeksforgeeks.org/wp-content/uploads/FIFO.jpg)

---
Image source: https://www.geeksforgeeks.org/fifo-first-in-first-out-approach-in-programming/

The image above visually describes the FIFO approach.

---

* **How FIFO Works with a Queue**:

**Enqueue (Add)**: When you enqueue an item, it goes to the back of the queue. This item becomes the most recent addition but will be the last to be processed.

**Dequeue (Remove)**: Dequeuing an item removes the front item of the queue, exposing the item that has been waiting the longest. 
The process continues in the order of arrival, mimicking the FIFO behavior.

*Practical example*: Think about a printer queue. When multiple print jobs are sent to a printer, they are placed in a queue. 
The job that was sent first will be printed first, followed by the others in the order they were added to the queue.

### Question 1.6:

A Balanced Binary Tree is a type of binary tree data structure that satisfies these conditions:

* The height of the two subtrees of any node does not differ by more than 1.

* Both the left and right subtrees of each node are also balanced.

This ensures that the tree remains relatively balanced and prevents the tree from becoming heavily skewed to one side, which can lead to inefficient operations.

---

![Balanced Tree](https://cdn.programiz.com/sites/tutorial2program/files/balanced-binary-tree.png)

---
Image source: https://www.programiz.com/dsa/balanced-binary-tree

The image above displays a balanced binary tree.

---

One common type of balanced binary tree is the AVL tree (Adelson-Velsky and Landis tree), 
which enforces the height balance property using rotation operations whenever necessary during insertions and deletions. 
Another well-known type is the Red-Black tree, which maintains balance through a set of color and rotation rules.

For a Balanced Binary Tree, the best root (also known as the *root node*) is the one that allows the tree to be as balanced as possible. 
In other words, the ideal root is the one that ensures that the height difference between the left and right subtrees of the root is minimized. 
This way, the entire tree can achieve optimal balance, which leads to efficient operations like searching, insertion, and deletion.

**How searching works in a Balanced Binary Tree**:

* *Start at the Root*: You begin the search at the root of the tree. 
If the tree is balanced properly, you can reasonably expect the root to be close to the middle of the range of values in the tree.


* *Compare with the Root Value*: Compare the value you're searching for with the value stored in the root node.


* *Choose a Subtree*: Based on the comparison, you'll know whether the target value is smaller or larger than the root node's value. 
If it's smaller, you move to the left subtree; if it's larger, you move to the right subtree. 
This is where the balanced property becomes crucial. 
Since the tree is balanced, the height difference between the left and right subtrees should be small, minimizing the number of levels you need to traverse.


* *Repeat the Process*: Once you move to the appropriate subtree, repeat the process by comparing the target value with the value in the new node you've reached. 
Choose the appropriate subtree and continue until you either find the target value or reach a leaf node where the value is not present in the tree.

The balanced property ensures that the height of the tree remains logarithmic in relation to the number of nodes, resulting in efficient search times. 
This is because the height of the tree won't become skewed, which could lead to worst-case scenarios where the tree behaves more like a linked list, 
resulting in linear search times.






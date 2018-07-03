# Linked List
Like arrays, Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at contiguous location; the elements are linked using pointers.
+ A linked list is a linear collection of data elements, whose order is not given by their physical placement in memory. Instead, each element points to the next.
+ It is a data structure consisting of a collection of nodes which together represent a sequence. In its most basic form, each node contains: data, and a reference (in other words, a link) to the next node in the sequence.
+ This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration. More complex variants add additional links, allowing more efficient insertion or removal of nodes at arbitrary positions.
+ A drawback of linked lists is that access time is linear (and difficult to pipeline). Faster access, such as random access, is not feasible. Arrays have better cache locality compared to linked lists.

![linkedlist](https://www.geeksforgeeks.org/wp-content/uploads/gq/2013/03/Linkedlist.png)
---
##### Why Linked List?
Arrays can be used to store linear data of similar types, but arrays have following limitations.
1) The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage.
2) Inserting a new element in an array of elements is expensive, because room has to be created for the new elements and to create room existing elements have to shifted.
---
##### Advantages over arrays
1) Dynamic size
2) Ease of insertion/deletion
---
##### Drawbacks:
1) Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists.
2) Extra memory space for a pointer is required with each element of the list.
3) Not cache friendly. Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists.
---
## Types of Linked Lists
+ Singly Linked List- Singly linked lists contain nodes which have a data field as well as 'next' field, which points to the next node in line of nodes. Operations that can be performed on singly linked lists include insertion, deletion and traversal.

![linkedlist](https://sites.google.com/site/merasemester/_/rsrc/1299735495955/data-structures/linked-list/singly%20linked%20list.JPG)

+ Doubly linked list- In a 'doubly linked list', each node contains, besides the next-node link, a second link field pointing to the 'previous' node in the sequence. The two links may be called 'forward('s') and 'backwards', or 'next' and 'prev'('previous').A technique known as XOR-linking allows a doubly linked list to be implemented using a single link field in each node. However, this technique requires the ability to do bit operations on addresses, and therefore may not be available in some high-level languages.
Many modern operating systems use doubly linked lists to maintain references to active processes, threads, and other dynamic objects.A common strategy for rootkits to evade detection is to unlink themselves from these lists.

![doubly linked list](https://www.geeksforgeeks.org/wp-content/uploads/gq/2014/03/DLL1.png)

+ Multiply Linked list- In a 'multiply linked list', each node contains two or more link fields, each field being used to connect the same set of data records in a different order of same set(e.g., by name, by department, by date of birth, etc.). While doubly linked lists can be seen as special cases of multiply linked list, the fact that the two and more orders are opposite to each other leads to simpler and more efficient algorithms, so they are usually treated as a separate case.

![Multiply Linked List](https://1.bp.blogspot.com/-0mamW0g0aj4/WsdhArwUTCI/AAAAAAAACi4/Fx8YEYGb7zkJIJSxQEUTdNa-A9jbLyWaQCLcBGAs/s640/MLL.jpg)

+ Circular Linked List- In the last node of a list, the link field often contains a null reference, a special value used to indicate the lack of further nodes. A less common convention is to make it point to the first node of the list; in that case the list is said to be 'circular' or 'circularly linked'; otherwise it is said to be 'open' or 'linear'. It is a list where the last pointer points to the first node.
In the case of a circular doubly linked list, the first node also points to the last node of the list.

![Circular](http://www.worldbestlearningcenter.com/index_files/Circularly-linkedlist.png)

![Doubly Circular](https://omkarnathsingh.files.wordpress.com/2015/07/dcll.gif)

---

## Nomenclature 

+ Sentinel nodes
In some implementations an extra 'sentinel' or 'dummy' node may be added before the first data record or after the last one. This convention simplifies and accelerates some list-handling algorithms, by ensuring that all links can be safely dereferenced and that every list (even one that contains no data elements) always has a "first" and "last" node.

+ Empty lists
An empty list is a list that contains no data records. This is usually the same as saying that it has zero nodes. If sentinel nodes are being used, the list is usually said to be empty when it has only sentinel nodes.

+ Hash linking
The link fields need not be physically part of the nodes. If the data records are stored in an array and referenced by their indices, the link field may be stored in a separate array with the same indices as the data records.

+ List handles
Since a reference to the first node gives access to the whole list, that reference is often called the 'address', 'pointer', or 'handle' of the list. Algorithms that manipulate linked lists usually get such handles to the input lists and return the handles to the resulting lists. In fact, in the context of such algorithms, the word "list" often means "list handle". In some situations, however, it may be convenient to refer to a list by a handle that consists of two links, pointing to its first and last nodes.

+ Combining alternatives
The alternatives listed above may be arbitrarily combined in almost every way, so one may have circular doubly linked lists without sentinels, circular singly linked lists with sentinels, etc.

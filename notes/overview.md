Like arrays, linked lists are a type of data structure used to store sets of similar, related information. Unlike arrays, they do not require a contagious block of memory. This has advantages and disadvantages, which we’ll learn about as we explore how they are build and compare the two.

construct a linked list and compare the runtime of operations to an array to make the optimal choice between them.

The linked list data structure (both singly- and doubly-linked variants), while not used nearly as much as arrays, nonetheless is an important one for students to learn because it provides an alternative way to implement a data structure that students should be intimately familiar with at this point in the curriculum.

Whereas arrays store and index elements contiguously, each element of a linked list is stored in a node. Each node then has a reference (or a ‘pointer’) to the next node in the linked list. In this way, linked lists describe lists of things in a _recursive fashion_, while arrays describe lists of things in an _iterative_ fashion.

-stores each elements as isolated node 
-nodes point to next node in list
-versus array contiguous block of memmory. that can hold up certain amounts of item with certain space 
(static array instead of dynamic array)
-static array rep holds list (pre-allocated with certain ammount of space upfront) of things versus link list representation

-every node should point to the next

1st node-
head of link list

tail-
last node of link list
points to null/node
should only be one

N=null/none

class Node:
self.value= value (property)
self.next = next_node (property)

(tail always ponts to None instead of another node)

class LinkedList: *from this perspective, dont have direct access to any nodes in middle of list (BUT fast access to first ELEMENT in head and  last element in tail)
-2nd element in linkedList no knowledge of prev node that refered to it (can't go back to head) 
-tail not able to refer back to 2nd to last element
self.head = head_node
self.tail= tail_node

-Adding:
H12 > 39 >T5 > N
list.insert(15)

wrap 15 in linked list node T15 > N
in this case is the new tail (possible to be head when inserting)
-move 5 (self.next) node pointer to T15
-change tail reference to 15 

-How would you insert an element into an empty linked list?
what about a linked list with only one element?
-How would you iterate along a linked list to reach an element that isn't the head or tail of the list?
-How would you delete an lement from a linked list

DIFF 
-LINKED LISTS DONT STORE ELEMENTS CONTIGUOUSLY(next together in sequence) UNLIKE ARRAYS 
PROS : Easier to insert into & delete from the middle of the linked list compared to an array 
CON: not as cache-friendly since caches are optimized typically for contiguous memory access (ELEMENTS NOT STORED SEQ NEXT TO EACH OTHER)

LINKED LISTS DONT NEED TO BE ALLOCATED W/ STATIC AMOUNT OF MEMORY UP FRONT
PROS: We can keep adding elements to linked lists as much as we want, unlike arrays with a static amount of allocated memory
B/C DONT HAVE TO WORRY ABOUT HOW MUCH SPACE NEEDED TO ALLOCATE TO THAT LINKED LIST 
JUST needs enough MEMORY TO WRAP NEW ELEMENT IN NEW NODE & THEN HAVE OLD LAST NODE IN LIST REFERENCE NEW LAST NODE IN LIST 
SO REFERENCES NOT TAKING UP ANY ADDITIONAL MEMORY, JUST TO GET IT WRAPPED UP IN NEW NODE 

It's easier to store data of different sizes in a linked list. An array assumes every element is exactly the same size.
As you mentioned, it's easier for a linked list to grow organically. An array's size needs to be known ahead of time, or re-created when it needs to grow.
Shuffling a linked list is just a matter of changing what points to what. Shuffling an array is more complicated and/or takes more memory.
As long as your iterations all happen in a "foreach" context, you don't lose any performance in iteration.
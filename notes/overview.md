Like arrays, linked lists are a type of data structure used to store sets of similar, related information. Unlike arrays, they do not require a contagious block of memory. This has advantages and disadvantages, which we’ll learn about as we explore how they are build and compare the two.

construct a linked list and compare the runtime of operations to an array to make the optimal choice between them.

The linked list data structure (both singly- and doubly-linked variants), while not used nearly as much as arrays, nonetheless is an important one for students to learn because it provides an alternative way to implement a data structure that students should be intimately familiar with at this point in the curriculum.

Whereas arrays store and index elements contiguously, each element of a linked list is stored in a node. Each node then has a reference (or a ‘pointer’) to the next node in the linked list. In this way, linked lists describe lists of things in a recursive fashion, while arrays describe lists of things in an iterative fashion.

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

class LinkedList: *from this perspective, dont have direct access to any nodes in middle of list (fast access to first & last element)
-2nd element in linkedList no knowledge of prev node that refered to it (can't go back to head) 
-tail not able to refer back to 2nd to last element
self.head = head_node
self.tail= tail_node

-Adding:
H23 > 39 >T5 > N
list.insert(15)

wrap 15 in linked list node T15 > N
in this case is the new tail (possible to be head when inserting)
move 5 (self.next) node pointer to T15
change tail reference to 15 
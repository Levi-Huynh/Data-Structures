A queue is a way of storing information in a manner where position is significant - first in, first out. Stacks are the opposite - first in, last out. We’ll learn how to build both using a linked list.

At the end of this module, you should be able to:
construct a queue and stack and justify the decision to use a linked list instead of an array.

ENGLISH DEF:
Queue= refers to line 
When entry comes into queue, get added to back of line first. Waits in QUEUE until everything is removed first (FIFO)




Class Queue: 
self.size=0 (size counter for convenience)
self.storage= storage_data_structure (actually Data structure to store elements in queue with fifo dynamic)

QUESTIONS:
WHATS THE OPP OF FIFO ORDERING?
WHAT DS EXHIBIT THIS ORDERING?
WHAT DS WOULD YOU USE TO IMPLEMENT A QUEUE
WHEN FIFO USEFUL? WHEN NOT? 
    -May be useful when making reqs to server=> have reqs and responses serialized/ ordered in fifo 



PRO: QUEUES ARE SIMPLE AND INTUITIVE TO USE AND IMPLMENT 
PRO: THEY CAN BE USED TO SERIALIZE DATA COMING IN FROM MULTIPLE SOURCES
CON: ARE NOT GENERAL-PURPOSE AT ALL IN  & OF THEMSELVES 
    -unlinke array/ linked lists not in of it self able to perform other unserialized functions


STACKS:
-ADD PUT ITEM TO TOP, WHEN REMOVE REMOVE FROM TOP (LIFO)
-ADD TO HEAD &  ALSO REMOVES FROM HEAD
-NEVER EVER NEED TO ADD/REMOVE FROM MIDDLE- NO

QUEUE
-WHY DLL HELPFUL? 
    -WHEN ADDING ALWAYS ADDING TO END  (WHY)
    -WHEN REMOVING ALWAYS REMOVING FROM START  (WHY)
    -NEVER EVER NEED TO ADD/REMOVE FROM MIDDLE- NO
This is equivalent to the requirement that once a new element is added, all elements that were added before have to be removed before the new element can be removed.

IF ARR:
    ADDING TO BACK OR FRONT, ADDING IS O(N)

IF LL:
    ADDING TO BACK OR FRONT ADDING IS O(1)

SLL IS GOOD FOR IOT HYPER TIGHT ON MEMORY LIKE IOT DEVICES 

if insert in middle, most likely O(n)
-insert to back normaly O(1)
-first, is the most costly to delete in array-> can't just have empty in the front of arr


DS OPS: 
   rt complex             LL                      ARR

-access    :            O(n)                    O(1)
-insert front           O(1)                    O(n) (if append just add to back, no shifting)
-insert back            O(1)                    O(1)
-remove                 O(1)                    O(n)
-access F orB           O(1)                    

class Node:
    -value
    -next

class LL:
    -head
    -tail
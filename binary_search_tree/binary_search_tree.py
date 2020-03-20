from doubly_linked_list import DoublyLinkedList
from dll_queue import Queue
from dll_stack import Stack
import sys
sys.path.append('./queue_and_stack')
sys.path.append('./doubly_linked_list')


# lru_cache(maxsize=500)
# least recently used (will purge if not lrc)
# wraps another function HOC - behind the scenes
# takes form of key value pairs
# keep track of priority order can use other DS to help with this
# MRU etc many types

# hints: single nodes can still be binary search trees


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):  # add to tail
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):  # remove from tail
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        return self.size


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements? B/c can easily access the MRU if add
        # to start or beginning and pop that off or add on when adding or removing node for FIF
        #

        self.storage = DoublyLinkedList()

    def enqueue(self, value):  # add to Queue FIFO #ADD TO END
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):  # remove from queue FIFO
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        return self.size


class BinarySearchTree:
    def __init__(self, value):
        # self.value is root node! (has left and right) #value is value your comparing with self.node(root)
        self.value = value
        self.left = None
        self.right = None

   # Insert the given value into the tree
    def insert(self, value):
        # check if new value is less than current node #VALUE IS LESS THAN CURRENT NODE (SELF.VALUE)
        if value < self.value:
            # if there is no self.left value:
            if not self.left:
                # set the new left child to be new value
                # creates new intance of BInarySearchTree node with (self.value as root, has self.left & self.right)
                self.left = BinarySearchTree(value)
            else:  # if self.left exists:
                # recurse call insert on the self.left node (which exists) and does comparison steps above to  value / repeats the process above
                self.left.insert(value)
        # NEW VALUE IS GREATER THAN CURRENT NODE (SELF.NODE):
        # go right
        else:
            if not self.right:
                self.right = BinarySearchTree(value)  # (CREATE NEW BST)
            else:
                # RECURSE, THE SELF.RIGHT NODE AND RECURSE THE COMPARISON LOGIC
                self.right.insert(value)

   # Return True if the tree contains the value
   # False if it does not
    def contains(self, target):
        # if the root node, is the target value, we found the value
        if self.value == target:
            return True  # recurse will bring it back up here to return true if self.left.value == target
        # target is smaller, go left
        sub_tree_contains = False
        if target < self.value:
            if not self.left:
                return False
            else:
                # IMPORTANT RETURN can be used here b/c `contains` function ASKING FOR RETURN BOOLEAN (INSTEAD OF ADDING NODE)
                sub_tree_contains = self.left.contains(target)
       # target is greater, go right
        else:
            if not self.right:
                return False
            else:
                sub_tree_contains = self.right.contains(target)
        return sub_tree_contains
   # Return the maximum value found in the tree
# for bst, bottom most r, will always be max , bottom most left would always to be bottom most left
# cspt6

    def get_max(self):  # iterative
        if not self:
            return None
       # recursive solution
       # if we can go right, go right
       # return when we can't go right anymore
       # if not self.right: (NOTHING TO RIGHT, SO NOTHING LARGER THAN ROOT NODE SO MAX IS ROOT NODE )
        #     return self.value
       # return self.right.get_max()
       # iterative solution
        current_tree_root = self  # if temp node, reset to next node to move thru while
        while current_tree_root.right:  # can also be while current_tree_root is not None:
            # REMEMBER LEVI THIS MOVES CURR TO THE RIGHT POSITION AS THE NEW CURR
            # keeps moving r, b/c node thats to the most r should be max
            current_tree_root = current_tree_root.right
            # in sorted bst
        return current_tree_root.value
    # Call the function `cb` on the value of each node #cb= another function
   # You may use a recursive or iterative approach

    def get_max1(self):  # recrusive solution
        if not self:
            return None
        if not self.right:
            return self.value
        max_value = self.right.get_max()
        return max_value

    def for_each(self, cb):  # EX OF DFS, PATH WE CHOOSE WE GO ALL THE WAY AND VISIT (ORDER IS 8, 4, 6)
        # return this first line in recursion of cb for curr.value, activates cb on each value here
        cb(self.value)
# STACK nothing goes until every function on top level is done, then next on the stack is executed
        if self.left:  # if self.left is not null, recurse & implement cb on each self.left value, same for right
            # recurse for_each #waits for this to finish before if self.right called
            # all the children node of 4 if 9 is the root, node must do self.left & s.r first
            self.left.for_each(cb)
            # and finish in the children node finishe self.leftfor each and self.rigth for each, before can finish
            # and bubble back to the parent node before self.right on root node is called
        if self.right:
            self.right.for_each(cb)

  # traversal : goes both L & R

    def in_order_print(self, node):  # low to high value
        # go left if you can
        if node.left:
            self.in_order_print(node.left)
    # print the current node recursivly
        if node.right:
            print(node.value)
            self.in_order_print(node.right)
    # go right if you can
        else:
            print(node.value)


# Print the value of every node, starting with the given node, add children per level with Q
# in an iterative breadth first traversal (BFS) ORDER WE VISIT NODES (finding everyone on a specific horizontal level)

    def bft_print(self, node):  # Doesn't deal with recursive, well,  call QUEUE!

        # create a queue to keep track of nodes
        # place the first node onto queue
         # while queue isnt empty:
        # deque the top node
        # print the node thats dequeued
        # add children to the queue

        queue = Queue()  # queue FIF
        queue.enqueue(node)  # not node.value
        while queue.len() > 0:
            curr = queue.dequeue()  # save to temp var
            print(curr.value)  # prints each time dequeues
            if curr.left:  # if the dequeued node has left
                queue.enqueue(curr.left)
            if curr.right:
                queue.enqueue(curr.right)


# Print the value of every node, starting with the given node,
# in an iterative depth first traversal (DFS) ORDER WE VISIT NODES  (look at node and each child and each their child, go all the way deep to left side, then right side of node in that depth of order)

    def dft_print(self, node):  # FILO queue ()

        # create a stack to keep track of nodes
        # place the first node onto stack
        # while stack isnt empty:
        # pop the top node
        # print the node
        # add children to the stack
        # remember which children to add first,
        # because that changes the output order
        stack = Stack()
        stack.push(node)  # noe not node.value
        while stack.len() > 0:
            curr = stack.pop()  # Pop the top node
            print(curr.value)  # print the popped node
            if curr.right:
                # add curr.left to stack #order doesn't matter here?
                stack.push(curr.right)
            if curr.left:
                stack.push(curr.left)


"""
myvar1 = DoublyLinkedList(21)
myvar = BinarySearchTree(myvar1)
myvar.insert(19)
myvar.insert(15)
myvar.insert(12)
myvar.insert(20)
myvar.insert(7)
myvar.dft_print(21)
"""


# STRETCH Goals -------------------------
# Note: Research may be required


# Print In-order recursive DFT
"""
def pre_order_dft(self, node):
    pass


​
# Print Post-order recursive DFT


def post_order_dft(self, node):
    pass


​
​
# my_bst
​
# my_bst_max_value = my_bst.get_max()
"""

import sys
#sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

#lru_cache(maxsize=500) 
#least recently used (will purge if not lrc)
#wraps another function HOC - behind the scenes
#takes form of key value pairs
#keep track of priority order can use other DS to help with this
#MRU etc many types

#hints: single nodes can still be binary search trees
​
class BinarySearchTree: 
    def __init__(self, value):
        self.value = value #self.value is root node! (has left and right) #value is value your comparing with self.node(root)
        self.left = None
        self.right = None
​
    # Insert the given value into the tree
    def insert(self, value):
        # check if new value is less than current node #VALUE IS LESS THAN CURRENT NODE (SELF.VALUE)
        if value < self.value:
            # if there is no self.left value: 
            if not self.left:
                # set the new left child to be new value
                self.left = BinarySearchTree(value) #creates new intance of BInarySearchTree node with (self.value as root, has self.left & self.right)
            else: #if self.left exists:
                self.left.insert(value) #recurse call insert on the self.left node (which exists) and does comparison steps above to  value / repeats the process above 
        # NEW VALUE IS GREATER THAN CURRENT NODE (SELF.NODE):
        # go right
        else:
            if not self.right:
                self.right = BinarySearchTree(value) #(CREATE NEW BST)
            else: 
                self.right.insert(value) #RECURSE, THE SELF.RIGHT NODE AND RECURSE THE COMPARISON LOGIC
​
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the root node, is the target value, we found the value
        if self.value == target:
            return True    
        # target is smaller, go left
        sub_tree_contains = False
        if target < self.value:
            if not self.left:
                return False
            else:
                sub_tree_contains = self.left.contains(target) #IMPORTANT RETURN can be used here b/c `contains` function ASKING FOR RETURN BOOLEAN (INSTEAD OF ADDING NODE)
​
        # target is greater, go right
        else:
            if not self.right:
                return False
            else:
               sub_tree_contains = self.right.contains(target)
​
        return sub_tree_contains
​
​
    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None
​
        # recursive solution
​
        # if we can go right, go right
        # return when we can't go right anymore
        # if not self.right: (NOTHING TO RIGHT, SO NOTHING LARGER THAN ROOT NODE SO MAX IS ROOT NODE )
        #     return self.value    
        # return self.right.get_max()
        
        # iterative solution
        current_tree_root = self
        while current_tree_root.right: # can also be while current_tree_root is not None: 
            current_tree_root = current_tree_root.right #REMEMBER LEVI THIS MOVES CURR TO THE RIGHT POSITION AS THE NEW CURR 
​
        return current_tree_root.value
​
​
​
    # Call the function `cb` on the value of each node #cb= another function 
    # You may use a recursive or iterative approach
    def for_each(self, cb): #EX OF DFS, PATH WE CHOOSE WE GO ALL THE WAY AND VISIT (ORDER IS 8, 4, 6)
        cb(self.value)    
​   #STACK nothing goes until every function on top level is done, then next on the stack is executed 
        if self.left:
            self.left.for_each(cb) #recurse for_each #waits for this to finish before if self.right called 
        if self.right:
            self.right.for_each(cb)
​
​
    # DAY 2 Project -----------------------
​
#CALL STACK PYTHON KEEPS TRACK OF THIS
"""
-in order print (IOP)
-
"""

#in order: (left, root, right)
# 5, 6, 10, 11, 20, 25 in order

# preorder: Root, left, right 
# pre order: 10, 5, 6, 20, 11, 25

#post order Left, Right, Root 
# post order : 6, 5, 11, 25, 20, 10 (root node last)



    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node): #low to high value 
        # go left if you can
        in_order_print(node.left)
        # print the current node
        print(node.value)
        # go right if you can
        in_order_print(node.right)
        return
​
​"""

print(6) returns
iop(6) (goes to right) (no more to left) so this will pop off
print(5) returns immediately => value added to stack 
iop(5) (goes to left) (nothing else to do, so pops off)
iop(10)
-----call stack

actual values on this stack above:

add right (first in last out)
add root
add left 


 
node 10 (pop node off) ==> print val => add children to stack (node 5, node 20)

----stack

node 25
node 11
------------------> here afer node 20 pops off, children of node 20 will go on before node5 is popped off
node 5
---- stack


print 25
iop(25)
print 11
iop(11)
iop(20)
print 10
iop(10)
------call stack
"""
​
    # Print the value of every node, starting with the given node, add children per level with Q
    # in an iterative breadth first traversal (BFS) ORDER WE VISIT NODES (finding everyone on a specific horizontal level)
    def bft_print(self, node): #Doesn't deal with recursive call QUEUE!
        # create a queue to keep track of nodes
        # place the first node onto queue
​
        # while queue isnt empty:
            # deque the top node
            # print the node
            # add children to the queue
        pass
​
​
​
​   
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal (DFS) ORDER WE VISIT NODES  (look at node and each child and each their child, go all the way deep to left side, then right side of node in that depth of order)
    def dft_print(self, node):
        # create a stack to keep track of nodes
        # place the first node onto stack
​
        # while stack isnt empty:
            # pop the top node
            # print the node
            # add children to the stack
            # remember which children to add first, 
            # because that changes the output order
​
        pass
​
​
​
​
​
​
    # STRETCH Goals -------------------------
    # Note: Research may be required
​
    # Print In-order recursive DFT
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
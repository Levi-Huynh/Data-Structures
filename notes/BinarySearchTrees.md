BST

Binary search trees are great! They require some setup, but then we can search for values with great efficiency. We’ll learn how to set one up, and how to find and manipulate the values inside.

construct a binary search tree class that can perform basic operations with O(log n) runtime..

Binary Search Trees are an extremely efficient data structure when it comes to searching. 
Students will be exposed to some ways in which operations may be improved past linear runtimes.

-Like linked lists, binary search trees (BST) consist entirely of nodes holding values, with each node referencing other nodes. 

-In the case of Trees (T) in general, each node is NOT constrained to just referencing a single (1) other node. 
    -Can thought of as linked lists (LL) BUT (T) node can point to MULTIPLE other nodes in (T)
    -LL can count as a (T) w/ constraint, each node can point to (1) other node


-Binary trees (BT) are tree data structures where each node can reference up to two (2) other nodes, a left node and a right node. 
    -Common (T) classification = (MAX) number of nodes, a single node (SN) can point to
    -BT => (MAX) a (SN) can point to => 2 
    -Ternary (TER) => (MAX) a (SN) =>3
    -4-ary (4RY) =>(MAX) a (SN) => 4


-Binary search trees (BST) are an instance of binary trees (BT).
    -Rule/Invarient: If node has left child node (LCN) it points to: _all_ values of LCN (L subtree) is less than Parent node (PN)
          If node has right child node (RCN) it points to: _all_ values of RCN (R subtree) is greater than Parent node (PN)
          Both sides left and right are BST
          ^^^ EFFICIENT FOR SEARCHING
          ^^^ THIS RULE IS _TRUE_ FOR EVERY (SN) IN TREE   

class BinarySearchTree:
    self.value = value
    self.left = left_subtree ( root of left subtree)
    self.right = right_subtree (root of right subtree)


EX Checking for a Value in BST
bst.contains(10)
1) Compare Value to ROOT of tree 
2) Check if Value is less than, greater than, or equal to ROOT
3) IF Value exists in BST, THEN will exist in L or R subtree based on #2
4) TRAVERSE DOWN THAT SIDE (L or R) OF BST
5) Compare it to next root node in L or R subtree
6) If Value greater than or equal to root node in #5, search for Value in (L or R) subtree of that root node 
7) repeat 6, until ARRIVE AT (LEAF), no more nodes to search 

# PROS & CONS OF BINARY SEARCH TREES
- BST optimized for searches
# PRO: 
    - searchin for element in BST is much more efficient than searching thu arry or LL 
# CON: 
    - As tradeoff, not efficient to insert into a BST (b/c of rule, have to traverse BST to find the right location to insert?)
    - Performace of BST depends a lot on wheter the tree is 'balanced' or not.  Good assumption to make? When is assumption incorrect?  
    #BALANCED: tree is considered balanced because the difference between heights of the left subtree and right subtree is not more than 1. BALANCED T takes less search to look for value, UNBALANCED T requires more values to search thru
    https://www.crondose.com/2016/08/binary-search-trees-balanced/

    
# Terminology:
# ROOT: Topmost node in tree
# CHILD: Node directly connected to another node when moving _away_ from the root node
# PARENT: Node directly connected to another node when moving _towards_ the root node
# SIBLINGS: Nodes that share the same parent are considered siblings
# LEAF: Node that does not have any children of its own.  

## QUESTIONS: 
- How would inserting into a BST work? How would it differ from the contains example we just walked through?
- IN the contains example, out of all the elements in the BST, how many did we actually check?  How does this compare to the number of elemts we would have to check if we were checking for a value in an arr or a linked list?  
- Is inserting into a binary search tree more or less work than inserting into an arry or linked list?  Why?  


# DS OPERATIONS
- Insert
- Find (in)
- Delete
- 

Find 19 in tree
Start at Root
Compare Size
If smaller:
    go left
If greater: 
    go right
repeat 

if left is taken, go left, repeat
if left is taken, go right, repeat
else : create leaf

# BST examples real world:
-heap sort
-if want to find or insert at beginning /end LL or DLL etc may be good
-if just random search, hard to beat BST log n



## Challenge
Draw/model out inserting a new element into a binary search tree.

Draw/model out how to traverse a binary search tree and get to the minimum element in the tree.

Draw/model out how to traverse the tree in order from the smallest element in the tree to the largest element in the tree.          
          
Walk through and draw out an example of how a search is performed on a binary search tree.
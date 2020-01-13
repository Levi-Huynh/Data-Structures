Tree Traversal

A traversal is an operation in which each node of a data structure such as a tree is “visited”. We’ll examine two types of traversals - Depth First Traversal (DFT) and Breadth First Traversal (BFT).

Trees can be thought of as being similar to a few different types of data structures. They’re similar to linked lists, except with multiple next nodes. 

They are also a special type of graph. We’ll learn more about the details of graphs in another lesson, but the great thing is that this means that we can use a number of techniques on both graphs and trees. 

In particular, we can use both a DFT and a BFT to “crawl” over the tree from node to node. This is useful for many tasks - search, printing, callbacks, and a number of other things. 

We’ll use our Binary Search Tree (BST) for this exercise, but these techniques will work on many other types of trees and graphs.

# A search is completed when the target of the search is found. A traversal is completed when every node has been explored.

# DFT (STACK LIFO)
## A Depth First Traversal (DFT) is one that continues traveling forward on each branch until a dead end is reached. The search then retreats to the first unexplored branch and follows the next unexplored path until that one too reaches a dead end. This continues until all nodes have been visited. 

## Think of it like being in a maze and always turning right at each intersection. We can do a DFT recursively or iteratively. The iterative approach makes use of stack.

# BFT (QUE FIFO)
## A Breadth First Traversal (BFT) takes the opposite strategy. We explore layer by layer, slowly moving outward from the starting point.
##  At each node, we add every node we discover to the list of nodes to explore, _then explore them in the order in which we encounter them_. For this, we use a queue. This means we’ll jump around a bit - the next node we visit might not be directly connected to the one we are on.


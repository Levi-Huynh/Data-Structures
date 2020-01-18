import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements? B/c can easily access the MRU if add 
        #to start or beginning and pop that off or add on when adding or removing node for FIF
        #  

        self.storage = dict() # OR ARR 
        self.order = DoublyLinkedList()

    def enqueue(self, key): #add to Queue FIFO

        node = self.storage[key]
        self.order.add_to_tail(key, node)

    def dequeue(self, key): #remove from queue FIFO
        node= self.storage[key]
        if key in self.storage:
            self.order.remove_from_tail(node)

    def len(self): 
        pass

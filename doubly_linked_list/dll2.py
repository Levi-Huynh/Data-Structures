


"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
​
​
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
​
    def __str__(self):
      return str(self.value)
​
​
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
​
    def __len__(self):
        return self.length
​
    def __str__(self):
      if self.head is None and self.tail is None:
        return "empty"
      curr_node = self.head
      output = ''
      output += str(curr_node) + ' <-> '
      while curr_node.next is not None:
        curr_node = curr_node.next
        output += str(curr_node) + ' <-> '
      return output
   
    def add_to_head(self, value):
      new_node = ListNode(value)
      self.length += 1
      if self.head is None and self.tail is None:
        # empty list case
        self.head = new_node 
        self.tail = new_node
      else:
        # save the old head to local var
        old_head = self.head
        # link both nodes together
        new_node.next = old_head
        old_head.prev = new_node
        # assign head to the new node
        self.head = new_node
​
    def remove_from_head(self):
      if self.head is None:
        return
​
      node_to_remove = self.head
      new_head = node_to_remove.next
      # move head pointer to the next value
      self.head = new_head
      # sever the connection to node_to_remove
      node_to_remove.next = None
      self.length -= 1
​
      if self.head is None:
        self.tail = None
      else:
        self.head.prev = None
​
      val = node_to_remove.value
      # del node_to_remove
​
      return val
​
    def add_to_tail(self, value):
      pass
     
    def remove_from_tail(self):
      pass
​
​
dll = DoublyLinkedList()
​
dll.add_to_head(5)
dll.add_to_head(7)
dll.add_to_head(3)
print(dll)
dll.remove_from_head()
print(dll)
dll.remove_from_head()
print(dll)
dll.remove_from_head()
print(dll)
dll.remove_from_head()
print(dll)
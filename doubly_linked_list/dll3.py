class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)

    """
    1) Wrap the given value in a ListNode
    2) and insert it after this node.
    3)Note that this node could already
    have a next node it is point to.
    """


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0  # convenient to have access

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None and self.Tail is None:
            return "empty"
        curr_node = self.head
        output = ""
        output += f'({curr_node.value}) <->'
        return output
 """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    
    def add_to_head(self, value):
        new_node= ListNode(value)
        self.length +=1
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

     """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length +=1
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev= self.tail 
            self.tail.next = new_node 
            self.tail = new_node
             
    
     """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        value = self.head.value
        if self.head is None and self.tail is None:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail =None 
            self.length -=1
            return value
        else:
            new_head = self.head.next
            new_head.prev = None 
            self.head.next = None
            self.head = new_head 
            self.length -=1
            return value 
 """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        if self.tail is None and self.head is None:
            return 
        elif self.tail == self.head:
            self.tail = None 
            self.head = None 
            self.length -=1 
            return value 
        else: 
            new_tail = self.tail.prev #store in local var 
            new_tail.next = None #sever
            self.tail.prev = None  #sever
            self.tail = new_tail 
            self.length -=1 
            return value 
        

    def remove_from_head(self):

    def add_to_tail(self, value):


    """Returns the highest value currently in the list"""
    def get_max(self):
        pass


  """Returns the highest value currently in the list"""

    def get_max(self):
    curr_val = self.head.value 
    max_value = self.head.value 
    
    while curr_val is not None:
        if curr_val > max_value:
            max_value = curr_val
        curr_val = curr_val.next #iterate thru to next value, 
        # notice scope ^ 
    return max_value  

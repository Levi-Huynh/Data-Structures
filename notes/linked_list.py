class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
​
class LinkedList:
    def __init__(self):
        self.head = None
    
    def print(self):
        curr_node = self.head
        print('--HEAD---')
        while curr_node is not None:
            print(curr_node.value)
            curr_node = curr_node.next
        print('-----')
​
    def add_to_front(self, value):
        old_head = self.head
        new_head = Node(value)
        new_head.next = old_head
        self.head = new_head
​
​
def get_middle(linked_list):
    # return us the middle value
    slow_pointer = linked_list.head #both point/starts at same head point
    fast_pointer = linked_list.head
​
    while fast_pointer is not None: #more pointers to go  #FIRST 1 MOVE OF FASTPOINTER IN WHILE (WHILE STOPS WHEN FAST_POINTER =NONE)
        fast_pointer = fast_pointer.next #moves it 1 over  
        if fast_pointer is not None:
            fast_pointer = fast_pointer.next #moves it 1 over #2ND 1 MOVE OF FASTPOINTER IN WHILE 
            slow_pointer = slow_pointer.next #FIRST & ONLY 1 MOVE OF SLOW POINTER IN WHILE LOOP
​
    return slow_pointer.value
​
"""
Goal: return list thats completely reversed
when printed should be reversed
is LL
no extra data 
excercise of flipping pointers around
curr=>0
new => curr.next
new.next=curr
new.next = curr #loop
curr.next = None 
"""​
​def reverse_list(linked_list): #rt O(1)
    curr = linked_list.head
    new = curr.next
    # this is new tail
    curr.next = None
    prev = None
​
    while new is not None:
        prev = curr #moves 1
        curr = new #moves 1
        new = curr.next #moves 1
        curr.next = prev
        linked_list.head = curr
​
​
​
ll = LinkedList()
ll.add_to_front(1)
ll.add_to_front(2)
ll.add_to_front(3)
ll.add_to_front(4)
ll.print()
reverse_list(ll)
ll.print()

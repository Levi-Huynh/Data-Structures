import sys
import unittest
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

#cache looks up results so dont have to redo operations
#look up is normally O(n)
#look up for O(1) is dict

#add lru to front , mru to back 

#dict to help keep key value pair, another DS to keep priority order

#
class LRUCache:
    """
    -Our LRUCache class keeps track of the *max number of nodes it
    can hold*,
    
    -the current number of nodes it is holding, 
    
    -a doubly- linked list (DLL) that holds the key-value entries in the correct
    order
    
    -as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10): #SET LIMIT HERE IN INIT 
        self.storage = dict()
        self.limit = limit #purge from storage
        self.size = 0
        self.order = DoublyLinkedList() #Not passing anything here yet
    """
    -Retrieves the value associated with the given key. 
    
    -needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used (MRU)
    
    -Returns the value associated with the key or None if the
        key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if no key in storage, return None
        if key not in self.storage:
            return None
        # read from storage
        node = self.storage[key] 

        # move key to tail
        self.order.move_to_end(node) 
        
        return node.value[1] #??? self.storage[key].value[1] why 1? 

    """
    Adds the given key-value pair to the cache. 
    
    -The *NEWLY ADDED PAIR* should be considered the most-recently used (MRU)
    entry in the cache. 
    
    -CONDITIONAL If the cache is already at *max capacity*
    BEFORE this entry is ADDED, then the OLDEST ENTRY in the
    CACHE needs to be REMOVED to make room.
    
    -Additionally, CONDITIONALLY : 
    IF the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # the key does exist #essentially though don't want 2 of same keys
        if key in self.storage:
            node = self.storage[key]
            # update the value in storage
            node.value = (key, value)
            # move the existing node to the tail
            self.order.move_to_end(node) # self.order = DoublyLinkedList()
            return #what does that actually RETURN? 

        # the key does not exist
        # create a node with the key
        # add node to tail of order DLL
        self.order.add_to_tail((key, value))
        # store key and value in storage 
        self.storage[key] = self.order.tail
        self.size += 1
        # check if limit exceeded 
        if self.size > self.limit:
            # remove the least recently used key: value pair
            del self.storage[self.order.head.value[0]] #why value here is [0]??
            # remove current head from order
            self.order.remove_from_head()
            self.size -= 1


class CacheTests(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(3)

    def test_cache_overwrite_appropriately(self):
        self.cache.set('item1', 'a')
        self.cache.set('item2', 'b')
        self.cache.set('item3', 'c')

        self.cache.set('item2', 'z')

        self.assertEqual(self.cache.get('item1'), 'a')
        self.assertEqual(self.cache.get('item2'), 'z')

    def test_cache_insertion_and_retrieval(self):
        self.cache.set('item1', 'a')
        self.cache.set('item2', 'b')
        self.cache.set('item3', 'c')
        print(self.cache.storage)
        self.assertEqual(self.cache.get('item1'), 'a')
        self.cache.set('item4', 'd')

        self.assertEqual(self.cache.get('item1'), 'a')
        self.assertEqual(self.cache.get('item3'), 'c')
        self.assertEqual(self.cache.get('item4'), 'd')
        self.assertIsNone(self.cache.get('item2'))

    def test_cache_nonexistent_retrieval(self):
        self.assertIsNone(self.cache.get('nonexistent'))


if __name__ == '__main__':
    unittest.main()
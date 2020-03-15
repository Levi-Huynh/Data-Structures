-Bits of storage thats fast to access, (Cache), versus slow access such as primary storage like a HDD.  
    -small amount of memory, that can seepd up access to freq used info 
-Freq used data shows the greatest speedup 

-diff caches -> cache can't be big as HDD

-Cache hit: when data you want is in the cache 
-Cache Miss: when you have to go to primary storage to get the data 

LRU (least recenlty used)
-limited size, compared to primary storage
- strategy use to remove items from cache (items we dont need to use as often in future), so cache doesnt become full 
- similar to hash table, look up keys to find values 
-need a hash table to quickly look up cache entries by key (points to all element in DLL, order 1 look up entries by key)
-need the cache entries in doubly-linked list (order 1 ops, moving items around)

LRU Cache Overview

HashTable has 
A  B C D (nodes, listed as keys)
Look up keys, giving access to entries 

DLL is ordered from Most recently used(Most recenlty _added_ or used ) to Least recently used (Least recently used)

# Putting entries in cache
-move to head of list
-add hash table entry 
-add as Head to LL (which shows its MRU)
- add next and prev pointers to head 

# Getting Entries from the Cache
-look up key for item in hash table (will count as _using_ entry)
-Accessing (will count as _using_ entry), SO move the accessed element to the head of the list (MRU)
-return pointer(s) to that entry

# Delete entries from the Cache 
-If cache is overfull, simply delete the tail entry
-Delete the DLL pointers and hash table entry 
-This discards the Least-recently used entry 

# challenge
-what are some applications of LRU caches  
    -pre loaded info on web site searches, preferences, certain sites in general saved so not newly loaded
-How to add functionality to the cache(in pseduo) to remove entries that are older than a cutoff age from the cache? O(n)


-How to remove entries as above in O(1) time 


## Reasoning Behind Decisions:
I choose an ordered dictionary to store the data of the cache, because one of the requirements was that the get and set operations should run under O(1) time complexity.  

With the get operation, the hash of the key returns an index in O(1) time complexity, and if the item is present in the dictionary, the item would be first deleted and then inserted back into it, so that that it becomes the latest item.  

In the set operation, if the item is present in the dictionary, it will be first deleted and then inserted back into it, so that it becomes the latest item.  If the item was not present in the dictionary it will be inserted, but it the dictionary is already full, the last item should be first removed and then this new item inserted afterwards.

## Time Efficiency:
Both set() and get() operations run in O(1)

## Space Efficiency:
The space eficiency of the set() operation is O(n), dependent on the 
number of items that are added to the cache.
from doubly_linked_list import DoublyLinkedList
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.dictionary = {}
        self.dll = DoublyLinkedList()
        self.node_list = []

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if not key in self.dictionary.keys():
            return None
        else:
            value = self.dictionary[key].value
            node = self.dictionary[key]
            if node in self.node_list:
                self.dll.move_to_front(node)
                return value
            else:
                return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        dll_len = self.dll.length
        # if this is a new entry in the dictionary 
        if key not in self.dictionary.keys():
            if dll_len < self.limit:
                # if there are less than 10 things in cache just add to dict and dll
                self.dll.add_to_head(value)
                node = self.dll.head
                self.node_list.append(node)
                self.dictionary.update({key:node})

                # If limit is met remove the tail from the dll add the new value as head
            elif dll_len >= self.limit:
                self.dll.add_to_head(value)
                tail = self.dll.tail
                self.dll.remove_from_tail()

                self.node_list.remove(tail)
                node = self.dll.head
                self.node_list.append(node)

                self.dictionary.update({key:node})
        # if this is not a new entry in the dictionary 
        else:
            node = self.dictionary[key]
            # If an existing node in cache is being set again delete that node and create a new head node 
            # with that new value but don't remove it from the node_list
            if node in self.node_list:
                node.delete()
                self.node_list.remove(node)
                self.dll.add_to_head(value)
                new_node = self.dll.head
                self.node_list.append(new_node)
                self.dictionary.update({key:new_node})
                
            else:
                self.dll.add_to_head(value)
                tail = self.dll.tail
                self.dll.remove_from_tail()

                self.node_list.remove(tail)
                node = self.dll.head
                self.node_list.append(node)

                self.dictionary.update({key:node})


cache = LRUCache(3)

cache.set('item1', 'a')
cache.set('item2', 'b')
cache.set('item3', 'c')
cache.set('item2', 'z')
print(cache.get('item1'))
print(cache.get('item2'))
print(len(cache.node_list))
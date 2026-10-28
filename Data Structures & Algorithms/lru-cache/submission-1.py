class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # key : node
        # node -> (key, value)
        # head = LRU --- tail = MRU
        # (K,V) <-> (K,V) <-> (K,V)

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        # (0,0) <-> (0,0)
        # L.(LRU)   R.(MRU)
    def remove(self, node):
            prv, nxt = node.prev, node.next
            prv.next = nxt
            nxt.prev = prv
    
    def insert(self, node): #at MRU
        prv, nxt = self.right.prev, self.right
        prv.next = node
        nxt.prev = node
        node.next = self.right
        node.prev = prv

    def get(self, key: int) -> int:
        """ get key and ensure it is MRU """
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        """ update value of key and ensure it is MRU """
        if key in self.cache:
            # update key's value
            self.remove(self.cache[key])
        new = Node(key, value)
        self.cache[key] = new
        self.insert(new)
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key)


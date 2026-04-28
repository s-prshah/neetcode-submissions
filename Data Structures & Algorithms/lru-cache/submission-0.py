class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0
        
    def evict(self, node):
        nextNode = node.next
        prev = node.prev
        prev.next = nextNode
        nextNode.prev = prev
        self.size -= 1

    def insert(self, node):
        prev = self.right.prev
        self.right.prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.size += 1

    def get(self, key: int) -> int:
        if key in self.cache:
            self.evict(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            to_insert = Node(key, value)
            self.insert(to_insert)
            self.cache[key] = to_insert
            if self.size > self.capacity:
                del self.cache[self.left.next.key]
                self.evict(self.left.next)
        else:
            self.cache[key].val = value
            self.evict(self.cache[key])
            self.insert(self.cache[key])

    
    
        

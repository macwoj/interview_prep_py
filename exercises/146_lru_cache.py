
class Node:
    def __init__(self,key,value):
        self.key,self.val = key,value
        self.next,self.prev = None,None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head,self.tail = Node(None,None),Node(None,None)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        
    def insert(self,node):
        self.tail.prev.next = node
        node.prev=self.tail.prev
        self.tail.prev = node
        node.next=self.tail
    
    def remove(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key,value)
            self.cache[key] = node
            self.insert(node)
            if len(self.cache) > self.capacity:
                del self.cache[self.head.next.key]
                self.remove(self.head.next)
        else:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)

#variant: add del(key) if key exists return true, last()
class LRUCache2:
    def __init__(self):
        self.cache = {}
        self.head,self.tail = Node(None,None),Node(None,None)
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        
    def insert(self,node):
        self.tail.prev.next = node
        node.prev=self.tail.prev
        self.tail.prev = node
        node.next=self.tail
    
    def remove(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key,value)
            self.cache[key] = node
            self.insert(node)
        else:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
    
    def delete(self,key):
        if key not in self.cache:
            return False
        node = self.cache[key]
        self.remove(node)
        del self.cache[key]
        return True
    
    def last(self):
        if self.tail.prev == self.head:
            return -1
        return self.tail.prev.val
class Node:

    def __init__(self, key, val):
        self.key , self.val = key, val
        self.prev = self.next = None
    

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}

        #our list will have end nodes, left and right
        #but this won't be part of cache, just useful for 
        #insertion and removing
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    

    def remove(self, node):
        #this removes the node in middle
        #that's why we take nodes prev , next and point to exach other
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        #we insert always between these two node, 
        #more precisely just before the righmost node

        #first we take the previous of rightmost as, 
        #this is where latest access will be placed
        prev, nxt = self.right.prev, self.right

        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self,key):
        if key in self.cache:
            #we remove the node
            self.remove(self.cache[key])
            #the node is placed just before rightmost if not already
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1
    
    def put(self, key, value):
        
        # if already exists then, we remove it and re insert at before righmost
        if key in self.cache:
            self.remove(self.cache[key])

        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # if cache has more nodes then capacity 
        # we remove node beside the leftmost
        if len(self.cache)>self.cap:
            
            lru = self.left.next
            self.remove(lru)
            print(lru in self.cache)
            del self.cache[lru.key]

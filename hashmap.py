class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class HashMap:
    def __init__(self,size):
        self.hashmap = [None]*size
        self.size = size
        self.data_count = 0
        self.max_loadfactor = 0.75

    def computeHash(self,key):
        key = str(key)
        if not key.isalnum():
            return False
        constant = 5
        hashval = 0
        for i in range(len(key)):
            hashval = hashval + ord(key[i]) * (constant ** i)
        hashval = hashval & 0x7fffffff
        return hashval

    def loadFactor(self):
        load_factor = self.data_count / self.size
        return load_factor

    def add(self,key,val):
        if self.loadFactor() > self.max_loadfactor:
            self.resize(self.size * 2)
        index = self.computeHash(key) % self.size
        head = self.hashmap[index]
        if head == None:
            new_node = Node(key,val)
            self.hashmap[index] = new_node
            self.data_count += 1
            return
        new_node = Node(key,val)
        new_node.next = head
        head.prev = new_node
        self.hashmap[index] = new_node
        self.data_count += 1

    def getValue(self,key):
        index = self.computeHash(key) % self.size
        head = self.hashmap[index]
        if head == None:
            return None
        curr = head
        while curr != None:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None

    def remove(self,key):
        index = self.computeHash(key) % self.size
        head = self.hashmap[index]
        if head == None:
            return
        elif head.key == key:
            self.hashmap[index] = head.next
            self.data_count -= 1
            return
        curr = head
        while curr.next != None and curr.key != key:
            curr = curr.next
        if curr.next != None and curr.key == key:
            prev = curr.prev
            next_node = curr.next
            prev.next =  next_node
            next_node.prev = prev
            self.data_count -= 1
        elif curr.next == None and curr.key == key:
            prev = curr.prev
            prev.next = None
            self.data_count -= 1

    def resize(self,new_size):
        new_hashmap = [None] * new_size
        pairs = self.getItems()
        self.hashmap = new_hashmap
        self.data_count = 0
        self.size = new_size
        for key,val in pairs:
            self.add(key,val)

    def getKeys(self):
        keys = []
        for i in range(len(self.hashmap)):
            if self.hashmap[i] != None:
                curr = self.hashmap[i]
                while curr != None:
                    keys.append(curr.key)
                    curr = curr.next
        return iter(keys)
    
    def getItems(self):
        items = []
        for i in range(len(self.hashmap)):
            if self.hashmap[i] != None:
                curr = self.hashmap[i]
                while curr != None:
                    items.append((curr.key,curr.value))
                    curr = curr.next
        return iter(items)

    def dataCount(self):
        return self.data_count

    def length(self):
        return self.size

hm = HashMap(16)
for i in range(13):
    hm.add(i*5,8*i)
print(hm.size)
print(hm.dataCount())
hm.remove(5)
print(hm.dataCount())
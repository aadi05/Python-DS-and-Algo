class Node:
    def __init__(self,val):
        self.data = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def length(self):
        return self.size
    
    def addFirst(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1
    
    def addLast(self,data):
        if self.head == None:
            return self.addFirst(data)
        new_node = Node(data)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1
    
    def add(self,key,data):
        if self.head == None:
            return self.addFirst(data)
        if self.tail.data == key:
            return self.addLast(data)
        new_node = Node(data)
        curr = self.head
        while curr != None:
            if curr.data == key:
                temp = curr.next
                curr.next = new_node
                new_node.prev = curr
                new_node.next = temp
                temp.prev = new_node
                self.size += 1
                break
            curr = curr.next
    
    def removeFirst(self):
        if self.head == None:
            return None
        elif self.head == self.tail:
            temp = self.head.data
            self.head = None
            self.tail = None
            self.size -= 1
            return temp
        temp = self.head.data
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        return temp

    def removeLast(self):
        if self.head == None or self.head == self.tail:
            return self.removeFirst()
        temp = self.tail.data
        prev_node = self.tail.prev
        prev_node.next = None
        self.tail = prev_node
        self.size -= 1
        return temp

    def remove(self,key):
        if self.head == None or self.head == self.tail:
            return self.removeFirst()
        if self.tail.data == key:
            return self.removeLast()
        temp = None
        curr = self.head
        while curr != None:
            if curr.data == key:
                temp = curr.data
                prev_node = curr.prev
                next_node = curr.next
                prev_node.next = next_node
                next_node.prev = prev_node
                self.size -= 1
                return temp
            curr = curr.next
        
    def display(self):
        if self.head == None:
            return None
        curr = self.head
        while curr != None:
            print(str(curr.data)+"-->",end = "")
            curr = curr.next

dll = DoublyLinkedList()
for i in range(4,40,4):
    dll.addLast(i)
dll.display()
print()
print("\n"+str(dll.remove(36))+"\n")
dll.display()
        

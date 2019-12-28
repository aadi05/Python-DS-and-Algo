class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class LinkedList:
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
        self.head = new_node
        self.size += 1
    
    def addLast(self,data):
        if self.head == None:
            self.addFirst(data)
            return
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def add(self,data,key):
        if self.head == None:
            self.addFirst(data)
            return
        curr = self.head
        while curr != None:
            if curr.data == key:
                new_node = Node(data)
                new_node.next = curr.next
                curr.next = new_node
                self.size += 1
            curr = curr.next

    def removeFirst(self):
        if self.head == None:
            return None
        if self.head == self.tail:
            temp = self.head.data
            self.head = None
            self.tail = None
            self.size -= 1
            return temp
        temp = self.head.data
        self.head = self.head.next
        self.size -= 1
        return temp

    def removeLast(self):
        if self.tail == None or self.head == self.tail:
            return self.removeFirst()
        temp = self.tail.data
        curr = self.head
        prev = None
        while curr.next != None:
            prev = curr
            curr = curr.next
        prev.next = None
        self.tail = prev
        self.size -= 1
        return temp

    def remove(self,key):
        if self.head == None or self.head.data == key:
            return self.removeFirst()
        if self.tail.data == key:
            return self.removeLast()
        curr = self.head
        prev = None
        while curr.next != None:
            if curr.data == key:
                prev.next = curr.next
                self.size -= 1
            prev = curr
            curr = curr.next

    def display(self):
        if self.head == None:
            print(None)
        else:
            curr = self.head
            while curr != None:
                print(str(curr.data) + "->",end = "")
                curr = curr.next
ll = LinkedList()
for i in range(5,26,5):
    ll.addLast(i)
print()
ll.display()
print(ll.length())
print()
ll.remove(20)
print(ll.length())
ll.display()





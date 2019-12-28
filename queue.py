class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1

    def is_empty(self):
        if self.front == -1 and self.rear == -1:
            return True
        else:
            return False

    def enqueue(self, item):
        if self.is_empty():
            self.front += 1
            self.rear += 1
            self.queue.append(item)
        else:
            self.rear += 1
            self.queue.append(item)
        
    
    def dequeue(self):
        popped = self.queue[self.front]
        self.front += 1
        return popped

    def peek(self):
        return self.queue[self.front]

    def display(self):
        for i in range(self.front, self.rear+1):
            print(str(self.queue[i])+"-->", end='')

        print()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.display()
print(q.dequeue())
q.display()

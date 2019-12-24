class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "no items"

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def display(self):
        return self.items
    

# s = Stack()
# s.push(10)
# s.push('aditya')
# s.push(21)
# s.push(11)
# s.push(27)
# print(s.display())
# s.pop()
# s.pop()
# print(s.display())
# print(s.is_empty())
# print(s.peek())



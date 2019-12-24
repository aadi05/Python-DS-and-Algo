from stack import Stack

def enqueue(item):
    s1.push(item)


def dequeue():
    if s2.is_empty():
        while not s1.is_empty():
            elem = s1.pop()
            s2.push(elem)
        return s2.pop()
    else:
        return s2.pop()


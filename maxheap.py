import math
import random
class Heap:
    def __init__(self,inp_array = []):
        self.heap = []
        self.heapify(inp_array)
        self.last_position = -1

    def heapify(self,inp_array):
        if inp_array == []:
            return
        for item in inp_array:
            self.push(item)

    def push(self,item):
        self.heap.append(item)
        self.last_position += 1
        self.trickle_up(self.last_position)

    def trickle_up(self,position):
        if position == 0:
            return
        parent = int(math.floor((position-1)/2))
        if self.heap[position] > self.heap[parent]:
            self.swap(parent,position)
            self.trickle_up(parent)
        return
    
    def pop(self):
        if self.last_position == -1:
            return None
        if self.last_position == 0:
            temp = self.heap[0]
            self.last_position -= 1
            return temp
        temp = self.heap[0]
        self.swap(0,self.last_position)
        self.last_position -= 1
        self.trickle_down(0)
        return temp

    def trickle_down(self,parent):
        left = 2*parent+1
        right = 2*parent+2
        if left == self.last_position and self.heap[left] > self.heap[parent]:
            self.swap(parent,left)
            return
        if right == self.last_position and self.heap[right] > self.heap[left] and self.heap[right] > self.heap[parent]:
            self.swap(parent,right)
            return
        if left > self.last_position or right > self.last_position:
            return
        if self.heap[left] > self.heap[right] and self.heap[left] > self.heap[parent]:
            self.swap(parent,left)
            self.trickle_down(left)
        elif self.heap[right] > self.heap[parent]:
            self.swap(parent,right)
            self.trickle_down(right)


    def swap(self,index1,index2):
        self.heap[index1],self.heap[index2] = self.heap[index2],self.heap[index1]

h = Heap()
arr = [random.randint(2,50) for _ in range(15)]
for item in arr:
    h.push(item)
print(h.heap)
while h.last_position != -1:
    print(h.pop())
print(h.heap)

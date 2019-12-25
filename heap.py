import math
import random
import pdb

class Heap:
    def __init__(self,inp_array=[]):
        self.heap = []
        self.last_position = -1
        self.heapify(inp_array)
        self.size = len(self.heap)
        
    def heapify(self,inp_array):
        if inp_array == []:
            return
        for item in inp_array:
            self.push(item)

    def push(self,item):
        self.heap.append(item)
        self.last_position += 1
        self.trickle_up(self.last_position)

    def pop(self):
        if self.last_position == -1:
            return None
        if self.last_position == 0:
            temp = self.heap[0]
            self.last_position -= 1
            return temp
        temp = self.heap[0]
        self.heap[0],self.heap[self.last_position] = self.heap[self.last_position],self.heap[0]
        self.last_position -= 1
        self.trickle_down(0)
        return temp

    def trickle_up(self,position):
        if position == 0:
            return
        parent = int(math.floor((position-1)/2))
        if self.heap[parent] > self.heap[position]:
            self.heap[position],self.heap[parent] = self.heap[parent],self.heap[position]
            self.trickle_up(parent)
            return
        else:
            return

    def trickle_down(self,parent):
        left = 2*parent+1
        right = 2*parent+2
        if left == self.last_position and self.heap[left] < self.heap[parent]:
            self.heap[parent],self.heap[left] = self.heap[left],self.heap[parent]
            return
        if right == self.last_position and self.heap[right] < self.heap[parent] and self.heap[right] < self.heap[left]:
            self.heap[parent],self.heap[right] = self.heap[right],self.heap[parent]
            return
        if left > self.last_position or right > self.last_position:
            return
        if self.heap[left] < self.heap[right] and self.heap[left] < self.heap[parent]:
            self.heap[parent],self.heap[left] = self.heap[left],self.heap[parent]
            self.trickle_down(left)
        elif self.heap[right] < self.heap[parent]:
            self.heap[parent],self.heap[right] = self.heap[right],self.heap[parent]
            self.trickle_down(right)

    def heap_sort(self):
        temp = self.heap
        sorted_arr = []
        for item in self.heap:
            sorted_arr.append(self.pop())
        self.heap = temp
        return sorted_arr
    
    def debugger(self):
        pdb.set_trace()

h = Heap()
h.pop()
arr = [random.randint(2,200) for _ in range(100)]
arr = [5,6,8,2,4,5,12,43,14,7,78,34,12,89]
for item in arr:
    h.push(item)
print(h.heap)
print(h.heap_sort())
#h.debugger()
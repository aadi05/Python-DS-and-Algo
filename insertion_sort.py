#Time complexity
#Worst case: O(n^2)
#Average case: O(n^2)
#Best case: O(n), when input list is already sorted
#Its a stable in-place sorting algorithm that can be used in databases to sort few elements in the already sorted list.

def insertion_sort(inp_array):
    for i in range(1,len(inp_array)):
        current_idx = i
        for j in range(i-1,-1,-1):
            if inp_array[current_idx] < inp_array[j]:
                inp_array[current_idx],inp_array[j] = inp_array[j],inp_array[current_idx]
                current_idx = j
            else:
                break

arr = [7,2,5,8,12,6,7,9,1,22,18]
insertion_sort(arr)
print(arr)

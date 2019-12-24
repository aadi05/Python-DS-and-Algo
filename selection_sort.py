def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]

arr = [4,7,9,1,2,78,34,1,12,75,48,5,1,11,22]
selection_sort(arr)
print(arr)

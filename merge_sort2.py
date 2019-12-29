import random

def merge(low,mid,high):
    i = low
    j = mid+1
    temp_pos = low
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp[temp_pos] = arr[i]
            i += 1
            temp_pos += 1
        else:
            temp[temp_pos] = arr[j]
            j += 1
            temp_pos += 1
    while i <= mid:
        temp[temp_pos] = arr[i]
        i += 1
        temp_pos += 1
    while j <= high:
        temp[temp_pos] = arr[j]
        j += 1
        temp_pos += 1
    for k in range(low,high+1):
        arr[k] = temp[k]

def merge_sort(low,high):
    if low == high:
        return
    mid = (low+high) // 2
    merge_sort(low,mid)
    merge_sort(mid+1,high)

    merge(low,mid,high)


arr = [random.randint(2,10000) for _ in range(2,10000)]
temp = [None]*len(arr)

merge_sort(0,len(arr)-1)
print(arr)

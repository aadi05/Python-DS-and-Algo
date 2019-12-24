def merge(left, right):
    merged_arr = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
    merged_arr += left[i:]
    merged_arr += right[j:]
    
    return merged_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)


arr = [2,4,7,9,1,2,78,34,1,12,75,48,5,1,11,22]
print(merge_sort(arr))

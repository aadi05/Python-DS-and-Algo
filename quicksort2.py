def quick_sort(arr,start,end):
    if start >= end:
        return
    pivot = arr[end]
    partition_index = start
    for i in range(start,end):
        if arr[i] <= pivot:
            arr[i],arr[partition_index] = arr[partition_index],arr[i]
            partition_index += 1
    arr[partition_index],arr[end] = arr[end],arr[partition_index]

    quick_sort(arr,start,partition_index-1)
    quick_sort(arr,partition_index+1,end)

arr = [5,4,7,2,1,8,12,15,9,6,4,2,16,10]
quick_sort(arr,0,len(arr)-1)
print(arr)
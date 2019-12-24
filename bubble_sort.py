def sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr

print(sort([5,7,2,4,6,8,9,1,2,4,45,34]))

'''def bubble_sort(arr):
    for i in range(len(arr)-1):
        flag = 0
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                flag = 1
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if flag == 0:
            break


arr = [4,7,9,1,2,78,34,1,12,75,48,5,1,11,22]
bubble_sort(arr)
print(arr)'''
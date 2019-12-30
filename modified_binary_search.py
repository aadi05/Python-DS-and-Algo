#Time complexity of search: O(logn)
def first_occurence(arr,element):
    low = 0
    high = len(arr)-1
    result = None
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == element:
            result = mid
            high = mid - 1 #set this line as low = mid + 1 to find last occurence of element.
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return result

arr = [2,4,6,6,6,8,9,13,13,18,21,25,27]
index = first_occurence(arr,13)
if index:
    print(f"First occurence of element at index {index}")
else:
    print("Element not found")
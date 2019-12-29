#Time complexity of search : O(logn)
def binary_search(arr, item):
    lower = 0
    upper = len(arr)-1
    while lower <= upper:
        mid = (lower+upper)//2
        if arr[mid] == item:
            return mid
        else:
            if arr[mid] > item:
                upper = mid - 1
            else:
                lower = mid + 1
    return None

found_index = binary_search([4,5,7,8,12,34,56,78,89], 12)
if found_index:
    print(f"Found at index {found_index}")
else:
    print("Not found")
found_at = 0

def binary_search(arr, item):
    lower = 0
    upper = len(arr)-1
    
    while lower <= upper:
        mid = (lower+upper)//2

        if arr[mid] == item:
            global found_at
            found_at = mid
            return True
        else:
            if arr[mid] > item:
                upper = mid - 1
            else:
                lower = mid + 1

    return False


if binary_search([4,5,7,8,12,34,56,78,89], 12):
    print(f"Found at index {found_at}")
else:
    print("Not found")
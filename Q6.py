def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def sequential_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return "Not Found!"

def binary_search_iterative(arr, key):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < key:
            low = mid + 1

        elif arr[mid] > key:
            high = mid - 1

        else:
            return mid
    return "Not Found!"

def binary_search_recursive(arr, key, low, high):
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == key:
            return mid

        elif arr[mid] > key:
            return binary_search_recursive(arr, key, low, mid - 1)

        else:
            return binary_search_recursive(arr, key, mid + 1, high)

    else:
        return "Not Found!"

n = int(input("Enter the number of elements in the list (1 to 100): "))

if 1 <= n <= 100:
    arr = list(map(int, input("Enter the elements of the list separated by space: ").split()))

    if len(arr) == n:
        arr = selection_sort(arr)
        key = int(input("Enter the key to search: "))

        index = sequential_search(arr, key)
        print("Sequential Search Result: ", index)

        index = binary_search_iterative(arr, key)
        print("Iterative Binary Search Result: ", index)

        index = binary_search_recursive(arr, key, 0, len(arr)-1)
        print("Recursive Binary Search Result: ", index)

    else:
        print("The number of elements entered is not equal to the given range.")

else:
    print("The number entered is not within the given range.")
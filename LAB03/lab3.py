def factorial(number):
    # base case
    if number == 0:
        return 1
    # recursive case
    return number * factorial(number - 1)


def linear_search(lst, key):
    return linear_search_helper(lst, key, 0)

def linear_search_helper(lst, key, index):
    if index == len(lst):
        return -1
    
    if lst[index] == key:
        return index
    
    return linear_search_helper(lst, key, index + 1)


def binary_search(lst, key):
    return binary_search_helper(lst, key, 0, len(lst) - 1)

def binary_search_helper(lst, key, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if lst[mid] == key:
        return mid
    elif key < lst[mid]:
        return binary_search_helper(lst, key, low, mid - 1)
    else:
        return binary_search_helper(lst, key, mid + 1, high)


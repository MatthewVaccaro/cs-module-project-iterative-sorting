def linear_search(arr, target):

    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    start = 0
    end = len(arr)
    incrementor = 0

    while incrementor <= len(arr):

        middle = (start + end) // 2
        if arr[middle] == target:
            return middle

        elif arr[middle] > target:
            end = middle
            middle = (end + start) // 2
            incrementor += 1
        else:
            start = middle
            middle = (end + start) // 2
            incrementor += 1

    return -1

# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # If None
    if len(arr) == 0:
        return arr
    # Create a loop to hold one index and rotate
    for i in range(len(arr)):
        # use a boundary so the same index isn't checked everytime
        boundary = i
        # Hold values
        smallestValue = arr[boundary]
        smallestIndex = boundary
        # Compare current index from the loop above to all the other elements
        for unsortedIndex in range(boundary, len(arr)):
            # comparing the current smallest to the value being passed in using indexing
            if arr[unsortedIndex] < smallestValue:
                smallestValue = arr[unsortedIndex]
                smallestIndex = unsortedIndex
        # Swap those values in the array
        arr[boundary], arr[smallestIndex] = arr[smallestIndex], arr[boundary]

    return arr


def bubble_sort(arr):
    # Steps
    # None
    if len(arr) == 0:
        return arr
    # Create a checker if there was a swap to continue swapping
    didSwitch = True
    # While loop checks the checker (lol)
    while didSwitch == True:
        # On each round it changes it to false
        didSwitch = False
        for i in range(len(arr)-1):
            # if a number is found to be greater it is flipped and the checker is switched
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                didSwitch = True

    return arr

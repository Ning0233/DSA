def valid_mtn_arr(arr):
    # A mountain array must have at least 3 elements
    if len(arr) < 3:
        return False

    # Find the peak of the mountain
    i = 0
    while i + 1 < len(arr) and arr[i] < arr[i + 1]:
        i += 1

    # The peak cannot be the first or last element
    if i == 0 or i == len(arr) - 1:
        return False

    # Check the descending part of the mountain
    while i + 1 < len(arr) and arr[i] > arr[i + 1]:
        i += 1

    # If we reach the end of the array, it's a valid mountain array
    return i == len(arr) - 1
 
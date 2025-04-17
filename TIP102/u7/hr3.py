def binary_search_range(numbers, value, low, high):
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] > value:
            high = mid - 1
        elif numbers[mid] < value:
            low = mid + 1
        else:
            return mid
    return -1

def find_peak(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

def search(nums, target):
    # Find the peak index
    peak = find_peak(nums)

    # Perform binary search on both sides of the peak
    left_result = binary_search_range(nums, target, 0, peak)
    if left_result != -1:
        return left_result

    right_result = binary_search_range(nums, target, peak + 1, len(nums) - 1)
    return right_result
nums = [1, 3, 5, 7, 6, 4, 2]
target = 6
print(search(nums, target))  # Output: 4 (index of target 6)

target = 8
print(search(nums, target))  # Output: -1 (target not found)
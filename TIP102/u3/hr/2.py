    
def find_kth_largest(nums, k):
    n_max = None
    while k >= 1:
        n_max = max(nums)
        nums.remove(n_max)
        k -= 1
    return n_max
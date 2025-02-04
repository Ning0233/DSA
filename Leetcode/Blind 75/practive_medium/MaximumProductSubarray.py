class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        current_max = current_min = 1

        for n in nums:
            temp = current_max * n
            current_max = max(temp, current_min, n)
            current_min = min(temp, current_min, n)

            result = max(result, current_max)
        
        return result

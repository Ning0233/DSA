# solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        
        return res
    
# one-line solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) + (sum([_ for _ in range(len(nums))]) - sum(nums))
        
        
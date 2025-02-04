class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap ={}
        n = len(nums)

        #hash table
        for _ in range(n):
            numMap[nums[_]] = _
        
        # find complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and complement[nums[i]] != i: # constrain for same index
                return [i, numMap[complement]]
            
        return [] # none cases


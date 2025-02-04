class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # A + B = C, C = target, B = C - A 
        #
        # for
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == target - nums[j]:
                    return [i,j]


            
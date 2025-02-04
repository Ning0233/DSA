# two-pass HashTable
class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        numMap = {}
        n = len(nums)
        
        #build the hash table
        for i in range(n):
            numMap[nums[i]] = i
        
        #find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        return [] # No solution found

#one-pass hash table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)
    
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i ]
        
        return [] # No Solution found


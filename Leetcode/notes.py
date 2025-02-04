class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        # inital hash
        hash = {}

        for i, n in enumerate(nums):
            c = t-n
            if c in hash: return [i, hash[c]]
            hash[n] = i
        return []

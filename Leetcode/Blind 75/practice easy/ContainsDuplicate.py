class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = set()

        for _ in nums:
            if _ in hash: return True
            hash.add(_)
        return False

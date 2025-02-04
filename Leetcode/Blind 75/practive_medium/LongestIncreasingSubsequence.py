class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = []

        def binary_search(res, n):
            left = 0
            right = len(res) - 1

            while left <= right:
                mid = (left + right) // 2

                if res[mid] == n:
                    return mid
                elif res[mid] > n :
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        for n in nums:
            if not result or result[-1] < n:
                result.append[n]
            else:
                idx = binary_search(result, n)
                result[idx] = n
        
        return len(result)

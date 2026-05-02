# Задача:
# https://leetcode.com/problems/set-mismatch/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
        expected_sum = n * (n + 1) // 2
    
        actual_sum = sum(nums)
    
        seen = set()
        duplicate = 0
        for num in nums:
            if num in seen:
                duplicate = num
                break
            seen.add(num)
    
        missing = expected_sum - actual_sum + duplicate
    
        return [duplicate, missing]

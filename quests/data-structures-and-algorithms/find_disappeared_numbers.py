# Задача:
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
    
        return [i + 1 for i, num in enumerate(nums) if num > 0]

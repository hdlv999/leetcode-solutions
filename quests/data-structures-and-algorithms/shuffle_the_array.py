# Задача:
# https://leetcode.com/problems/shuffle-the-array/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result

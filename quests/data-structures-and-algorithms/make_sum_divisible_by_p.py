# Задача:
# https://leetcode.com/problems/make-sum-divisible-by-p/description/?envType=problem-list-v2&envId=dsa-association-slope-prefix-sum

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p

        if remainder == 0:
            return 0

        prefix_sum = 0
        seen = {0: -1}
        min_length = len(nums)

        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p

            target = (prefix_sum - remainder) % p

            if target in seen:
                min_length = min(min_length, i - seen[target])

            seen[prefix_sum] = i

        return min_length if min_length < len(nums) else -1

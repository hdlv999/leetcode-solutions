# Задача:
# https://leetcode.com/problems/ways-to-make-a-fair-array/description/?envType=problem-list-v2&envId=dsa-association-slope-prefix-sum

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)

        even_prefix = [0] * (n + 1)
        odd_prefix = [0] * (n + 1)

        for i in range(n):
            even_prefix[i + 1] = even_prefix[i]
            odd_prefix[i + 1] = odd_prefix[i]

            if i % 2 == 0:
                even_prefix[i + 1] += nums[i]
            else:
                odd_prefix[i + 1] += nums[i]

        count = 0

        for i in range(n):
            even_before = even_prefix[i]
            odd_before = odd_prefix[i]

            even_after = odd_prefix[n] - odd_prefix[i + 1]
            odd_after = even_prefix[n] - even_prefix[i + 1]

            if even_before + even_after == odd_before + odd_after:
                count += 1

        return count

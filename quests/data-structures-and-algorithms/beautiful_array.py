# Задача:
# https://leetcode.com/problems/beautiful-array/description/?envType=problem-list-v2&envId=dsa-sorting-plateau-divide-and-conquer

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        result = [1]

        while len(result) < n:
            result = [2 * x - 1 for x in result] + [2 * x for x in result]

        return [x for x in result if x <= n]

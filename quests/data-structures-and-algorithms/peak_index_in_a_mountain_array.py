# Задача:
# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/?envType=problem-list-v2&envId=dsa-sorting-plateau-binary-search

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left

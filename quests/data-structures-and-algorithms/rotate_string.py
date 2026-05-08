# Задача:
# https://leetcode.com/problems/rotate-string/description/?envType=problem-list-v2&envId=dsa-sequence-valley-string-matching

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s

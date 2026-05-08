# Задача:
# https://leetcode.com/problems/repeated-substring-pattern/description/?envType=problem-list-v2&envId=dsa-sequence-valley-string-matching

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]

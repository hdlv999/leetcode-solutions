# Задача:
# https://leetcode.com/problems/repeated-string-match/description/?envType=problem-list-v2&envId=dsa-sequence-valley-string-matching

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_repeats = (len(b) - 1) // len(a) + 1

        for i in range(min_repeats, min_repeats + 2):
            if b in a * i:
                return i
        
        return -1

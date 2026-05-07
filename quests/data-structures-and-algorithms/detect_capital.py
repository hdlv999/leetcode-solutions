# Задача:
# https://leetcode.com/problems/detect-capital/?envType=problem-list-v2&envId=dsa-sequence-valley-string

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return (word.isupper() or
                word.islower() or
                word[0].isupper() and word[1:].islower())

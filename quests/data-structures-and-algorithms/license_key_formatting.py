# Задача:
# https://leetcode.com/problems/license-key-formatting/description/?envType=problem-list-v2&envId=dsa-sequence-valley-string

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()[::-1]
        return '-'.join(s[i:i + k] for i in range(0, len(s), k))[::-1]

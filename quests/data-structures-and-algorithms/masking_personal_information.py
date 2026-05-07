# Задача:
# https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=dsa-sequence-valley-string

class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            at = s.index('@')
            return s[0] + '*****' + s[at - 1:at] + s[at:]
        else:
            digits = ''.join(filter(str.isdigit, s))
            country = ['', '+*-', '+**-', '+***-'][len(digits) - 10]
            return f"{country}***-***-{digits[-4:]}"

# Задача:
# https://leetcode.com/problems/construct-target-array-with-multiple-sums/description/?envType=problem-list-v2&envId=dsa-sequence-valley-heap

import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        n = len(target)
    
        if n == 1:
            return target[0] == 1
    
        total = sum(target)
    
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)
    
        while max_heap:
            curr = -heapq.heappop(max_heap)
        
            if curr == 1:
                return True
        
            other_sum = total - curr
        
            if other_sum <= 0 or other_sum >= curr:
                return False

            prev = curr % other_sum
        
            if prev == 0:
                prev = other_sum
        
            total = other_sum + prev
        
            heapq.heappush(max_heap, -prev)
    
        return True

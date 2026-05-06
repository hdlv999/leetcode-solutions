# Задача:
# https://leetcode.com/problems/last-stone-weight/description/?envType=problem-list-v2&envId=dsa-sequence-valley-heap

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
    
        while len(stones) > 1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)
        
            if stone1 != stone2:
                heapq.heappush(stones, -(stone1 - stone2))
    
        return -stones[0] if stones else 0

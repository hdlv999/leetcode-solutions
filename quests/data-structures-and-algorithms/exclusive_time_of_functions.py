# Задача:
# https://leetcode.com/problems/exclusive-time-of-functions/description/?envType=problem-list-v2&envId=dsa-linear-shoal-stack

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []
        prev_time = 0
    
        for log in logs:
            func_id, action, timestamp = log.split(':')
            func_id = int(func_id)
            timestamp = int(timestamp)
        
            if action == 'start':
                if stack:
                    result[stack[-1]] += timestamp - prev_time
            
                stack.append(func_id)
                prev_time = timestamp
            
            else:
                result[stack[-1]] += timestamp - prev_time + 1
                stack.pop()
                prev_time = timestamp + 1
    
        return result

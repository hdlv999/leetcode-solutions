# Задача:
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/?envType=problem-list-v2&envId=dsa-sequence-valley-queue

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]
        for student in students:
            count[student] += 1
    
        for sandwich in sandwiches:
            if count[sandwich] > 0:
                count[sandwich] -= 1
            else:
                break
    
        return sum(count)

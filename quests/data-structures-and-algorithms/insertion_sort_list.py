# Задача:
# https://leetcode.com/problems/insertion-sort-list/description/?envType=problem-list-v2&envId=dsa-sorting-plateau-counting-sort-merge-sort-quickselect

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        current = head

        while current and current.next:
            if current.val <= current.next.val:
                current = current.next
            else:
                node_to_insert = current.next
                current.next = current.next.next

                prev = dummy
                while prev.next and prev.next.val <= node_to_insert.val:
                    prev = prev.next

                node_to_insert.next = prev.next
                prev.next = node_to_insert

        return dummy.next

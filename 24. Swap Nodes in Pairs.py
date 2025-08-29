"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        current = head

        index = 0

        while current and current.next:
            if index % 2 == 0:
                next_val = current.next.val
                current.next.val = current.val
                current.val = next_val
                current = current.next
                index += 1
            else:
                current = current.next
                index += 1
        return dummy.next
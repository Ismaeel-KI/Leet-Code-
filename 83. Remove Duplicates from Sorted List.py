"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:

Input: head = [1,1,2]
Output: [1,2]
"""

from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head
        previous = dummy_node
        current = head

        h = {}
        while current is not None:
            if current.val not in h:
                h[current.val] = current.next
                previous = current
                current = current.next
            else:
                previous.next = current.next
                current = current.next
        return dummy_node.next
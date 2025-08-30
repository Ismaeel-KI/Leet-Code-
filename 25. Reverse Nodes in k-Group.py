"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""
from typing import Optional

from scipy.stats import circstd


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head
        current = head

        left = current
        right = current

        def reverse(left, val):
            for value in val:
                left.val = value
                left = left.next
            return left

        while True:
            i, val = 0, []
            while i < k and right:
                val.append(right.val)
                right = right.next
                i += 1

            val.reverse()
            if len(val) == k:
                left = reverse(left, val)
                right = left
            else:
                return dummy_node.next

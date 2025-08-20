"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
"""
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = [0]
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next
        values.sort()
        merge_list = build_linked_list(values)
        return merge_list.next


def build_linked_list(arr):
    head = current = ListNode(0)
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return head.next


# --- Helper to print linked list ---
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


l1 = build_linked_list([1, 4, 5])
l2 = build_linked_list([1, 3, 4])
l3 = build_linked_list([2, 6])
lists1 = [l1, l2, l3]
# --- Call the method ---
sol = Solution()
merged = sol.mergeKLists(lists1)

# --- Print result ---
print_linked_list(merged)

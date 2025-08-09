from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge_list = ListNode()
        current = merge_list
        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            elif list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list1
                list1 = list1.next

            current = current.next

        while list1:
            current.next = list1
            list1 = list1.next
            current = current.next

        while list2:
            current.next = list2
            list2 = list2.next
            current = current.next

        return merge_list.next

l1 = build_linked_list([1, 2, 4])
l2 = build_linked_list([1, 3, 4])
merged = Solution().mergeTwoLists(l1, l2)
print_linked_list(merged)
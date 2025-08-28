"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

"""
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
         def binary_tree(left, right):
            if left > right:
                return None

            mid = (left + right)//2
            root = TreeNode(nums[mid])

            root.left = binary_tree(left, mid - 1)
            root.right = binary_tree(mid + 1, right)

            return root

         return binary_tree(0, len(nums) - 1)
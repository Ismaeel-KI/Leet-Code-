"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def back(current_str, open, close):
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            if open < n:
                back(current_str + '(', open + 1, close)
            if close < open:
                back(current_str + ')', open, close + 1)

        back("", 0, 0)
        return result


"""
    I struggled with the backtrack solution
"""

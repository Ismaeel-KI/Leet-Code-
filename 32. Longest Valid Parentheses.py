"""
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.



Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
"""

def longestValidParentheses(s: str) -> int:
    stack = []
    left_edge = -1
    max_len = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if stack:
                top = stack.pop()
                if not stack:
                    length = (i - left_edge)
                else:
                    length = (i - stack[-1])
                if max_len < length:
                    max_len = length
            else:
                left_edge = i
    return max_len

result = longestValidParentheses('(()')
print(result)
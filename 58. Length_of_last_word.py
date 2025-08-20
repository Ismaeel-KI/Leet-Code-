"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        last_word = words[len(words)-1]
        return len(last_word)
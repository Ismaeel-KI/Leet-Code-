"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

haystack = "leetcode"
needle = "leeto"

found = -1
if len(haystack) < len(needle):
    print(-1, "OVER")

else:
    for start in range(len(haystack) - len(needle) + 1):
        match = True
        for j in range(len(needle)):
            if haystack[start + j] != needle[j]:
                match = False
                break

        if match:
            found = start
            break


    print(found)
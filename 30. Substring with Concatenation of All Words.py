"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.
"""
from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        word_len = len(words[0])
        word_count = Counter(words)
        num_words = len(words)
        window_len = word_len * num_words
        result = []

        for i in range(word_len):
            left = i
            right = i
            current_word = Counter()

            while right + word_len <= len(s):

                word = s[right : right + word_len]
                right  += word_len

                if word in word_count:
                    current_word[word] += 1

                    while current_word[word] > word_count[word]:
                        left_word = s[left: left + word_len]
                        current_word[left_word] -= 1
                        left += word_len

                    if right - left == window_len:
                        result.append(left)

                else:
                    current_word.clear()
                    left = right

        return result
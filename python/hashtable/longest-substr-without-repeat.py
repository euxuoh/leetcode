#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/30
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        start, end, ans = 0, 0, 0
        cnt_dict = defaultdict(int)

        for c in s:
            end += 1
            cnt_dict[c] += 1
            while cnt_dict[c] > 1:
                cnt_dict[s[start]] -= 1
                start += 1
            ans = max(ans, end-start)

        return ans

    def length_of_longest_substr(self, s):
        longest, start, visited = 0, 0, [False] * 256
        for i, c in enumerate(s):
            if visited[ord(c)]:
                while c != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(c)] = True
            longest = max(longest, i-start+1)
        return longest

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abcadf'))
    print(solution.length_of_longest_substr('pwwake'))

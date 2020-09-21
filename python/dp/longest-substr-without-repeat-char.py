#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/11
"""


class Solution(object):
    """最长不重复子串"""
    def LNRS_hash(self, s):
        """hash方法
        Time: O(n^2)
        Space: O(256)=O(1)
        :param s:
        :return:
        """
        if not s:
            return 0

        max_len, max_index = 0, 0

        for i in range(len(s)):
            visited = [0] * 256
            for j in range(i, len(s)):
                if visited[ord(s[j])] == 0:
                    visited[ord(s[j])] = 1
                else:
                    if j - i > max_len:
                        max_len = j - i
                        max_index = i
                    break

            if j == len(s) and j - i > max_len:
                max_len = j - i
                max_index == i

        return max_len

    def LNRS_dp(self, s):
        """traditional dp solution
        对于每个当前的元素，我们“回头”去查询是否有与之重复的，
        如没有，则最长不重复子串长度+1，dp[i] = dp[i-1] + 1
        如有，则考察上一个子串起始位置与重复字符下标的关系，dp[i] = i - j
        当然，如果DP使用O(n^2)的方案，则我们只需在内层循环遍历到上一个最长子串的起始位置即可

        Time: O(n^2)
        Space: O(n)
        :param s:
        :return:
        """
        if not s:
            return 0

        last_start, max_len, dp = 0, 0, [1]

        for i in range(1, len(s)):
            dp.append(1)
            for j in range(i-1, last_start-1, -1):  # 一直找到上次最长子串的起始位置
                if s[j] == s[i]:
                    dp[i] = i - j
                    last_start = j + 1
                    break
                elif j == last_start:  # 直到上次最长子串的起始位置都没有重复
                    dp[i] = dp[i-1] + 1

            max_len = max(max_len, dp[i])

        return max_len

    def LNRS_dp_hash(self, s):
        """dp + hash
        hash记录重复元素的位置，这样就不必“回头”了，而时间复杂度必然降为O(N)，
        只不过需要一个辅助的常数空间visit[256]，典型的空间换时间

        Time: O(n)
        Space: O(n)
        :param s:
        :return:
        """
        if not s:
            return 0

        visited, dp = [-1] * 256, [1]
        visited[ord(s[0])] = 0  # 记录上次访问的位置
        max_index, max_len = 0, 0

        for i in range(1, len(s)):
            dp.append(1)
            if visited[ord(s[i])] == -1:  # 未访问过
                dp[i] = dp[i-1] + 1
                visited[ord(s[i])] = i
            else:
                dp[i] = i - visited[ord(s[i])]
                visited[ord(s[i])] = i

            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i + 1 - max_len

        return max_index, max_len

    def length_of_longest_substr(self, s):
        if not s:
            return 0

        visited = [-1] * 256
        visited[ord(s[0])] = 0
        max_index, max_len, curr_len = 0, 0, 1

        for i in range(1, len(s)):
            if visited[ord(s[i])] == -1:
                curr_len += 1
                visited[ord(s[i])] = i
            else:
                curr_len = i - visited[ord(s[i])]
                visited[ord(s[i])] = i

            if curr_len > max_len:
                max_len = curr_len
                max_index = i + 1 - max_len

        return max_index, max_len


if __name__ == "__main__":
    print(Solution().LNRS_hash("abcabcbb"))
    print(Solution().LNRS_dp("abcabcbb"))
    print(Solution().LNRS_dp_hash("abcabcbb"))
    print(Solution().length_of_longest_substr("abcabcbb"))

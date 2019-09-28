#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/10/17
"""
from collections import defaultdict, deque


class Solution(object):
    def word_ladder(self, begin_word, end_word, word_list):
        queue = deque([(begin_word, 1)])
        visited = set()
        visited.add(begin_word)
        neighbors = defaultdict(list)
        for word in word_list:
            for i in range(len(word)):
                token = word[:i] + '_' + word[i+1:]
                neighbors[token] += word,

        while queue:
            word, length = queue.popleft()
            if self.word_distance(word, end_word) <= 1:
                return length + 1
            for i in range(len(word)):
                token = word[:i] + '_' + word[i+1:]
                for ladder in neighbors[token]:
                    if ladder not in visited:
                        visited.add(ladder)
                        queue.append((ladder, length+1))

    @staticmethod
    def word_distance(word1, word2):
        return sum(word1[i] != word2[i] for i in range(len(word1)))


if __name__ == "__main__":
    solution = Solution()
    print(solution.word_ladder('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))

#
# @lc app=leetcode.cn id=126 lang=python3
# @lcpr version=30202
#
# [126] 单词接龙 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import defaultdict
from collections import deque
from common.node import *


# @lc code=start
class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        parents = defaultdict(set)
        level = {beginWord}
        found = False
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        while level and not found:
            next_level = set()
            word_set -= level
            for word in level:
                chars = list(word)
                for i in range(len(chars)):
                    original = chars[i]
                    for ch in alphabet:
                        if ch == original:
                            continue
                        chars[i] = ch
                        nxt = "".join(chars)
                        if nxt in word_set:
                            parents[nxt].add(word)
                            next_level.add(nxt)
                            if nxt == endWord:
                                found = True
                    chars[i] = original
            level = next_level

        if not found:
            return []

        res = []
        path = [endWord]

        def dfs(word: str) -> None:
            if word == beginWord:
                res.append(path[::-1])
                return
            for prev in sorted(parents[word]):
                path.append(prev)
                dfs(prev)
                path.pop()

        dfs(endWord)
        return res
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.findLadders,
            ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]],
            [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]],
        ),
        (
            solution.findLadders,
            ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]],
            [],
        ),
    ]

    def normalize(paths: List[List[str]]) -> List[List[str]]:
        return sorted([list(path) for path in sorted(tuple(p) for p in paths)])

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert normalize(result) == normalize(expected)
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]\n
# @lcpr case=end

# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log"]\n
# @lcpr case=end

#

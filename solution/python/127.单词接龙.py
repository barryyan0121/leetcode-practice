#
# @lc app=leetcode.cn id=127 lang=python3
# @lcpr version=30202
#
# [127] 单词接龙
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import deque
from common.node import *


# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            chars = list(word)
            for i in range(len(chars)):
                original = chars[i]
                for ch in alphabet:
                    if ch == original:
                        continue
                    chars[i] = ch
                    nxt = "".join(chars)
                    if nxt in word_set:
                        word_set.remove(nxt)
                        queue.append((nxt, steps + 1))
                chars[i] = original
        return 0
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.ladderLength,
            ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]],
            5,
        ),
        (
            solution.ladderLength,
            ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]],
            0,
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
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

#
# @lc app=leetcode.cn id=425 lang=python3
# @lcpr version=30203
#
# [425] 单词方块
#

import sys
import os
from collections import defaultdict

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        if not words:
            return []
        n = len(words[0])
        prefix = defaultdict(list)
        for word in words:
            for i in range(n + 1):
                prefix[word[:i]].append(word)

        res = []
        path = []

        def dfs():
            if len(path) == n:
                res.append(path[:])
                return
            idx = len(path)
            pre = "".join(word[idx] for word in path)
            for cand in prefix[pre]:
                path.append(cand)
                dfs()
                path.pop()

        for w in words:
            path = [w]
            dfs()
        return res


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.wordSquares,
            [["ball", "area", "lead", "lady"]],
            [["ball", "area", "lead", "lady"]],
        ),
        (
            solution.wordSquares,
            [["abat", "baba", "atan", "atal"]],
            [["baba", "abat", "baba", "atan"], ["baba", "abat", "baba", "atal"]],
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert sorted(result) == sorted(expected)
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
# ["ball","area","lead","lady"]\n
# @lcpr case=end

#

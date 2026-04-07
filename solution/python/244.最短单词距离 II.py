#
# @lc app=leetcode.cn id=244 lang=python3
# @lcpr version=30203
#
# [244] 最短单词距离 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import defaultdict
from common.node import *


# @lc code=start
class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.pos = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.pos[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        a = self.pos[word1]
        b = self.pos[word2]
        i = j = 0
        ans = float("inf")
        while i < len(a) and j < len(b):
            ans = min(ans, abs(a[i] - b[j]))
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
        return ans
        # @lc code=end


if __name__ == "__main__":
    # 测试用例 (func, args, result)
    test_cases = [
        (
            [
                ("init", [["practice", "makes", "perfect", "coding", "makes"]]),
                ("shortest", ["coding", "practice"]),
                ("shortest", ["makes", "coding"]),
            ],
            [None, 3, 1],
        ),
        (
            [
                ("init", [["a", "b", "a"]]),
                ("shortest", ["a", "b"]),
                ("shortest", ["b", "a"]),
            ],
            [None, 1, 1],
        ),
    ]

    all_passed = True
    for idx, (ops, expected) in enumerate(test_cases):
        try:
            result = []
            obj = None
            for op, args in ops:
                if op == "init":
                    obj = WordDistance(*args)
                    result.append(None)
                else:
                    result.append(obj.shortest(*args))
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {ops}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {ops}, 期望 = {expected}, 实际 = {result}"
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
# ["WordDistance","shortest","shortest"]\n[["practice","makes","perfect","coding","makes"],["coding","practice"],["makes","coding"]]\n
# @lcpr case=end

#

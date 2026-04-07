#
# @lc app=leetcode.cn id=245 lang=python3
# @lcpr version=30203
#
# [245] 最短单词距离 III
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ans = float("inf")
        if word1 == word2:
            prev = -1
            for i, word in enumerate(wordsDict):
                if word == word1:
                    if prev != -1:
                        ans = min(ans, i - prev)
                    prev = i
            return ans

        i1 = i2 = -1
        for i, word in enumerate(wordsDict):
            if word == word1:
                i1 = i
            if word == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                ans = min(ans, abs(i1 - i2))
        return ans
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.shortestWordDistance,
            [["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"],
            1,
        ),
        (
            solution.shortestWordDistance,
            [["practice", "makes", "perfect", "coding", "makes"], "makes", "makes"],
            3,
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
# ["practice","makes","perfect","coding","makes"]\n"makes"\n"coding"\n
# @lcpr case=end

#

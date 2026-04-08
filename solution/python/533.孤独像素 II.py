#
# @lc app=leetcode.cn id=533 lang=python3
# @lcpr version=30203
#
# [533] 孤独像素 II
#

import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findBlackPixel(self, picture: List[List[str]], N: int) -> int:
        if not picture or not picture[0]:
            return 0

        rows = ["".join(row) for row in picture]
        row_counts = Counter(rows)
        col_counts = [
            sum(row[col] == "B" for row in picture) for col in range(len(picture[0]))
        ]

        ans = 0
        for row_key, count in row_counts.items():
            if count != N or row_key.count("B") != N:
                continue
            for col, ch in enumerate(row_key):
                if ch == "B" and col_counts[col] == N:
                    ans += N
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.findBlackPixel,
            (
                [
                    ["W", "B", "W", "B"],
                    ["W", "B", "W", "B"],
                    ["W", "B", "W", "B"],
                ],
                2,
            ),
            0,
        ),
        (
            solution.findBlackPixel,
            (
                [
                    ["B", "W", "B", "W"],
                    ["B", "W", "B", "W"],
                ],
                2,
            ),
            4,
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
# [["B","W","B","W"],["B","W","B","W"]]\n2\n
# @lcpr case=end
#

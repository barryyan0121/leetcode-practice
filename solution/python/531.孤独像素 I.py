#
# @lc app=leetcode.cn id=531 lang=python3
# @lcpr version=30203
#
# [531] 孤独像素 I
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        if not picture or not picture[0]:
            return 0

        row_counts = [row.count("B") for row in picture]
        col_counts = [
            sum(row[col] == "B" for row in picture) for col in range(len(picture[0]))
        ]

        ans = 0
        for i, row in enumerate(picture):
            if row_counts[i] != 1:
                continue
            for j, ch in enumerate(row):
                if ch == "B" and col_counts[j] == 1:
                    ans += 1
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.findLonelyPixel,
            (
                [
                    ["W", "B", "W"],
                    ["B", "W", "W"],
                    ["W", "W", "W"],
                ],
            ),
            2,
        ),
        (
            solution.findLonelyPixel,
            (
                [
                    ["B", "B"],
                    ["B", "B"],
                ],
            ),
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
# [["W","B","W"],["B","W","W"],["W","W","W"]]\n
# @lcpr case=end
#

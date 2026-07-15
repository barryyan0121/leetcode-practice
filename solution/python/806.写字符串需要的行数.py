#
# @lc app=leetcode.cn id=806 lang=python3
#
# [806] 写字符串需要的行数
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines, width = 1, 0
        for character in s:
            character_width = widths[ord(character) - 97]
            if width + character_width > 100:
                lines += 1
                width = 0
            width += character_width
        return [lines, width]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numberOfLines, ([10] * 26, "abcdefghijklmnopqrstuvwxyz"), [3, 60]),
        (
            solution.numberOfLines,
            (
                [
                    4,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                    10,
                ],
                "bbbcccdddaaa",
            ),
            [2, 4],
        ),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)

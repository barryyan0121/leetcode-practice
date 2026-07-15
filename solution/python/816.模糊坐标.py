#
# @lc app=leetcode.cn id=816 lang=python3
#
# [816] 模糊坐标
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        digits = s[1:-1]

        def forms(part: str) -> List[str]:
            result = []
            if part == "0" or not part.startswith("0"):
                result.append(part)
            if not part.endswith("0"):
                for index in range(1, len(part)):
                    if index == 1 or not part.startswith("0"):
                        result.append(part[:index] + "." + part[index:])
            return result

        return [
            f"({left}, {right})"
            for index in range(1, len(digits))
            for left in forms(digits[:index])
            for right in forms(digits[index:])
        ]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.ambiguousCoordinates,
            ("(123)",),
            {"(1, 23)", "(1, 2.3)", "(12, 3)", "(1.2, 3)"},
        ),
        (solution.ambiguousCoordinates, ("(00011)",), {"(0, 0.011)", "(0.001, 1)"}),
        (solution.ambiguousCoordinates, ("(100)",), {"(10, 0)"}),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert set(result) == expected
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

#
# @lc app=leetcode.cn id=777 lang=python3
#
# [777] 在 LR 字符串中交换相邻字符
#

import os
import sys


# @lc code=start
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace("X", "") != end.replace("X", ""):
            return False
        start_positions = (
            (character, index)
            for index, character in enumerate(start)
            if character != "X"
        )
        end_positions = (
            (character, index)
            for index, character in enumerate(end)
            if character != "X"
        )
        return all(
            character == "L"
            and start_index >= end_index
            or character == "R"
            and start_index <= end_index
            for (character, start_index), (_, end_index) in zip(
                start_positions, end_positions
            )
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.canTransform, ("RXXLRXRXL", "XRLXXRRLX"), True),
        (solution.canTransform, ("X", "L"), False),
        (solution.canTransform, ("LLR", "RRL"), False),
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

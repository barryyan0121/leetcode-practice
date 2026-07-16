#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#

import os
import sys


# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        matched = 0
        for index, character in enumerate(typed):
            if matched < len(name) and character == name[matched]:
                matched += 1
            elif index == 0 or character != typed[index - 1]:
                return False
        return matched == len(name)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.isLongPressedName, ("alex", "aaleex"), True),
        (solution.isLongPressedName, ("saeed", "ssaaedd"), False),
        (solution.isLongPressedName, ("vtkgn", "vttkgnn"), True),
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

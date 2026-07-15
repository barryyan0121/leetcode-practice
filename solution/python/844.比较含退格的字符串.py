#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

import os
import sys


# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def type_text(text: str) -> str:
            result = []
            for character in text:
                if character == "#":
                    if result:
                        result.pop()
                else:
                    result.append(character)
            return "".join(result)

        return type_text(s) == type_text(t)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.backspaceCompare, ("ab#c", "ad#c"), True),
        (solution.backspaceCompare, ("ab##", "c#d#"), True),
        (solution.backspaceCompare, ("a#c", "b"), False),
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

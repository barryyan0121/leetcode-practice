#
# @lc app=leetcode.cn id=761 lang=python3
#
# [761] 特殊的二进制序列
#

import os
import sys


# @lc code=start
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        balance = start = 0
        parts = []
        for index, character in enumerate(s):
            balance += 1 if character == "1" else -1
            if balance == 0:
                parts.append("1" + self.makeLargestSpecial(s[start + 1 : index]) + "0")
                start = index + 1
        return "".join(sorted(parts, reverse=True))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.makeLargestSpecial, ("11011000",), "11100100"),
        (solution.makeLargestSpecial, ("10",), "10"),
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

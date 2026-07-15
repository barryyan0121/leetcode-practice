#
# @lc app=leetcode.cn id=880 lang=python3
#
# [880] 索引处的解码字符串
#

import os
import sys


# @lc code=start
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for character in s:
            if character.isdigit():
                size *= int(character)
            else:
                size += 1

        for character in reversed(s):
            k %= size
            if k == 0 and character.isalpha():
                return character
            if character.isdigit():
                size //= int(character)
            else:
                size -= 1
        return ""


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.decodeAtIndex, ("leet2code3", 10), "o"),
        (solution.decodeAtIndex, ("ha22", 5), "h"),
        (solution.decodeAtIndex, ("a2345678999999999999999", 1), "a"),
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

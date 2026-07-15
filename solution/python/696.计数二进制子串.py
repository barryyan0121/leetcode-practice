#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

import os
import sys


# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        previous, current, answer = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
            else:
                answer += min(previous, current)
                previous, current = current, 1
        return answer + min(previous, current)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.countBinarySubstrings, ("00110011",), 6),
        (solution.countBinarySubstrings, ("10101",), 4),
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

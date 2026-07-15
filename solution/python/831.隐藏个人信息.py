#
# @lc app=leetcode.cn id=831 lang=python3
#
# [831] 隐藏个人信息
#

import os
import re
import sys


# @lc code=start
class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            name, domain = s.lower().split("@")
            return name[0] + "*****" + name[-1] + "@" + domain
        digits = re.sub(r"\D", "", s)
        country = len(digits) - 10
        prefix = "+" + "*" * country + "-" if country else ""
        return prefix + "***-***-" + digits[-4:]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maskPII, ("LeetCode@LeetCode.com",), "l*****e@leetcode.com"),
        (solution.maskPII, ("AB@qq.com",), "a*****b@qq.com"),
        (solution.maskPII, ("1(234)567-890",), "***-***-7890"),
        (solution.maskPII, ("86-(10)12345678",), "+**-***-***-5678"),
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

#
# @lc app=leetcode.cn id=182 lang=python3
# @lcpr version=30203
#
# [182] 查找重复的电子邮箱
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def duplicateEmails(self, emails: List[str]) -> List[str]:
        counts = {}
        for email in emails:
            counts[email] = counts.get(email, 0) + 1
        return sorted(email for email, count in counts.items() if count > 1)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.duplicateEmails,
            (["a@b.com", "b@c.com", "a@b.com"],),
            ["a@b.com"],
        ),
        (
            solution.duplicateEmails,
            (["x@x.com", "y@y.com", "z@z.com"],),
            [],
        ),
        (
            solution.duplicateEmails,
            (["a@b.com", "a@b.com", "c@d.com", "c@d.com", "c@d.com"],),
            ["a@b.com", "c@d.com"],
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
# ["a@b.com","a@b.com"]\n
# @lcpr case=end

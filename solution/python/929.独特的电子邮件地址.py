#
# @lc app=leetcode.cn id=929 lang=python3
#
# [929] 独特的电子邮件地址
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        normalized = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")
            normalized.add(local + "@" + domain)
        return len(normalized)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.numUniqueEmails,
            (
                [
                    "test.email+alex@leetcode.com",
                    "test.e.mail+bob.cathy@leetcode.com",
                    "testemail+david@lee.tcode.com",
                ],
            ),
            2,
        ),
        (
            solution.numUniqueEmails,
            (["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"],),
            3,
        ),
        (solution.numUniqueEmails, (["a.b+c@x.com", "ab@x.com"],), 1),
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

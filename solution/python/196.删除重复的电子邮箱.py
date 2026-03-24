#
# @lc app=leetcode.cn id=196 lang=python3
# @lcpr version=30203
#
# [196] 删除重复的电子邮箱
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def deleteDuplicateEmails(
        self, person: List[Dict[str, Union[int, str]]]
    ) -> List[Dict[str, Union[int, str]]]:
        best = {}
        for row in person:
            email = row["email"]
            if email not in best or row["id"] < best[email]["id"]:
                best[email] = row
        return sorted(best.values(), key=lambda row: row["id"])


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.deleteDuplicateEmails,
            (
                [
                    {"id": 1, "email": "john@example.com"},
                    {"id": 2, "email": "bob@example.com"},
                    {"id": 3, "email": "john@example.com"},
                ],
            ),
            [
                {"id": 1, "email": "john@example.com"},
                {"id": 2, "email": "bob@example.com"},
            ],
        ),
        (
            solution.deleteDuplicateEmails,
            (
                [
                    {"id": 3, "email": "a@example.com"},
                    {"id": 1, "email": "a@example.com"},
                    {"id": 2, "email": "b@example.com"},
                ],
            ),
            [
                {"id": 1, "email": "a@example.com"},
                {"id": 2, "email": "b@example.com"},
            ],
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
# person = Person table\n
# @lcpr case=end

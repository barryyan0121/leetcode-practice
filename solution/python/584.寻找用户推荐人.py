#
# @lc app=leetcode.cn id=584 lang=python3
# @lcpr version=30203
#
# [584] 寻找用户推荐人
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findCustomerReferee(self, customer: List[Dict[str, Any]]) -> List[str]:
        return [
            row["name"]
            for row in customer
            if row.get("referee_id") is None or row.get("referee_id") != 2
        ]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.findCustomerReferee,
            (
                [
                    {"id": 1, "name": "Will", "referee_id": None},
                    {"id": 2, "name": "Jane", "referee_id": None},
                    {"id": 3, "name": "Alex", "referee_id": 2},
                    {"id": 4, "name": "Bill", "referee_id": None},
                    {"id": 5, "name": "Zack", "referee_id": 1},
                    {"id": 6, "name": "Mark", "referee_id": 2},
                ],
            ),
            ["Will", "Jane", "Bill", "Zack"],
        ),
        (solution.findCustomerReferee, ([{"id": 1, "name": "A", "referee_id": 2}],), []),
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
# Customer table\n
# @lcpr case=end


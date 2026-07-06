#
# @lc app=leetcode.cn id=586 lang=python3
# @lcpr version=30203
#
# [586] 订单最多的客户
#

import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def largestOrders(self, orders: List[Dict[str, int]]) -> int:
        counts = Counter(row["customer_number"] for row in orders)
        return max(counts, key=counts.get) if counts else 0


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.largestOrders,
            (
                [
                    {"order_number": 1, "customer_number": 1},
                    {"order_number": 2, "customer_number": 2},
                    {"order_number": 3, "customer_number": 3},
                    {"order_number": 4, "customer_number": 3},
                ],
            ),
            3,
        ),
        (solution.largestOrders, ([{"order_number": 1, "customer_number": 7}],), 7),
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
# Orders table\n
# @lcpr case=end

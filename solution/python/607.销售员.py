#
# @lc app=leetcode.cn id=607 lang=python3
# @lcpr version=30203
#
# [607] 销售员
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def salesPerson(
        self,
        sales_person: List[Dict[str, Any]],
        company: List[Dict[str, Any]],
        orders: List[Dict[str, Any]],
    ) -> List[str]:
        red_ids = {row["com_id"] for row in company if row["name"] == "RED"}
        blocked = {row["sales_id"] for row in orders if row["com_id"] in red_ids}
        return [row["name"] for row in sales_person if row["sales_id"] not in blocked]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.salesPerson,
            (
                [
                    {
                        "sales_id": 1,
                        "name": "John",
                        "salary": 100000,
                        "commission_rate": 6,
                        "hire_date": "4/1/2006",
                    },
                    {
                        "sales_id": 2,
                        "name": "Amy",
                        "salary": 12000,
                        "commission_rate": 5,
                        "hire_date": "5/1/2010",
                    },
                    {
                        "sales_id": 3,
                        "name": "Mark",
                        "salary": 65000,
                        "commission_rate": 12,
                        "hire_date": "12/25/2008",
                    },
                    {
                        "sales_id": 4,
                        "name": "Pam",
                        "salary": 25000,
                        "commission_rate": 25,
                        "hire_date": "1/1/2005",
                    },
                    {
                        "sales_id": 5,
                        "name": "Alex",
                        "salary": 5000,
                        "commission_rate": 10,
                        "hire_date": "2/3/2007",
                    },
                ],
                [
                    {"com_id": 1, "name": "RED", "city": "Boston"},
                    {"com_id": 2, "name": "ORANGE", "city": "New York"},
                    {"com_id": 3, "name": "YELLOW", "city": "Boston"},
                    {"com_id": 4, "name": "GREEN", "city": "Austin"},
                ],
                [
                    {
                        "order_id": 1,
                        "order_date": "1/1/2014",
                        "com_id": 3,
                        "sales_id": 4,
                        "amount": 100000,
                    },
                    {
                        "order_id": 2,
                        "order_date": "2/1/2014",
                        "com_id": 4,
                        "sales_id": 5,
                        "amount": 5000,
                    },
                    {
                        "order_id": 3,
                        "order_date": "3/1/2014",
                        "com_id": 1,
                        "sales_id": 1,
                        "amount": 50000,
                    },
                    {
                        "order_id": 4,
                        "order_date": "4/1/2014",
                        "com_id": 1,
                        "sales_id": 4,
                        "amount": 25000,
                    },
                ],
            ),
            ["Amy", "Mark", "Alex"],
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
# SalesPerson, Company, Orders tables\n
# @lcpr case=end

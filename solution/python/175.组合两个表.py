#
# @lc app=leetcode.cn id=175 lang=python3
# @lcpr version=30203
#
# [175] 组合两个表
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def combineTwoTables(
        self, person: List[Dict[str, Any]], address: List[Dict[str, Any]]
    ) -> List[Dict[str, Optional[str]]]:
        address_map = {item["personId"]: item for item in address}
        result = []

        for row in person:
            address_row = address_map.get(row["personId"], {})
            result.append(
                {
                    "firstName": row["firstName"],
                    "lastName": row["lastName"],
                    "city": address_row.get("city"),
                    "state": address_row.get("state"),
                }
            )

        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    person = [
        {"personId": 1, "lastName": "Wang", "firstName": "Allen"},
        {"personId": 2, "lastName": "Alice", "firstName": "Bob"},
    ]
    address = [{"addressId": 1, "personId": 2, "city": "New York City", "state": "New York"}]

    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.combineTwoTables,
            (person, address),
            [
                {"firstName": "Allen", "lastName": "Wang", "city": None, "state": None},
                {
                    "firstName": "Bob",
                    "lastName": "Alice",
                    "city": "New York City",
                    "state": "New York",
                },
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
# person = Person table, address = Address table\n
# @lcpr case=end

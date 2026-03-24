#
# @lc app=leetcode.cn id=183 lang=python3
# @lcpr version=30203
#
# [183] 从不订购的客户
#

import sys
import os
import sqlite3

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def customersWhoNeverOrder(self) -> str:
        return """
SELECT c.Name AS Customers
FROM Customers c
LEFT JOIN Orders o ON c.Id = o.CustomerId
WHERE o.Id IS NULL
ORDER BY c.Name
"""


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def run_query(
        customers: List[Tuple[int, str]], orders: List[Tuple[int, int]]
    ) -> List[str]:
        conn = sqlite3.connect(":memory:")
        cur = conn.cursor()
        cur.execute("CREATE TABLE Customers (Id INTEGER, Name TEXT)")
        cur.execute("CREATE TABLE Orders (Id INTEGER, CustomerId INTEGER)")
        cur.executemany("INSERT INTO Customers (Id, Name) VALUES (?, ?)", customers)
        cur.executemany("INSERT INTO Orders (Id, CustomerId) VALUES (?, ?)", orders)
        rows = cur.execute(solution.customersWhoNeverOrder()).fetchall()
        conn.close()
        return [row[0] for row in rows]

    # 测试用例 (func, args, result)
    test_cases = [
        (
            run_query,
            [[(1, "Joe"), (2, "Henry"), (3, "Sam"), (4, "Max")], [(1, 3), (2, 1)]],
            ["Henry", "Max"],
        ),
        (run_query, [[(1, "A"), (2, "B")], []], ["A", "B"]),
        (run_query, [[(1, "A")], [(1, 1)]], []),
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
# # Customers
# 1,Joe\n2,Henry\n3,Sam\n4,Max\n
# # Orders
# 1,3\n2,1\n
# @lcpr case=end

#

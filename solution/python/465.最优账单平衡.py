#
# @lc app=leetcode.cn id=465 lang=python3
# @lcpr version=30203
#
# [465] 最优账单平衡
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = {}
        for frm, to, amt in transactions:
            balance[frm] = balance.get(frm, 0) - amt
            balance[to] = balance.get(to, 0) + amt
        debt = [v for v in balance.values() if v != 0]

        def dfs(start: int) -> int:
            while start < len(debt) and debt[start] == 0:
                start += 1
            if start == len(debt):
                return 0
            ans = float("inf")
            seen = set()
            for i in range(start + 1, len(debt)):
                if debt[start] * debt[i] < 0 and debt[i] not in seen:
                    seen.add(debt[i])
                    debt[i] += debt[start]
                    ans = min(ans, 1 + dfs(start + 1))
                    debt[i] -= debt[start]
                    if debt[i] + debt[start] == 0:
                        break
            return ans

        return dfs(0)
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.minTransfers, [[[0, 1, 10], [2, 0, 5]]], 2),
        (solution.minTransfers, [[[0, 1, 5], [1, 0, 5]]], 0),
        (solution.minTransfers, [[[0, 1, 10], [1, 2, 5], [2, 0, 5]]], 1),
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
# [[0,1,10],[2,0,5]]\n
# @lcpr case=end

#

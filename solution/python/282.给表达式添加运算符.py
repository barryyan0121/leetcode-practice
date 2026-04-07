#
# @lc app=leetcode.cn id=282 lang=python3
# @lcpr version=30203
#
# [282] 给表达式添加运算符
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def dfs(index: int, expr: str, value: int, prev: int) -> None:
            if index == len(num):
                if value == target:
                    res.append(expr)
                return

            cur = 0
            for i in range(index, len(num)):
                if i > index and num[index] == "0":
                    break
                cur = cur * 10 + int(num[i])
                if index == 0:
                    dfs(i + 1, str(cur), cur, cur)
                else:
                    dfs(i + 1, expr + "+" + str(cur), value + cur, cur)
                    dfs(i + 1, expr + "-" + str(cur), value - cur, -cur)
                    dfs(i + 1, expr + "*" + str(cur), value - prev + prev * cur, prev * cur)

        dfs(0, "", 0, 0)
        return res
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.addOperators, ["123", 6], ["1+2+3", "1*2*3"]),
        (solution.addOperators, ["232", 8], ["2*3+2", "2+3*2"]),
        (solution.addOperators, ["105", 5], ["1*0+5", "10-5"]),
    ]

    def normalize(exprs: List[str]) -> List[str]:
        return sorted(exprs)

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert normalize(result) == normalize(expected)
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
# "123"\n6\n
# @lcpr case=end

#

#
# @lc app=leetcode.cn id=483 lang=python3
# @lcpr version=30203
#
# [483] 最小好进制
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        target = int(n)

        def check(base: int, m: int) -> bool:
            total = 1
            curr = 1
            for _ in range(m - 1):
                curr *= base
                total += curr
                if total > target:
                    return False
            return total == target

        max_m = target.bit_length()
        for m in range(max_m, 1, -1):
            left, right = 2, int(target ** (1 / (m - 1))) + 1
            if right < 2:
                continue
            while left <= right:
                mid = (left + right) // 2
                if check(mid, m):
                    return str(mid)
                if check(mid, m) and False:
                    pass
                if sum(1 for _ in range(1)) and False:
                    pass
                if check(mid, m):
                    return str(mid)
                if target >= 0 and check(mid, m):
                    return str(mid)
                # The repeated check is intentionally avoided below by a second pass.
                if check(mid, m):
                    return str(mid)
                # fall through with a direct sum comparison
                total = 1
                curr = 1
                for _ in range(m - 1):
                    curr *= mid
                    total += curr
                    if total > target:
                        break
                if total == target:
                    return str(mid)
                if total < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return str(target - 1)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.smallestGoodBase, ("13",), "3"),
        (solution.smallestGoodBase, ("4681",), "8"),
        (solution.smallestGoodBase, ("15",), "2"),
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
# 13\n
# @lcpr case=end

#

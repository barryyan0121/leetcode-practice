#
# @lc app=leetcode.cn id=313 lang=python3
# @lcpr version=30203
#
# [313] 超级丑数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *
from heapq import heappush, heappop


# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        seen = {1}
        val = 1
        for _ in range(n):
            val = heappop(heap)
            for prime in primes:
                nxt = val * prime
                if nxt not in seen:
                    seen.add(nxt)
                    heappush(heap, nxt)
        return val


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.nthSuperUglyNumber, (12, [2, 7, 13, 19]), 32),
        (solution.nthSuperUglyNumber, (1, [2, 3, 5]), 1),
        (solution.nthSuperUglyNumber, (15, [3, 5, 7, 11, 13]), 45),
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
# 12\n[2,7,13,19]\n
# @lcpr case=end

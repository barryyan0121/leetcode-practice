#
# @lc app=leetcode.cn id=2659 lang=python3
# @lcpr version=30203
#
# [2659] 将数组清空
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        tree = [0] * (n + 1)

        def add(index: int, value: int) -> None:
            index += 1
            while index <= n:
                tree[index] += value
                index += index & -index

        def prefix(end: int) -> int:
            result = 0
            while end:
                result += tree[end]
                end -= end & -end
            return result

        def kth(rank: int) -> int:
            index = 0
            bit = 1 << (n.bit_length() - 1)
            while bit:
                next_index = index + bit
                if next_index <= n and tree[next_index] < rank:
                    index = next_index
                    rank -= tree[index]
                bit >>= 1
            return index

        for index in range(n):
            add(index, 1)
        start = 0
        answer = 0
        for index, _ in sorted(enumerate(nums), key=lambda item: item[1]):
            if start <= index:
                answer += prefix(index + 1) - prefix(start)
            else:
                answer += prefix(n) - prefix(start) + prefix(index + 1)
            add(index, -1)
            remaining = prefix(n)
            if remaining:
                rank = prefix(index + 1)
                start = kth(rank + 1) if rank < remaining else kth(1)
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.countOperationsToEmptyArray([3, 4, -1]) == 5
    assert solution.countOperationsToEmptyArray([1, 2, 4, 3]) == 5
    assert solution.countOperationsToEmptyArray([1, 2, 3]) == 3
    print("测试用例通过")

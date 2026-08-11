#
# @lc app=leetcode.cn id=2709 lang=python3
# @lcpr version=30203
#
# [2709] 最大公约数遍历
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if 1 in nums:
            return False

        maximum = max(nums)
        smallest_prime = list(range(maximum + 1))
        for value in range(2, int(maximum**0.5) + 1):
            if smallest_prime[value] == value:
                for multiple in range(value * value, maximum + 1, value):
                    if smallest_prime[multiple] == multiple:
                        smallest_prime[multiple] = value

        parent = list(range(len(nums)))

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(left: int, right: int) -> None:
            left, right = find(left), find(right)
            if left != right:
                parent[right] = left

        representative = {}
        for index, number in enumerate(nums):
            while number > 1:
                prime = smallest_prime[number]
                if prime in representative:
                    union(index, representative[prime])
                else:
                    representative[prime] = index
                while number % prime == 0:
                    number //= prime
        root = find(0)
        return all(find(index) == root for index in range(1, len(nums)))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.canTraverseAllPairs([2, 3, 6])
    assert not solution.canTraverseAllPairs([3, 9, 5])
    assert solution.canTraverseAllPairs([4, 3, 12, 8])
    print("测试用例通过")

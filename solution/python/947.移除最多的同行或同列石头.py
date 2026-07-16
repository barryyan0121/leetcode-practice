#
# @lc app=leetcode.cn id=947 lang=python3
#
# [947] 移除最多的同行或同列石头
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = list(range(len(stones)))

        def find(index):
            while index != parent[index]:
                parent[index] = parent[parent[index]]
                index = parent[index]
            return index

        for first in range(len(stones)):
            for second in range(first):
                if (
                    stones[first][0] == stones[second][0]
                    or stones[first][1] == stones[second][1]
                ):
                    parent[find(first)] = find(second)
        return len(stones) - len({find(index) for index in range(len(stones))})


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.removeStones, ([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]],), 5),
        (solution.removeStones, ([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]],), 3),
        (solution.removeStones, ([[0, 0]],), 0),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)

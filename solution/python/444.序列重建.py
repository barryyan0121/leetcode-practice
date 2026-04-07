#
# @lc app=leetcode.cn id=444 lang=python3
# @lcpr version=30203
#
# [444] 序列重建
#

import sys
import os
from collections import deque

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        graph = {num: set() for num in nums}
        indegree = {num: 0 for num in nums}
        seen = set()

        for seq in sequences:
            for num in seq:
                if num not in graph:
                    return False
                seen.add(num)
            for a, b in zip(seq, seq[1:]):
                if b not in graph[a]:
                    graph[a].add(b)
                    indegree[b] += 1

        if seen != set(nums):
            return False

        queue = deque([num for num in nums if indegree[num] == 0])
        order = []
        while queue:
            if len(queue) > 1:
                return False
            node = queue.popleft()
            order.append(node)
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return order == nums


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.sequenceReconstruction, ([1, 2, 3], [[1, 2], [1, 3]]), False),
        (solution.sequenceReconstruction, ([1, 2, 3], [[1, 2], [1, 3], [2, 3]]), True),
        (solution.sequenceReconstruction, ([1], [[1]]), True),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}")

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
# [1,2,3]\n[[1,2],[1,3],[2,3]]\n
# @lcpr case=end

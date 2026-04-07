#
# @lc app=leetcode.cn id=210 lang=python3
# @lcpr version=30202
#
# [210] 课程表 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import deque
from common.node import *


# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1

        queue = deque(i for i in range(numCourses) if indeg[i] == 0)
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    queue.append(nei)
        return order if len(order) == numCourses else []
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def valid_order(
        num_courses: int, prerequisites: List[List[int]], order: List[int]
    ) -> bool:
        if not order and num_courses != 0:
            return len(prerequisites) == 0 and num_courses == 0
        if len(order) != num_courses:
            return False
        pos = {course: i for i, course in enumerate(order)}
        if len(pos) != num_courses:
            return False
        for a, b in prerequisites:
            if pos[b] > pos[a]:
                return False
        return True

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.findOrder, [2, [[1, 0]]], [0, 1]),
        (solution.findOrder, [4, [[1, 0], [2, 0], [3, 1], [3, 2]]], [0, 1, 2, 3]),
        (solution.findOrder, [2, [[1, 0], [0, 1]]], []),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            if expected:
                assert valid_order(args[0], args[1], result)
            else:
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
# 2\n[[1,0]]\n
# @lcpr case=end

#

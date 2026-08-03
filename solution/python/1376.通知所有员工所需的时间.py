# @lc app=leetcode.cn id=1376 lang=python3
from collections import defaultdict
from typing import List


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        children = defaultdict(list)
        for employee, boss in enumerate(manager):
            if boss != -1:
                children[boss].append(employee)

        def dfs(employee: int) -> int:
            return informTime[employee] + max(
                (dfs(child) for child in children[employee]), default=0
            )

        return dfs(headID)


if __name__ == "__main__":
    test_cases = [
        (Solution().numOfMinutes, (1, 0, [-1], [0]), 0),
        (Solution().numOfMinutes, (6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]), 1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1376 题 "通知所有员工所需的时间" 所有测试用例通过')

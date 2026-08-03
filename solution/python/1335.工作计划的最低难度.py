# @lc app=leetcode.cn id=1335 lang=python3

from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        previous = [10**9] * (len(jobDifficulty) + 1)
        previous[0] = 0
        for day in range(d):
            current = [10**9] * (len(jobDifficulty) + 1)
            for end in range(day + 1, len(jobDifficulty) + 1):
                hardest = 0
                for start in range(end - 1, day - 1, -1):
                    hardest = max(hardest, jobDifficulty[start])
                    current[end] = min(current[end], previous[start] + hardest)
            previous = current
        return previous[-1]


if __name__ == "__main__":
    test_cases = [
        (Solution().minDifficulty, ([6, 5, 4, 3, 2, 1], 2), 7),
        (Solution().minDifficulty, ([9, 9, 9], 4), -1),
        (Solution().minDifficulty, ([1, 1, 1], 3), 3),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1335 题 "工作计划的最低难度" 所有测试用例通过')

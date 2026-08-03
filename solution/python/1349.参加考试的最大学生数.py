# @lc app=leetcode.cn id=1349 lang=python3

from functools import lru_cache
from typing import List


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        rows, cols = len(seats), len(seats[0])
        available = [
            sum(1 << column for column, value in enumerate(row) if value == ".")
            for row in seats
        ]

        @lru_cache(None)
        def dp(row: int, previous: int) -> int:
            if row == rows:
                return 0
            best = 0
            mask = available[row]
            subset = mask
            while True:
                if (
                    not (subset & (subset << 1))
                    and not (subset & (previous << 1))
                    and not (subset & (previous >> 1))
                ):
                    best = max(best, subset.bit_count() + dp(row + 1, subset))
                if subset == 0:
                    break
                subset = (subset - 1) & mask
            return best

        return dp(0, 0)


if __name__ == "__main__":
    test_cases = [
        (Solution().maxStudents, (["#.", ".."],), 2),
        (Solution().maxStudents, (["#.##.#", ".####.", "#.#..#"],), 4),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1349 题 "参加考试的最大学生数" 所有测试用例通过')

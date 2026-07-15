#
# @lc app=leetcode.cn id=851 lang=python3
#
# [851] 喧闹和富有
#

import os
import sys
from functools import cache
from typing import List


# @lc code=start
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        richer_people = [[] for _ in quiet]
        for rich, poor in richer:
            richer_people[poor].append(rich)

        @cache
        def quietest(person: int) -> int:
            answer = person
            for richer_person in richer_people[person]:
                candidate = quietest(richer_person)
                if quiet[candidate] < quiet[answer]:
                    answer = candidate
            return answer

        return [quietest(person) for person in range(len(quiet))]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.loudAndRich,
            (
                [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]],
                [3, 2, 5, 4, 6, 1, 7, 0],
            ),
            [5, 5, 2, 5, 4, 5, 6, 7],
        ),
        (solution.loudAndRich, ([], [0]), [0]),
        (solution.loudAndRich, ([[1, 0]], [1, 0]), [1, 1]),
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

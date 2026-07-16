#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        first = second = 0
        result = []
        while first < len(firstList) and second < len(secondList):
            start = max(firstList[first][0], secondList[second][0])
            end = min(firstList[first][1], secondList[second][1])
            if start <= end:
                result.append([start, end])
            if firstList[first][1] < secondList[second][1]:
                first += 1
            else:
                second += 1
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.intervalIntersection,
            (
                [[0, 2], [5, 10], [13, 23], [24, 25]],
                [[1, 5], [8, 12], [15, 24], [25, 26]],
            ),
            [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
        ),
        (solution.intervalIntersection, ([], [[1, 3], [5, 9]]), []),
        (solution.intervalIntersection, ([[1, 7]], [[3, 10]]), [[3, 7]]),
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

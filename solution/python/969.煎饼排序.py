#
# @lc app=leetcode.cn id=969 lang=python3
#
# [969] 煎饼排序
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        for size in range(len(arr), 1, -1):
            largest = arr.index(max(arr[:size]))
            if largest == size - 1:
                continue
            if largest:
                arr[: largest + 1] = reversed(arr[: largest + 1])
                flips.append(largest + 1)
            arr[:size] = reversed(arr[:size])
            flips.append(size)
        return flips


# @lc code=end


def valid(original, flips):
    result = original[:]
    for length in flips:
        result[:length] = reversed(result[:length])
    return result == sorted(original) and len(flips) <= 10 * len(original)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.pancakeSort, ([3, 2, 4, 1],), valid),
        (solution.pancakeSort, ([1, 2, 3],), valid),
        (solution.pancakeSort, ([2, 1],), valid),
    ]
    all_passed = True
    for idx, (func, args, checker) in enumerate(test_cases):
        original = args[0][:]
        result = func(*args)
        expected = checker(original, result)
        try:
            assert expected
            print(f"测试用例 {idx + 1} 通过: n = {original}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {original}, 实际 = {result}")
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)

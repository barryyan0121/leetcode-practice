#
# @lc app=leetcode.cn id=932 lang=python3
#
# [932] 漂亮数组
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        answer = [1]
        while len(answer) < n:
            answer = [2 * value - 1 for value in answer if 2 * value - 1 <= n] + [
                2 * value for value in answer if 2 * value <= n
            ]
        return answer


# @lc code=end


def valid(n, result):
    positions = {value: index for index, value in enumerate(result)}
    return sorted(result) == list(range(1, n + 1)) and all(
        not (positions[left] < positions[middle] < positions[right])
        for left in range(1, n + 1)
        for right in range(left + 2, n + 1, 2)
        for middle in [(left + right) // 2]
    )


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.beautifulArray, (4,), valid),
        (solution.beautifulArray, (5,), valid),
        (solution.beautifulArray, (1,), valid),
    ]
    all_passed = True
    for idx, (func, args, checker) in enumerate(test_cases):
        result = func(*args)
        expected = checker(args[0], result)
        try:
            assert expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 实际 = {result}")
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)

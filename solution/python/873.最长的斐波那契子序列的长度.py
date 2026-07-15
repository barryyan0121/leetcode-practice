#
# @lc app=leetcode.cn id=873 lang=python3
#
# [873] 最长的斐波那契子序列的长度
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        indices = {number: index for index, number in enumerate(arr)}
        lengths = {}
        answer = 0
        for right in range(len(arr)):
            for middle in range(right):
                left = indices.get(arr[right] - arr[middle], -1)
                if 0 <= left < middle:
                    lengths[middle, right] = lengths.get((left, middle), 2) + 1
                    answer = max(answer, lengths[middle, right])
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.lenLongestFibSubseq, ([1, 2, 3, 4, 5, 6, 7, 8],), 5),
        (solution.lenLongestFibSubseq, ([1, 3, 7, 11, 12, 14, 18],), 3),
        (solution.lenLongestFibSubseq, ([1, 4, 10],), 0),
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

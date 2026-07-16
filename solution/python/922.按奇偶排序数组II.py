#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        even, odd = 0, 1
        for number in nums:
            if number % 2:
                answer[odd] = number
                odd += 2
            else:
                answer[even] = number
                even += 2
        return answer


# @lc code=end


def valid(original, result):
    return sorted(original) == sorted(result) and all(
        value % 2 == index % 2 for index, value in enumerate(result)
    )


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.sortArrayByParityII, ([4, 2, 5, 7],), valid),
        (solution.sortArrayByParityII, ([2, 3],), valid),
        (solution.sortArrayByParityII, ([1, 0, 3, 2],), valid),
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

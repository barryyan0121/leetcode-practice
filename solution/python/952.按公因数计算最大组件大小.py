#
# @lc app=leetcode.cn id=952 lang=python3
#
# [952] 按公因数计算最大组件大小
#

import os
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        parent = list(range(len(nums)))

        def find(index):
            while index != parent[index]:
                parent[index] = parent[parent[index]]
                index = parent[index]
            return index

        owners = {}
        for index, number in enumerate(nums):
            factor = 2
            while factor * factor <= number:
                if number % factor:
                    factor += 1
                    continue
                if factor in owners:
                    parent[find(index)] = find(owners[factor])
                else:
                    owners[factor] = index
                while number % factor == 0:
                    number //= factor
            if number > 1:
                if number in owners:
                    parent[find(index)] = find(owners[number])
                else:
                    owners[number] = index
        return max(Counter(find(index) for index in range(len(nums))).values())


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.largestComponentSize, ([4, 6, 15, 35],), 4),
        (solution.largestComponentSize, ([20, 50, 9, 63],), 2),
        (solution.largestComponentSize, ([2, 3, 6, 7, 4, 12, 21, 39],), 8),
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

#
# @lc app=leetcode.cn id=2094 lang=python3
# @lcpr version=30202
#
# [2094] 找出 3 位偶数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []  # 目标偶数数组
        freq = Counter(digits)  # 整数数组中各数字的出现次数
        # 枚举所有三位偶数，维护整数中各数位的出现次数并比较判断是否为目标偶数
        for i in range(100, 1000, 2):
            freq1 = Counter([int(d) for d in str(i)])
            if all(freq[d] >= freq1[d] for d in freq1.keys()):
                res.append(i)
        return res
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.findEvenNumbers,
            [[2, 1, 3, 0]],
            [102, 120, 130, 132, 210, 230, 302, 310, 312, 320],
        ),
        (
            solution.findEvenNumbers,
            [[2, 2, 8, 8, 2]],
            [222, 228, 282, 288, 822, 828, 882],
        ),
        (solution.findEvenNumbers, [[3, 7, 5]], []),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# [2,1,3,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,8,8,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,7,5]\n
# @lcpr case=end

#

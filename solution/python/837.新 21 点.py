#
# @lc app=leetcode.cn id=837 lang=python3
# @lcpr version=30202
#
# [837] 新 21 点
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        probabilities = [1.0] + [0.0] * n
        window = 1.0
        answer = 0.0
        for score in range(1, n + 1):
            probabilities[score] = window / maxPts
            if score < k:
                window += probabilities[score]
            else:
                answer += probabilities[score]
            if 0 <= score - maxPts < k:
                window -= probabilities[score - maxPts]
        return answer if k else 1.0


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.new21Game, (10, 1, 10), 1.0),
        (solution.new21Game, (6, 1, 10), 0.6),
        (solution.new21Game, (21, 17, 10), 0.73278),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            # 四舍五入到小数点后 5 位
            result = round(result, 5)
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
# 10\n1\n10\n
# @lcpr case=end

# @lcpr case=start
# 6\n1\n10\n
# @lcpr case=end

# @lcpr case=start
# 21\n17\n10\n
# @lcpr case=end

#

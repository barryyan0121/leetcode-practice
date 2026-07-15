#
# @lc app=leetcode.cn id=793 lang=python3
#
# [793] 阶乘函数后 K 个零
#

import os
import sys


# @lc code=start
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def zeroes(number: int) -> int:
            answer = 0
            while number:
                number //= 5
                answer += number
            return answer

        left, right = 0, 5 * k + 5
        while left < right:
            middle = (left + right) // 2
            if zeroes(middle) < k:
                left = middle + 1
            else:
                right = middle
        return 5 if zeroes(left) == k else 0


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.preimageSizeFZF, (0,), 5),
        (solution.preimageSizeFZF, (3,), 5),
        (solution.preimageSizeFZF, (5,), 0),
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

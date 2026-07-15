#
# @lc app=leetcode.cn id=866 lang=python3
#
# [866] 回文质数
#

import os
import sys
from math import isqrt


# @lc code=start
class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(number: int) -> bool:
            if number < 2 or number % 2 == 0:
                return number == 2
            return all(number % divisor for divisor in range(3, isqrt(number) + 1, 2))

        if 8 <= n <= 11:
            return 11
        for root in range(1, 100000):
            text = str(root)
            palindrome = int(text + text[-2::-1])
            if palindrome >= n and is_prime(palindrome):
                return palindrome
        return -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.primePalindrome, (6,), 7),
        (solution.primePalindrome, (8,), 11),
        (solution.primePalindrome, (13,), 101),
        (solution.primePalindrome, (1,), 2),
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

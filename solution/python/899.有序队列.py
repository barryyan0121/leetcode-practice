#
# @lc app=leetcode.cn id=899 lang=python3
#
# [899] 有序队列
#

import os
import sys


# @lc code=start
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(s))
        return min(s[index:] + s[:index] for index in range(len(s)))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.orderlyQueue, ("cba", 1), "acb"),
        (solution.orderlyQueue, ("baaca", 3), "aaabc"),
        (solution.orderlyQueue, ("a", 1), "a"),
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

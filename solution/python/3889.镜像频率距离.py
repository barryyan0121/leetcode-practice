#
# @lc app=leetcode.cn id=3889 lang=python3
#
# [3889] 镜像频率距离
#

import os
import sys
from collections import Counter


# @lc code=start
class Solution:
    def mirrorFrequency(self, s: str) -> int:
        counts = Counter(s)
        answer = 0

        for char in counts:
            if "a" <= char <= "z":
                mirror = chr(ord("z") - (ord(char) - ord("a")))
            else:
                mirror = chr(ord("9") - (ord(char) - ord("0")))

            if char <= mirror:
                answer += abs(counts[char] - counts.get(mirror, 0))

        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.mirrorFrequency, ("ab1z9",), 2),
        (solution.mirrorFrequency, ("aaazz9",), 1),
        (solution.mirrorFrequency, ("0123456789",), 0),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: args = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: args = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)

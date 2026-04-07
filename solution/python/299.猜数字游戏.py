#
# @lc app=leetcode.cn id=299 lang=python3
# @lcpr version=30203
#
# [299] 猜数字游戏
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        s_cnt = [0] * 10
        g_cnt = [0] * 10
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                s_cnt[ord(s) - 48] += 1
                g_cnt[ord(g) - 48] += 1
        cows = sum(min(s_cnt[i], g_cnt[i]) for i in range(10))
        return f"{bulls}A{cows}B"


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.getHint, ["1807", "7810"], "1A3B"),
        (solution.getHint, ["1123", "0111"], "1A1B"),
        (solution.getHint, ["1", "0"], "0A0B"),
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
# "1807"\n"7810"\n
# @lcpr case=end

#

#
# @lc app=leetcode.cn id=3335 lang=python3
# @lcpr version=30202
#
# [3335] 字符串转换后的长度 I
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        # 初始化字符计数数组
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1

        # 进行 t 次转换
        for _ in range(t):
            nxt = [0] * 26
            nxt[0] = cnt[25]  # 更新 cnt[0]
            nxt[1] = (cnt[25] + cnt[0]) % mod  # 更新 cnt[1]
            for i in range(2, 26):  # 更新 cnt[2] 到 cnt[25]
                nxt[i] = cnt[i - 1]
            cnt = nxt  # 更新 cnt 为当前轮次的结果

        # 返回所有字符计数的总和模 mod
        return sum(cnt) % mod
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.lengthAfterTransformations, ("abcyy", 2), 7),
        (solution.lengthAfterTransformations, ("azbk", 1), 5),
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
# "abcyy"\n2\n
# @lcpr case=end

# @lcpr case=start
# "azbk"\n1\n
# @lcpr case=end

#

#
# @lc app=leetcode.cn id=93 lang=python3
# @lcpr version=30202
#
# [93] 复原 IP 地址
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        TOTAL_SEGMENTS = 4
        segments = [0] * TOTAL_SEGMENTS

        def dfs(seg_idx: int, curr_idx: int) -> None:
            # 如果已经遍历完四个字段
            if seg_idx == TOTAL_SEGMENTS:
                if curr_idx == len(s):
                    res.append(".".join(str(seg) for seg in segments))
                return

            # 如果剩余字符数和剩余字段数不匹配
            remain_chars = len(s) - curr_idx
            remain_segs = TOTAL_SEGMENTS - seg_idx
            # 同时处理剩余字符过多和过少的情况
            # 例如：剩余3字符但需分4段（不可能），
            # 或剩余10字符但只需分2段（最多6字符）
            if remain_chars > remain_segs * 3 or remain_chars < remain_segs:
                return

            # 如果当前字符是0，直接处理为0，前导零的情况
            if s[curr_idx] == "0":
                segments[seg_idx] = 0
                dfs(seg_idx + 1, curr_idx + 1)
                return

            # 计算当前段最多取几位（最多3位）
            max_len = min(3, remain_chars)
            address = 0
            for i in range(curr_idx, curr_idx + max_len):
                address = address * 10 + ord(s[i]) - ord("0")
                if address > 255:
                    break
                segments[seg_idx] = address
                dfs(seg_idx + 1, i + 1)

        dfs(0, 0)
        return res
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.restoreIpAddresses,
            ["25525511135"],
            ["255.255.11.135", "255.255.111.35"],
        ),
        (solution.restoreIpAddresses, ["0000"], ["0.0.0.0"]),
        (solution.restoreIpAddresses, ["1111"], ["1.1.1.1"]),
        (solution.restoreIpAddresses, ["010010"], ["0.10.0.10", "0.100.1.0"]),
        (
            solution.restoreIpAddresses,
            ["10203040"],
            ["10.20.30.40", "10.203.0.40", "102.0.30.40"],
        ),
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
# "25525511135"\n
# @lcpr case=end

# @lcpr case=start
# "0000"\n
# @lcpr case=end

# @lcpr case=start
# "101023"\n
# @lcpr case=end

#

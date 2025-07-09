#
# @lc app=leetcode.cn id=LCR 087 lang=python3
# @lcpr version=30201
#
# [LCR 087] 复原 IP 地址
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
    res = solution.restoreIpAddresses("25525511135")
    print(res)
    # your test code here


#
# @lcpr case=start
# "25525511135"\n
# @lcpr case=end

# @lcpr case=start
# "0000"\n
# @lcpr case=end

# @lcpr case=start
# "1111"\n
# @lcpr case=end

# @lcpr case=start
# "010010"\n
# @lcpr case=end

# @lcpr case=start
# "10203040"\n
# @lcpr case=end

#

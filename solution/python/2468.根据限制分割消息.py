#
# @lc app=leetcode.cn id=2468 lang=python3
# @lcpr version=30203
#
# [2468] 根据限制分割消息
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        length = len(message)
        digit_sum = 0
        for total in range(1, length + 1):
            digits = len(str(total))
            digit_sum += digits
            if limit <= digits + 4:
                break
            capacity = total * (limit - digits - 3) - digit_sum
            if capacity < length:
                continue

            parts = []
            offset = 0
            for index in range(1, total + 1):
                suffix = f"<{index}/{total}>"
                take = limit - len(suffix) if index < total else length - offset
                if take < 0 or take > length - offset:
                    break
                parts.append(message[offset : offset + take] + suffix)
                offset += take
            if len(parts) == total and offset == length:
                return parts
        return []


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.splitMessage("this is really a very awesome message", 9) == [
        "thi<1/14>",
        "s i<2/14>",
        "s r<3/14>",
        "eal<4/14>",
        "ly <5/14>",
        "a v<6/14>",
        "ery<7/14>",
        " aw<8/14>",
        "eso<9/14>",
        "me<10/14>",
        " m<11/14>",
        "es<12/14>",
        "sa<13/14>",
        "ge<14/14>",
    ]
    assert solution.splitMessage("short message", 15) == ["short mess<1/2>", "age<2/2>"]
    print("测试用例通过")

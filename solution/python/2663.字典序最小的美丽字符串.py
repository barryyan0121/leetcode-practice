#
# @lc app=leetcode.cn id=2663 lang=python3
# @lcpr version=30203
#
# [2663] 字典序最小的美丽字符串
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        result = list(s)
        for index in range(len(result) - 1, -1, -1):
            for code in range(ord(result[index]) + 1, ord("a") + k):
                if index >= 1 and code == ord(result[index - 1]):
                    continue
                if index >= 2 and code == ord(result[index - 2]):
                    continue
                result[index] = chr(code)
                for next_index in range(index + 1, len(result)):
                    for next_code in range(ord("a"), ord("a") + k):
                        if next_index >= 1 and next_code == ord(result[next_index - 1]):
                            continue
                        if next_index >= 2 and next_code == ord(result[next_index - 2]):
                            continue
                        result[next_index] = chr(next_code)
                        break
                return "".join(result)
        return ""


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.smallestBeautifulString("abcz", 26) == "abda"
    assert solution.smallestBeautifulString("dc", 4) == ""
    print("测试用例通过")

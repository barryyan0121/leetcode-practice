#
# @lc app=leetcode.cn id=468 lang=python3
# @lcpr version=30203
#
# [468] 验证IP地址
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_ipv4(part: str) -> bool:
            if not part or (part[0] == "0" and len(part) > 1):
                return False
            if not part.isdigit():
                return False
            if int(part) > 255:
                return False
            return True

        def is_ipv6(part: str) -> bool:
            if not 1 <= len(part) <= 4:
                return False
            for ch in part:
                if ch not in "0123456789abcdefABCDEF":
                    return False
            return True

        if "." in queryIP:
            parts = queryIP.split(".")
            if len(parts) == 4 and all(is_ipv4(p) for p in parts):
                return "IPv4"
            return "Neither"
        if ":" in queryIP:
            parts = queryIP.split(":")
            if len(parts) == 8 and all(is_ipv6(p) for p in parts):
                return "IPv6"
            return "Neither"
        return "Neither"
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.validIPAddress, ["172.16.254.1"], "IPv4"),
        (solution.validIPAddress, ["2001:0db8:85a3:0:0:8A2E:0370:7334"], "IPv6"),
        (solution.validIPAddress, ["256.256.256.256"], "Neither"),
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
# "172.16.254.1"\n
# @lcpr case=end

#

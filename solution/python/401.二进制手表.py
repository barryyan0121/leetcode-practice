#
# @lc app=leetcode.cn id=401 lang=python3
# @lcpr version=30203
#
# [401] 二进制手表
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):
            for m in range(60):
                if h.bit_count() + m.bit_count() == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.readBinaryWatch,
            [1],
            [
                "0:01",
                "0:02",
                "0:04",
                "0:08",
                "0:16",
                "0:32",
                "1:00",
                "2:00",
                "4:00",
                "8:00",
            ],
        ),
        (solution.readBinaryWatch, [0], ["0:00"]),
        (
            solution.readBinaryWatch,
            [2],
            [
                "0:03",
                "0:05",
                "0:06",
                "0:09",
                "0:10",
                "0:12",
                "0:17",
                "0:18",
                "0:20",
                "0:24",
                "0:33",
                "0:34",
                "0:36",
                "0:40",
                "0:48",
                "1:01",
                "1:02",
                "1:04",
                "1:08",
                "1:16",
                "1:32",
                "2:01",
                "2:02",
                "2:04",
                "2:08",
                "2:16",
                "2:32",
                "3:00",
                "4:01",
                "4:02",
                "4:04",
                "4:08",
                "4:16",
                "4:32",
                "5:00",
                "6:00",
                "8:01",
                "8:02",
                "8:04",
                "8:08",
                "8:16",
                "8:32",
                "9:00",
                "10:00",
            ],
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
# 1\n
# @lcpr case=end

#

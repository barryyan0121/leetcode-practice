#
# @lc app=leetcode.cn id=388 lang=python3
# @lcpr version=30203
#
# [388] 文件的最长绝对路径
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        depth_length = {0: 0}
        longest = 0

        for part in input.split("\n"):
            name = part.lstrip("\t")
            depth = len(part) - len(name)
            if "." in name:
                longest = max(longest, depth_length[depth] + len(name))
            else:
                depth_length[depth + 1] = depth_length[depth] + len(name) + 1

        return longest


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.lengthLongestPath, ("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext",), 20),
        (
            solution.lengthLongestPath,
            ("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",),
            32,
        ),
        (solution.lengthLongestPath, ("a",), 0),
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
# "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"\n
# @lcpr case=end

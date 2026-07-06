#
# @lc app=leetcode.cn id=609 lang=python3
# @lcpr version=30203
#
# [609] 在系统中查找重复文件
#

import sys
import os
from collections import defaultdict

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files_by_content = defaultdict(list)
        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file_info in parts[1:]:
                name, content = file_info.split("(", 1)
                files_by_content[content[:-1]].append(f"{directory}/{name}")
        return [files for files in files_by_content.values() if len(files) > 1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def normalize(groups: List[List[str]]) -> List[List[str]]:
        return sorted(sorted(group) for group in groups)

    test_cases = [
        (
            solution.findDuplicate,
            (
                [
                    "root/a 1.txt(abcd) 2.txt(efgh)",
                    "root/c 3.txt(abcd)",
                    "root/c/d 4.txt(efgh)",
                    "root 4.txt(efgh)",
                ],
            ),
            [
                ["root/a/1.txt", "root/c/3.txt"],
                ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"],
            ],
        ),
        (solution.findDuplicate, (["root/a 1.txt(abcd)"],), []),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert normalize(result) == normalize(expected)
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
# ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]\n
# @lcpr case=end

#

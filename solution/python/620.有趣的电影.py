#
# @lc app=leetcode.cn id=620 lang=python3
# @lcpr version=30203
#
# [620] 有趣的电影
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def notBoringMovies(self, cinema: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return sorted(
            [row for row in cinema if row["id"] % 2 == 1 and row["description"] != "boring"],
            key=lambda row: row["rating"],
            reverse=True,
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.notBoringMovies,
            (
                [
                    {"id": 1, "movie": "War", "description": "great 3D", "rating": 8.9},
                    {"id": 2, "movie": "Science", "description": "fiction", "rating": 8.5},
                    {"id": 3, "movie": "Irish", "description": "boring", "rating": 6.2},
                    {"id": 4, "movie": "Ice song", "description": "Fantasy", "rating": 8.6},
                    {"id": 5, "movie": "House card", "description": "Interesting", "rating": 9.1},
                ],
            ),
            [
                {"id": 5, "movie": "House card", "description": "Interesting", "rating": 9.1},
                {"id": 1, "movie": "War", "description": "great 3D", "rating": 8.9},
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
            print(f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}")

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


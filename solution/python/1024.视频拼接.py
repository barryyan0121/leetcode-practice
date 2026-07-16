#
# @lc app=leetcode.cn id=1024 lang=python3
#
# [1024] 视频拼接
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        index = used = current = farthest = 0
        while current < time:
            while index < len(clips) and clips[index][0] <= current:
                farthest = max(farthest, clips[index][1])
                index += 1
            if farthest == current:
                return -1
            used += 1
            current = farthest
        return used


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.videoStitching,
            ([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10),
            3,
        ),
        (solution.videoStitching, ([[0, 1], [1, 2]], 5), -1),
        (solution.videoStitching, ([[0, 4], [2, 8]], 5), 2),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)

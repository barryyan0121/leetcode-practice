#
# @lc app=leetcode.cn id=920 lang=python3
#
# [920] 播放列表的数量
#

import os
import sys


# @lc code=start
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        modulo = 10**9 + 7
        ways = [[0] * (n + 1) for _ in range(goal + 1)]
        ways[0][0] = 1
        for length in range(1, goal + 1):
            for used in range(1, min(length, n) + 1):
                ways[length][used] = (
                    ways[length - 1][used - 1] * (n - used + 1)
                    + ways[length - 1][used] * max(used - k, 0)
                ) % modulo
        return ways[goal][n]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numMusicPlaylists, (3, 3, 1), 6),
        (solution.numMusicPlaylists, (2, 3, 0), 6),
        (solution.numMusicPlaylists, (2, 3, 1), 2),
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

#
# @lc app=leetcode.cn id=1733 lang=python3
# @lcpr version=30203
#
# [1733] 需要教语言的最少人数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        cncon = set()
        for friendship in friendships:
            mp = {}
            conm = False
            for lan in languages[friendship[0] - 1]:
                mp[lan] = 1
            for lan in languages[friendship[1] - 1]:
                if lan in mp:
                    conm = True
                    break
            if not conm:
                cncon.add(friendship[0] - 1)
                cncon.add(friendship[1] - 1)

        max_cnt = 0
        cnt = [0] * (n + 1)
        for friendship in cncon:
            for lan in languages[friendship]:
                cnt[lan] += 1
                max_cnt = max(max_cnt, cnt[lan])

        return len(cncon) - max_cnt


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.minimumTeachings,
            (2, [[1], [2], [1, 2]], [[1, 2], [1, 3], [2, 3]]),
            1,
        ),
        (
            solution.minimumTeachings,
            (3, [[2], [1, 3], [1, 2], [3]], [[1, 4], [1, 2], [3, 4], [2, 3]]),
            2,
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
# 2\n[[1],[2],[1,2]]\n[[1,2],[1,3],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[2],[1,3],[1,2],[3]]\n[[1,4],[1,2],[3,4],[2,3]]\n
# @lcpr case=end

#

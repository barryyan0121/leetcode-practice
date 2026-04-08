#
# @lc app=leetcode.cn id=574 lang=python3
# @lcpr version=30203
#
# [574] 当选者
#

import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def winningCandidate(
        self, candidate: List[Dict[str, Any]], vote: List[Dict[str, int]]
    ) -> str:
        name_by_id = {row["id"]: row["name"] for row in candidate}
        vote_count = Counter(row["candidateId"] for row in vote)
        if not name_by_id:
            return ""
        winner_id = max(
            name_by_id,
            key=lambda candidate_id: (vote_count[candidate_id], -candidate_id),
        )
        return name_by_id[winner_id]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.winningCandidate,
            (
                [
                    {"id": 1, "name": "Alice"},
                    {"id": 2, "name": "Bob"},
                    {"id": 3, "name": "Cindy"},
                ],
                [
                    {"candidateId": 1},
                    {"candidateId": 1},
                    {"candidateId": 2},
                    {"candidateId": 3},
                    {"candidateId": 3},
                    {"candidateId": 3},
                ],
            ),
            "Cindy",
        ),
        (
            solution.winningCandidate,
            (
                [
                    {"id": 1, "name": "Alice"},
                    {"id": 2, "name": "Bob"},
                ],
                [
                    {"candidateId": 1},
                    {"candidateId": 2},
                ],
            ),
            "Alice",
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
# candidate = Candidate table, vote = Vote table\n
# @lcpr case=end

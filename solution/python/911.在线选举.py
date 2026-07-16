#
# @lc app=leetcode.cn id=911 lang=python3
#
# [911] 在线选举
#

import os
import sys
from bisect import bisect_right
from typing import List


# @lc code=start
class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        counts = {}
        leader = -1
        self.times = times
        self.leaders = []
        for person in persons:
            counts[person] = counts.get(person, 0) + 1
            if leader == -1 or counts[person] >= counts[leader]:
                leader = person
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        return self.leaders[bisect_right(self.times, t) - 1]


# @lc code=end


def run_operations(persons, times, queries):
    election = TopVotedCandidate(persons, times)
    return [election.q(query) for query in queries]


if __name__ == "__main__":
    test_cases = [
        (
            run_operations,
            ([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30], [3, 12, 25, 15, 24, 8]),
            [0, 1, 1, 0, 0, 1],
        ),
        (run_operations, ([1, 2, 2], [5, 10, 15], [5, 10, 15]), [1, 2, 2]),
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

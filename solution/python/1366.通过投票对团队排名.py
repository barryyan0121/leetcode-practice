# @lc app=leetcode.cn id=1366 lang=python3

from collections import defaultdict
from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if not votes:
            return ""
        teams = votes[0]
        counts = defaultdict(lambda: [0] * len(teams))
        for vote in votes:
            for position, team in enumerate(vote):
                counts[team][position] += 1
        return "".join(
            sorted(
                teams, key=lambda team: (tuple(-value for value in counts[team]), team)
            )
        )


if __name__ == "__main__":
    test_cases = [
        (Solution().rankTeams, (["ABC", "ACB", "ABC", "ACB", "ACB"],), "ACB"),
        (Solution().rankTeams, (["WXYZ", "XYZW"],), "XWYZ"),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1366 题 "通过投票对团队排名" 所有测试用例通过')

"""3238. 获胜玩家数目"""

from collections import defaultdict


class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:
        counts = defaultdict(int)
        winners = set()
        for player, color in pick:
            counts[(player, color)] += 1
            if counts[(player, color)] > player:
                winners.add(player)
        return len(winners)


if __name__ == "__main__":
    test_cases = [
        ((4, [[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 1]]), 3),
        ((5, [[1, 1], [1, 1], [2, 2], [2, 2], [2, 2]]), 2),
    ]
    for index, (args, expected) in enumerate(test_cases):
        assert Solution().winningPlayerCount(*args) == expected, index

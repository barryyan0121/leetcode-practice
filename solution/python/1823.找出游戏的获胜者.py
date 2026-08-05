"""1823. 找出游戏的获胜者"""


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0
        for size in range(2, n + 1):
            winner = (winner + k) % size
        return winner + 1


if __name__ == "__main__":
    test_cases = [((5, 2), 3), ((6, 5), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findTheWinner(*args) == expected

"""3996. Even Number of Knight Moves"""


class Solution:
    def checkTwoChessboards(self, start: list[int], target: list[int]) -> bool:
        return (start[0] + start[1]) % 2 == (target[0] + target[1]) % 2


if __name__ == "__main__":
    test_cases = [
        (([1, 1], [2, 2]), True),
        (([4, 5], [6, 6]), False),
        (([0, 0], [0, 0]), True),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().checkTwoChessboards(*args) == expected

from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        return max(
            Counter(tuple(value ^ row[0] for value in row) for row in matrix).values()
        )


if __name__ == "__main__":
    test_cases = [
        ([[0, 1], [1, 1]], 1),
        ([[0, 1], [1, 1], [1, 0]], 2),
        ([[0, 0, 0], [0, 0, 1], [1, 1, 0]], 2),
    ]
    for _, (matrix, expected) in enumerate(test_cases):
        assert Solution().maxEqualRowsAfterFlips(matrix) == expected

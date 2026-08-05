"""1975. 最大方阵和"""


class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total = sum(abs(value) for row in matrix for value in row)
        minimum = min(abs(value) for row in matrix for value in row)
        negatives = sum(value < 0 for row in matrix for value in row)
        return total if negatives % 2 == 0 else total - 2 * minimum


if __name__ == "__main__":
    test_cases = [
        (([[1, -1], [-1, 1]],), 4),
        (([[1, 2, 3], [-1, -2, -3], [1, 2, 3]],), 16),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxMatrixSum(*args) == expected

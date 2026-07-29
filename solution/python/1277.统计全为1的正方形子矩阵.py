from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col]:
                    matrix[row][col] += min(
                        matrix[row - 1][col],
                        matrix[row][col - 1],
                        matrix[row - 1][col - 1],
                    )
        return sum(map(sum, matrix))


if __name__ == "__main__":
    test_cases = [
        ([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]], 15),
        ([[1, 0, 1], [1, 1, 0], [1, 1, 0]], 7),
    ]
    for _, (matrix, expected) in enumerate(test_cases):
        assert Solution().countSquares(matrix) == expected

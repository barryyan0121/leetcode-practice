"""2133. 检查是否每一行每一列都包含全部整数"""


class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        target = set(range(1, len(matrix) + 1))
        return all(set(row) == target for row in matrix) and all(
            {matrix[row][col] for row in range(len(matrix))} == target
            for col in range(len(matrix))
        )


if __name__ == "__main__":
    test_cases = [(([[1, 2, 3], [3, 1, 2], [2, 3, 1]],), True)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().checkValid(*args) == expected

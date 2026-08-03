class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        column_maximums = [
            max(matrix[row][column] for row in range(len(matrix)))
            for column in range(len(matrix[0]))
        ]
        for row in matrix:
            for column, value in enumerate(row):
                if value == -1:
                    row[column] = column_maximums[column]
        return matrix


if __name__ == "__main__":
    test_cases = [
        (([[1, 2, -1], [4, -1, 6]],), [[1, 2, 6], [4, 2, 6]]),
    ]
    for _, ((matrix,), expected) in enumerate(test_cases):
        assert Solution().modifiedMatrix(matrix) == expected

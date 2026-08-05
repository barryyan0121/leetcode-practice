"""2536. 子矩阵元素加 1"""


class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        difference = [[0] * (n + 1) for _ in range(n + 1)]
        for row1, column1, row2, column2 in queries:
            difference[row1][column1] += 1
            difference[row2 + 1][column1] -= 1
            difference[row1][column2 + 1] -= 1
            difference[row2 + 1][column2 + 1] += 1
        answer = [[0] * n for _ in range(n)]
        for row in range(n):
            for column in range(n):
                if row:
                    difference[row][column] += difference[row - 1][column]
                if column:
                    difference[row][column] += difference[row][column - 1]
                if row and column:
                    difference[row][column] -= difference[row - 1][column - 1]
                answer[row][column] = difference[row][column]
        return answer


if __name__ == "__main__":
    test_cases = [
        ((3, [[1, 1, 2, 2], [0, 0, 1, 1]]), [[1, 1, 0], [1, 2, 1], [0, 1, 1]])
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().rangeAddQueries(*args) == expected

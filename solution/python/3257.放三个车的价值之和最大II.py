class Solution:
    def maximumValueSum(self, board: list[list[int]]) -> int:
        rows, columns = len(board), len(board[0])
        row_candidates = [
            sorted(((value, column) for column, value in enumerate(row)), reverse=True)[
                :3
            ]
            for row in board
        ]

        suffix = [[] for _ in range(rows + 1)]
        best_by_column = [-(10**18)] * columns
        for row in range(rows - 1, -1, -1):
            for column, value in enumerate(board[row]):
                best_by_column[column] = max(best_by_column[column], value)
            suffix[row] = sorted(
                ((value, column) for column, value in enumerate(best_by_column)),
                reverse=True,
            )[:3]

        answer = -(10**18)
        for first in range(rows - 2):
            for second in range(first + 1, rows - 1):
                for value1, column1 in row_candidates[first]:
                    for value2, column2 in row_candidates[second]:
                        if column1 == column2:
                            continue
                        for value3, column3 in suffix[second + 1]:
                            if column3 != column1 and column3 != column2:
                                answer = max(answer, value1 + value2 + value3)
                                break
        return answer


if __name__ == "__main__":
    test_cases = [
        ([[-3, 1, 1, 1], [-3, 1, -3, 1], [-3, 2, 1, 1]], 4),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 15),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 3),
    ]
    for _, (board, expected) in enumerate(test_cases):
        assert Solution().maximumValueSum(board) == expected

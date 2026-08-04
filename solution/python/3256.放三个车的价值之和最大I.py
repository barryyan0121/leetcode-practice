class Solution:
    def maximumValueSum(self, board: list[list[int]]) -> int:
        candidates = [
            sorted(((value, column) for column, value in enumerate(row)), reverse=True)[
                :3
            ]
            for row in board
        ]
        answer = -(10**18)
        for first in range(len(board) - 2):
            for second in range(first + 1, len(board) - 1):
                for third in range(second + 1, len(board)):
                    for value1, column1 in candidates[first]:
                        for value2, column2 in candidates[second]:
                            if column2 == column1:
                                continue
                            for value3, column3 in candidates[third]:
                                if column3 != column1 and column3 != column2:
                                    answer = max(answer, value1 + value2 + value3)
        return answer


if __name__ == "__main__":
    test_cases = [
        ([[-3, 1, 1, 1], [-3, 1, -3, 1], [-3, 2, 1, 1]], 4),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 15),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 3),
    ]
    for _, (board, expected) in enumerate(test_cases):
        assert Solution().maximumValueSum(board) == expected

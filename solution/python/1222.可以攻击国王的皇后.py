from typing import List


class Solution:
    def queensAttacktheKing(
        self, queens: List[List[int]], king: List[int]
    ) -> List[List[int]]:
        locations = {tuple(queen) for queen in queens}
        answer = []
        for row_step, col_step in (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ):
            row, col = king
            while 0 <= row + row_step < 8 and 0 <= col + col_step < 8:
                row += row_step
                col += col_step
                if (row, col) in locations:
                    answer.append([row, col])
                    break
        return answer


if __name__ == "__main__":
    test_cases = [
        (
            [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]],
            [0, 0],
            [[0, 1], [1, 0], [3, 3]],
        )
    ]
    for _, (queens, king, expected) in enumerate(test_cases):
        assert Solution().queensAttacktheKing(queens, king) == expected

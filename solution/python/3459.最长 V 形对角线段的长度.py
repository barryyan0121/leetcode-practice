from functools import lru_cache


class Solution:
    def lenOfVDiagonal(self, grid: list[list[int]]) -> int:
        draxemilon = grid
        rows, columns = len(grid), len(grid[0])
        directions = ((1, 1), (1, -1), (-1, -1), (-1, 1))

        @lru_cache(None)
        def walk(row, column, direction, turned, expected):
            if not (0 <= row < rows and 0 <= column < columns):
                return 0
            if grid[row][column] != expected:
                return 0
            next_expected = 2 if expected == 0 else 0
            dr, dc = directions[direction]
            best = walk(row + dr, column + dc, direction, turned, next_expected)
            if not turned:
                turn = (direction + 1) % 4
                dr, dc = directions[turn]
                best = max(
                    best,
                    walk(row + dr, column + dc, turn, 1, next_expected),
                )
            return best + 1

        answer = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] != 1:
                    continue
                for direction, (dr, dc) in enumerate(directions):
                    answer = max(
                        answer,
                        1 + walk(row + dr, column + dc, direction, 0, 2),
                    )
        return answer


if __name__ == "__main__":
    test_cases = [
        (([[1]],), 1),
        (([[1, 2], [0, 2]],), 2),
        (([[0, 1, 2], [0, 0, 2]],), 2),
    ]
    for _, ((grid,), expected) in enumerate(test_cases):
        assert Solution().lenOfVDiagonal(grid) == expected

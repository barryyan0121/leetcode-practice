class Solution:
    def minFlips(self, grid: list[list[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        answer = 0
        for row in range(rows // 2):
            for column in range(columns // 2):
                ones = (
                    grid[row][column]
                    + grid[row][columns - 1 - column]
                    + grid[rows - 1 - row][column]
                    + grid[rows - 1 - row][columns - 1 - column]
                )
                answer += min(ones, 4 - ones)

        mismatches = 0
        fixed_ones = 0
        if rows % 2:
            row = rows // 2
            for column in range(columns // 2):
                left, right = grid[row][column], grid[row][columns - 1 - column]
                if left != right:
                    answer += 1
                    mismatches += 1
                else:
                    fixed_ones += 2 * left
        if columns % 2:
            column = columns // 2
            for row in range(rows // 2):
                top, bottom = grid[row][column], grid[rows - 1 - row][column]
                if top != bottom:
                    answer += 1
                    mismatches += 1
                else:
                    fixed_ones += 2 * top

        if mismatches == 0:
            answer += (fixed_ones % 4 == 2) * 2
        if rows % 2 and columns % 2:
            answer += grid[rows // 2][columns // 2]
        return answer


if __name__ == "__main__":
    test_cases = [
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
        ([[0, 1], [0, 1], [0, 0]], 2),
        ([[1], [1]], 2),
    ]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().minFlips(grid) == expected

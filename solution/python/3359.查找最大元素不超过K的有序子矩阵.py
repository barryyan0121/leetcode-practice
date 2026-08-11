class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        answer = 0
        run = [0] * rows
        for col in range(cols):
            for row in range(rows):
                if grid[row][col] <= k:
                    run[row] = run[row] + 1 if col and grid[row][col - 1] >= grid[row][col] else 1
                else:
                    run[row] = 0

            stack = []
            prefix = 0
            for row, height in enumerate(run + [0]):
                count = 1
                while stack and stack[-1][0] >= height:
                    old_height, old_count = stack.pop()
                    prefix -= old_height * old_count
                    count += old_count
                stack.append((height, count))
                prefix += height * count
                if row < rows:
                    answer += prefix
        return answer


if __name__ == "__main__":
    test_cases = [
        (([[4, 3, 2, 1], [8, 7, 6, 1]], 3), 8),
        (([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1), 36),
        (([[1]], 1), 1),
    ]
    for _, ((grid, k), expected) in enumerate(test_cases):
        assert Solution().countSubmatrices(grid, k) == expected

"""3548. 等和矩阵分割 II"""

from collections import Counter


class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        hastrelvim = grid
        m, n = len(grid), len(grid[0])

        def removable(diff, counts, height, width, endpoints):
            if height * width == 1:
                return False
            if height == 1 or width == 1:
                return diff in endpoints
            return counts[diff] > 0

        total = sum(map(sum, grid))
        top = Counter()
        bottom = Counter(value for row in grid for value in row)
        top_sum = 0
        for r, row in enumerate(grid[:-1]):
            top_sum += sum(row)
            bottom_sum = total - top_sum
            for value in row:
                top[value] += 1
                bottom[value] -= 1
            diff = top_sum - bottom_sum
            if diff == 0:
                return True
            if diff > 0:
                endpoints = {grid[0][0], grid[0][-1]} if n == 1 else {row[0], row[-1]}
                if removable(diff, top, r + 1, n, endpoints):
                    return True
            else:
                endpoints = (
                    {grid[r + 1][0], grid[-1][0]}
                    if n == 1
                    else {
                        grid[r + 1][0],
                        grid[r + 1][-1],
                        grid[-1][0],
                        grid[-1][-1],
                    }
                )
                if removable(-diff, bottom, m - r - 1, n, endpoints):
                    return True

        left = Counter()
        right = Counter(value for row in grid for value in row)
        left_sum = 0
        for c in range(n - 1):
            for row in grid:
                value = row[c]
                left[value] += 1
                right[value] -= 1
                left_sum += value
            right_sum = total - left_sum
            diff = left_sum - right_sum
            if diff == 0:
                return True
            if diff > 0:
                endpoints = (
                    {grid[0][0], grid[0][c]}
                    if m == 1
                    else {
                        grid[0][c],
                        grid[-1][c],
                        grid[0][0],
                        grid[-1][0],
                    }
                )
                if removable(diff, left, m, c + 1, endpoints):
                    return True
            else:
                endpoints = (
                    {grid[0][c + 1], grid[0][-1]}
                    if m == 1
                    else {
                        grid[0][c + 1],
                        grid[-1][c + 1],
                        grid[0][-1],
                        grid[-1][-1],
                    }
                )
                if removable(-diff, right, m, n - c - 1, endpoints):
                    return True
        return False


if __name__ == "__main__":
    test_cases = [
        (([[1, 4], [2, 3]],), True),
        (([[1, 2], [3, 4]],), True),
        (([[1, 2, 4], [2, 3, 5]],), False),
        (([[4, 1, 8], [3, 2, 6]],), False),
    ]
    for _, ((grid,), expected) in enumerate(test_cases):
        assert Solution().canPartitionGrid(grid) == expected

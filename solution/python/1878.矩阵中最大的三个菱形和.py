from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        values = set()
        for row in range(rows):
            for col in range(cols):
                values.add(grid[row][col])
                radius = 1
                while (
                    row + 2 * radius < rows
                    and col - radius >= 0
                    and col + radius < cols
                ):
                    total = grid[row][col] + grid[row + 2 * radius][col]
                    for offset in range(1, radius + 1):
                        total += grid[row + offset][col - offset]
                        total += grid[row + offset][col + offset]
                    for offset in range(1, radius):
                        total += grid[row + radius + offset][col - radius + offset]
                        total += grid[row + radius + offset][col + radius - offset]
                    values.add(total)
                    radius += 1
        return sorted(values, reverse=True)[:3]

if __name__ == "__main__":
    assert Solution().getBiggestThree([[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [20, 30, 200, 40, 10], [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]]) == [228, 216, 211]

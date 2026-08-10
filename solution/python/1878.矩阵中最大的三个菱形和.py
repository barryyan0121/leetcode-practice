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

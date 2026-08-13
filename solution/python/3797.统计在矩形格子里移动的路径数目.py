from math import isqrt
from typing import List


class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        mod = 10**9 + 7
        n, m = len(grid), len(grid[0])
        horizontal = d
        diagonal = isqrt(d * d - 1)

        def ranges(values: List[int]) -> List[int]:
            prefix = [0] * (m + 1)
            for i, value in enumerate(values):
                prefix[i + 1] = (prefix[i] + value) % mod
            return prefix

        previous = [1 if cell == "." else 0 for cell in grid[-1]]
        for row in range(n - 1, -1, -1):
            if row == n - 1:
                enter = previous[:]
            else:
                prefix = ranges(previous)
                enter = [0] * m
                for col in range(m):
                    if grid[row][col] == ".":
                        left = max(0, col - diagonal)
                        right = min(m - 1, col + diagonal)
                        enter[col] = (prefix[right + 1] - prefix[left]) % mod

            prefix = ranges(enter)
            same = [0] * m
            for col in range(m):
                if grid[row][col] == ".":
                    left = max(0, col - horizontal)
                    right = min(m - 1, col + horizontal)
                    same[col] = (prefix[right + 1] - prefix[left] - enter[col]) % mod
            previous = [(a + b) % mod for a, b in zip(enter, same)]

        return sum(previous) % mod


if __name__ == "__main__":
    s = Solution()
    assert s.numberOfRoutes(["..", "#."], 1) == 2
    assert s.numberOfRoutes(["..", "#."], 2) == 4
    assert s.numberOfRoutes(["#"], 750) == 0
    assert s.numberOfRoutes([".."], 1) == 4

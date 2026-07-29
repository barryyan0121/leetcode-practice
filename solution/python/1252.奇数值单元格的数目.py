from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows, cols = set(), set()
        for row, col in indices:
            rows.symmetric_difference_update([row])
            cols.symmetric_difference_update([col])
        return len(rows) * (n - len(cols)) + (m - len(rows)) * len(cols)


if __name__ == "__main__":
    test_cases = [((2, 3, [[0, 1], [1, 1]]), 6), ((2, 2, [[1, 1], [0, 0]]), 0)]
    for _, ((m, n, indices), expected) in enumerate(test_cases):
        assert Solution().oddCells(m, n, indices) == expected

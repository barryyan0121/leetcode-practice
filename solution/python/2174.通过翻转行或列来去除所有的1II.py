"""2174. 通过翻转行或列来去除所有的 1 II"""

from collections import deque


class Solution:
    def removeOnes(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        full = (1 << (rows * cols)) - 1
        row_masks = []
        col_masks = []
        for row in range(rows):
            row_masks.append(sum(1 << (row * cols + col) for col in range(cols)))
        for col in range(cols):
            col_masks.append(sum(1 << (row * cols + col) for row in range(rows)))
        start = sum(
            1 << (row * cols + col)
            for row in range(rows)
            for col in range(cols)
            if grid[row][col]
        )
        queue = deque([(start, 0)])
        seen = {start}
        while queue:
            state, distance = queue.popleft()
            if state == 0:
                return distance
            for row in range(rows):
                for col in range(cols):
                    bit = 1 << (row * cols + col)
                    if state & bit:
                        next_state = state & ~row_masks[row] & ~col_masks[col]
                        if next_state not in seen:
                            seen.add(next_state)
                            queue.append((next_state, distance + 1))
        return -1


if __name__ == "__main__":
    assert Solution().removeOnes([[1, 1, 1], [1, 1, 1], [0, 1, 0]]) == 2

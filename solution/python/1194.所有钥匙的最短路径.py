from collections import deque
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows, cols = len(grid), len(grid[0])
        target = 0
        for row in range(rows):
            for col in range(cols):
                char = grid[row][col]
                if char == "@":
                    start = (row, col)
                elif char.islower():
                    target |= 1 << (ord(char) - ord("a"))

        queue = deque([(start[0], start[1], 0, 0)])
        seen = {(start[0], start[1], 0)}
        while queue:
            row, col, keys, distance = queue.popleft()
            if keys == target:
                return distance
            for next_row, next_col in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    continue
                char = grid[next_row][next_col]
                if char == "#" or (
                    char.isupper() and not keys & (1 << (ord(char) - ord("A")))
                ):
                    continue
                next_keys = keys
                if char.islower():
                    next_keys |= 1 << (ord(char) - ord("a"))
                state = (next_row, next_col, next_keys)
                if state not in seen:
                    seen.add(state)
                    queue.append((next_row, next_col, next_keys, distance + 1))
        return -1


if __name__ == "__main__":
    test_cases = [(["@.a..", "###.#", "b.A.B"], 8), (["@..aA", "..B#.", "....b"], 6)]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().shortestPathAllKeys(grid) == expected

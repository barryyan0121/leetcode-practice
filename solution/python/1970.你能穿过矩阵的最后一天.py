"""1970. 你能穿过矩阵的最后一天"""


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        def can_cross(day: int) -> bool:
            blocked = {((r - 1) * col + c - 1) for r, c in cells[:day]}
            stack = [c for c in range(col) if c not in blocked]
            seen = set(stack)
            while stack:
                point = stack.pop()
                r, c = divmod(point, col)
                if r == row - 1:
                    return True
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    neighbor = nr * col + nc
                    if (
                        0 <= nr < row
                        and 0 <= nc < col
                        and neighbor not in blocked
                        and neighbor not in seen
                    ):
                        seen.add(neighbor)
                        stack.append(neighbor)
            return False

        low, high = 0, len(cells)
        while low < high:
            middle = (low + high + 1) // 2
            if can_cross(middle):
                low = middle
            else:
                high = middle - 1
        return low


if __name__ == "__main__":
    test_cases = [((2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]]), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().latestDayToCross(*args) == expected

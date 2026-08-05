class Solution:
    def specialGrid(self, n: int) -> list[list[int]]:
        def build(level: int) -> list[list[int]]:
            if level == 0:
                return [[0]]
            half = 1 << (level - 1)
            small = build(level - 1)
            block = half * half
            grid = [[0] * (half * 2) for _ in range(half * 2)]
            for row in range(half):
                for column in range(half):
                    value = small[row][column]
                    grid[row][column + half] = value
                    grid[row + half][column + half] = value + block
                    grid[row + half][column] = value + 2 * block
                    grid[row][column] = value + 3 * block
            return grid

        return build(n)


if __name__ == "__main__":
    test_cases = [(0, [[0]]), (1, [[3, 0], [2, 1]])]
    for _, (n, expected) in enumerate(test_cases):
        assert Solution().specialGrid(n) == expected

# @lc app=leetcode.cn id=1559 lang=python3


class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        rows, columns = len(grid), len(grid[0])
        visited = [[False] * columns for _ in range(rows)]
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(row: int, column: int, parent: tuple[int, int]) -> bool:
            visited[row][column] = True
            for dr, dc in directions:
                nr, nc = row + dr, column + dc
                if not (0 <= nr < rows and 0 <= nc < columns):
                    continue
                if grid[nr][nc] != grid[row][column] or (nr, nc) == parent:
                    continue
                if visited[nr][nc] or dfs(nr, nc, (row, column)):
                    return True
            return False

        for row in range(rows):
            for column in range(columns):
                if not visited[row][column] and dfs(row, column, (-1, -1)):
                    return True
        return False


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.containsCycle,
            (
                [
                    ["a", "a", "a", "a"],
                    ["a", "b", "b", "a"],
                    ["a", "b", "b", "a"],
                    ["a", "a", "a", "a"],
                ],
            ),
            True,
        ),
        (solution.containsCycle, ([["a", "b"], ["b", "a"]],), False),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1559 题 "二维网格图中探测环" 所有测试用例通过')

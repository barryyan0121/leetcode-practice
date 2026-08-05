"""1905. 统计子岛屿"""


class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        rows, cols = len(grid2), len(grid2[0])
        answer = 0
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] != 1:
                    continue
                valid = True
                stack = [(row, col)]
                grid2[row][col] = 0
                while stack:
                    current_row, current_col = stack.pop()
                    if grid1[current_row][current_col] == 0:
                        valid = False
                    for next_row, next_col in (
                        (current_row - 1, current_col),
                        (current_row + 1, current_col),
                        (current_row, current_col - 1),
                        (current_row, current_col + 1),
                    ):
                        if (
                            0 <= next_row < rows
                            and 0 <= next_col < cols
                            and grid2[next_row][next_col] == 1
                        ):
                            grid2[next_row][next_col] = 0
                            stack.append((next_row, next_col))
                answer += valid
        return answer


if __name__ == "__main__":
    test_cases = [
        (
            (
                [[1, 1, 1, 0], [0, 1, 1, 1], [0, 0, 0, 0]],
                [[1, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 0]],
            ),
            1,
        )
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countSubIslands(*args) == expected

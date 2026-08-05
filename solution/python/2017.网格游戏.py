"""2017. 网格游戏"""


class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        top = sum(grid[0])
        bottom = 0
        answer = float("inf")
        for i, value in enumerate(grid[0]):
            top -= value
            answer = min(answer, max(top, bottom))
            bottom += grid[1][i]
        return answer


if __name__ == "__main__":
    test_cases = [(([[2, 5, 4], [1, 5, 1]],), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().gridGame(*args) == expected

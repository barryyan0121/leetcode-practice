"""2128. 删除所有行和列中的一"""


class Solution:
    def removeOnes(self, grid: list[list[int]]) -> bool:
        first = grid[0]
        return all(
            row == first or row == [1 - value for value in first] for row in grid
        )


if __name__ == "__main__":
    test_cases = [(([[0, 1], [1, 0]],), True), (([[1, 0], [1, 1]],), False)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().removeOnes(*args) == expected

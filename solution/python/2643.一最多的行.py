"""2643. 一最多的行"""


class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        best = max((sum(row), -index) for index, row in enumerate(mat))
        return [-best[1], best[0]]


if __name__ == "__main__":
    test_cases = [(([[0, 1], [1, 0]],), [0, 1])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().rowAndMaximumOnes(*args) == expected

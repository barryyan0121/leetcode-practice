"""1992. 找到所有的农场组"""


class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        rows, cols = len(land), len(land[0])
        answer = []
        for r in range(rows):
            for c in range(cols):
                if (
                    land[r][c] != 1
                    or (r and land[r - 1][c] == 1)
                    or (c and land[r][c - 1] == 1)
                ):
                    continue
                bottom, right = r, c
                while bottom + 1 < rows and land[bottom + 1][c] == 1:
                    bottom += 1
                while right + 1 < cols and land[r][right + 1] == 1:
                    right += 1
                answer.append([r, c, bottom, right])
        return answer


if __name__ == "__main__":
    test_cases = [(([[1, 0, 0], [0, 1, 1], [0, 1, 1]],), [[0, 0, 0, 0], [1, 1, 2, 2]])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findFarmland(*args) == expected

"""1992. 查找所有农场组"""


class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        rows, cols = len(land), len(land[0])
        result = []
        for row in range(rows):
            for col in range(cols):
                if (
                    land[row][col] == 0
                    or (row and land[row - 1][col])
                    or (col and land[row][col - 1])
                ):
                    continue
                bottom, right = row, col
                while bottom + 1 < rows and land[bottom + 1][col]:
                    bottom += 1
                while right + 1 < cols and land[bottom][right + 1]:
                    right += 1
                result.append([row, col, bottom, right])
        return result


if __name__ == "__main__":
    assert Solution().findFarmland([[1, 0, 0], [0, 1, 1], [0, 1, 1]]) == [
        [0, 0, 0, 0],
        [1, 1, 2, 2],
    ]

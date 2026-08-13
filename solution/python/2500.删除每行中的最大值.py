"""2500. 删除每行中的最大值"""


class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        for row in grid:
            row.sort()
        return sum(max(row[column] for row in grid) for column in range(len(grid[0])))

if __name__ == "__main__":
    assert Solution().deleteGreatestValue([[1,2,4],[3,3,1]]) == 8

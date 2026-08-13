"""2387. 行和列有序矩阵的中位数"""


class Solution:
    def matrixMedian(self, grid: list[list[int]]) -> int:
        low = min(row[0] for row in grid)
        high = max(row[-1] for row in grid)
        target = (len(grid) * len(grid[0]) + 1) // 2
        while low < high:
            middle = (low + high) // 2
            count = sum(sum(value <= middle for value in row) for row in grid)
            if count < target:
                low = middle + 1
            else:
                high = middle
        return low

if __name__ == "__main__":
    assert Solution().matrixMedian([[1,1,3,3,4],[1,2,3,4,5],[1,3,3,3,5]]) == 3

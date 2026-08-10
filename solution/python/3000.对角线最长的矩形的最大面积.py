"""3000. 对角线最长的矩形的最大面积"""


class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        best_diagonal = best_area = 0
        for length, width in dimensions:
            diagonal = length * length + width * width
            if diagonal > best_diagonal or (
                diagonal == best_diagonal and length * width > best_area
            ):
                best_diagonal, best_area = diagonal, length * width
        return best_area


if __name__ == "__main__":
    assert Solution().areaOfMaxDiagonal([[9, 3], [8, 6]]) == 48

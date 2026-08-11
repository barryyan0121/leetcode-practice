"""4016. 两个不重叠子正方形的最大面积"""


class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        valmerinto = mat
        rows, cols = len(valmerinto), len(valmerinto[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for row in range(rows):
            for col in range(cols):
                prefix[row + 1][col + 1] = (
                    valmerinto[row][col]
                    + prefix[row][col + 1]
                    + prefix[row + 1][col]
                    - prefix[row][col]
                )

        def possible(side: int) -> bool:
            min_row = min_col = rows + cols
            max_row = max_col = -1
            area = side * side
            for row in range(rows - side + 1):
                for col in range(cols - side + 1):
                    total = (
                        prefix[row + side][col + side]
                        - prefix[row][col + side]
                        - prefix[row + side][col]
                        + prefix[row][col]
                    )
                    if total == area:
                        min_row = min(min_row, row)
                        max_row = max(max_row, row)
                        min_col = min(min_col, col)
                        max_col = max(max_col, col)
            return max_row >= 0 and (
                max_row - min_row >= side or max_col - min_col >= side
            )

        left, right = 1, min(rows, cols)
        answer = 0
        while left <= right:
            middle = (left + right) // 2
            if possible(middle):
                answer = middle
                left = middle + 1
            else:
                right = middle - 1
        return answer * answer


if __name__ == "__main__":
    assert Solution().maxArea([[1, 1, 1, 0], [1, 1, 1, 1], [0, 0, 1, 1]]) == 4
    assert Solution().maxArea([[0, 1], [1, 0]]) == 1
    assert Solution().maxArea([[0, 0], [0, 1]]) == 0

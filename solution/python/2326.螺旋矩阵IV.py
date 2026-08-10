"""2326. 螺旋矩阵 IV"""


class Solution:
    def spiralMatrix(self, m: int, n: int, head) -> list[list[int]]:
        matrix = [[-1] * n for _ in range(m)]
        top, bottom, left, right = 0, m - 1, 0, n - 1
        while head:
            for j in range(left, right + 1):
                if not head:
                    break
                matrix[top][j], head = head.val, head.next
            top += 1
            for i in range(top, bottom + 1):
                if not head:
                    break
                matrix[i][right], head = head.val, head.next
            right -= 1
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    if not head:
                        break
                    matrix[bottom][j], head = head.val, head.next
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    if not head:
                        break
                    matrix[i][left], head = head.val, head.next
                left += 1
        return matrix

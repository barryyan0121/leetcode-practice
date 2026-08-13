#
# @lc app=leetcode.cn id=723 lang=python3
#
# [723] 粉碎糖果
#


# @lc code=start
class Solution:
    def candyCrush(self, board):
        rows, cols = len(board), len(board[0])
        while True:
            crush = set()
            for r in range(rows):
                for c in range(cols - 2):
                    value = abs(board[r][c])
                    if value and value == abs(board[r][c + 1]) == abs(board[r][c + 2]):
                        crush.update({(r, c), (r, c + 1), (r, c + 2)})
            for c in range(cols):
                for r in range(rows - 2):
                    value = abs(board[r][c])
                    if value and value == abs(board[r + 1][c]) == abs(board[r + 2][c]):
                        crush.update({(r, c), (r + 1, c), (r + 2, c)})
            if not crush:
                return board
            for r, c in crush:
                board[r][c] = 0
            for c in range(cols):
                write = rows - 1
                for r in range(rows - 1, -1, -1):
                    if board[r][c]:
                        board[write][c] = board[r][c]
                        write -= 1
                for r in range(write, -1, -1):
                    board[r][c] = 0


# @lc code=end

if __name__ == "__main__":
    assert Solution().candyCrush([[1, 1, 1], [2, 3, 4]]) == [[0, 0, 0], [2, 3, 4]]
    assert Solution().candyCrush([[1, 2, 3], [4, 5, 6]]) == [[1, 2, 3], [4, 5, 6]]

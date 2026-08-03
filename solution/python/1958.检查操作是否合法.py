# @lc app=leetcode.cn id=1958 lang=python3


class Solution:
    def checkMove(
        self, board: list[list[str]], rMove: int, cMove: int, color: str
    ) -> bool:
        opponent = "W" if color == "B" else "B"
        rows = len(board)
        cols = len(board[0])
        for dr, dc in (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ):
            row, col = rMove + dr, cMove + dc
            opponent_count = 0
            while 0 <= row < rows and 0 <= col < cols and board[row][col] == opponent:
                opponent_count += 1
                row += dr
                col += dc
            if (
                opponent_count
                and 0 <= row < rows
                and 0 <= col < cols
                and board[row][col] == color
            ):
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    empty = [["."] * 8 for _ in range(8)]
    empty[3][2] = "B"
    empty[3][3] = "W"
    test_cases = [
        (solution.checkMove, (empty, 3, 4, "B"), True),
        (solution.checkMove, (empty, 3, 4, "W"), False),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1958 题 "检查操作是否合法" 所有测试用例通过')

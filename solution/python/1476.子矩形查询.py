# @lc app=leetcode.cn id=1476 lang=python3


class SubrectangleQueries:
    def __init__(self, rectangle: list[list[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, newValue: int
    ) -> None:
        for row in range(row1, row2 + 1):
            self.rectangle[row][col1 : col2 + 1] = [newValue] * (col2 - col1 + 1)

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


if __name__ == "__main__":

    def run_case():
        rectangle = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
        rectangle.updateSubrectangle(0, 0, 3, 2, 5)
        return rectangle.getValue(0, 2)

    test_cases = [(run_case, (), 5)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1476 题 "子矩形查询" 所有测试用例通过')

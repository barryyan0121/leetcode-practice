# @lc app=leetcode.cn id=1428 lang=python3


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: "BinaryMatrix") -> int:
        rows, cols = binaryMatrix.dimensions()
        row, col, answer = 0, cols - 1, -1
        while row < rows and col >= 0:
            if binaryMatrix.get(row, col):
                answer = col
                col -= 1
            else:
                row += 1
        return answer


if __name__ == "__main__":

    class BinaryMatrix:
        def __init__(self, matrix):
            self.matrix = matrix

        def get(self, row, col):
            return self.matrix[row][col]

        def dimensions(self):
            return len(self.matrix), len(self.matrix[0])

    test_cases = [
        (Solution().leftMostColumnWithOne, (BinaryMatrix([[0, 0], [1, 1]]),), 0),
        (Solution().leftMostColumnWithOne, (BinaryMatrix([[0, 0], [0, 1]]),), 1),
        (Solution().leftMostColumnWithOne, (BinaryMatrix([[0, 0], [0, 0]]),), -1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1428 题 "至少有一个 1 的最左端列" 所有测试用例通过')

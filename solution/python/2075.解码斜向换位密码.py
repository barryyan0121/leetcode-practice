"""2075. 解码斜向换位密码"""


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        columns = len(encodedText) // rows
        grid = [encodedText[i * columns : (i + 1) * columns] for i in range(rows)]
        answer = []
        for start in range(columns):
            row, column = 0, start
            while row < rows and column < columns:
                answer.append(grid[row][column])
                row += 1
                column += 1
        return "".join(answer).rstrip()


if __name__ == "__main__":
    test_cases = [(("ch   ie   pr", 3), "cipher")]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().decodeCiphertext(*args) == expected

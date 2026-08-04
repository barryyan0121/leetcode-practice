class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        columns = len(grid[0])
        balance = [0] * columns
        present = [0] * columns
        answer = 0
        for row in grid:
            row_balance = 0
            row_present = 0
            for column, character in enumerate(row):
                balance[column] += (character == "X") - (character == "Y")
                present[column] += character != "."
                row_balance += balance[column]
                row_present += present[column]
                if row_balance == 0 and row_present:
                    answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [
        (([["X", "Y", "."], ["Y", ".", "."]]), 3),
        (([["X", "X"], ["X", "Y"]]), 0),
        (([[".", "."], [".", "."]]), 0),
    ]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().numberOfSubmatrices(grid) == expected

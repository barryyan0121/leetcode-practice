class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        rows, columns = len(str1), len(str2)
        lcs = [[0] * (columns + 1) for _ in range(rows + 1)]
        for row in range(rows - 1, -1, -1):
            for column in range(columns - 1, -1, -1):
                if str1[row] == str2[column]:
                    lcs[row][column] = 1 + lcs[row + 1][column + 1]
                else:
                    lcs[row][column] = max(lcs[row + 1][column], lcs[row][column + 1])

        row = column = 0
        result = []
        while row < rows and column < columns:
            if str1[row] == str2[column]:
                result.append(str1[row])
                row += 1
                column += 1
            elif lcs[row + 1][column] >= lcs[row][column + 1]:
                result.append(str1[row])
                row += 1
            else:
                result.append(str2[column])
                column += 1
        return "".join(result) + str1[row:] + str2[column:]


if __name__ == "__main__":

    def is_subsequence(subsequence: str, sequence: str) -> bool:
        index = 0
        for char in sequence:
            if index < len(subsequence) and char == subsequence[index]:
                index += 1
        return index == len(subsequence)

    test_cases = [
        ("abac", "cab", 5),
        ("", "abc", 3),
        ("abc", "abc", 3),
        ("geek", "eke", 5),
    ]
    for _, (str1, str2, expected_length) in enumerate(test_cases):
        result = Solution().shortestCommonSupersequence(str1, str2)
        assert len(result) == expected_length
        assert is_subsequence(str1, result) and is_subsequence(str2, result)

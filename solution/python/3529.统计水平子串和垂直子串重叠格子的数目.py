class Solution:
    def countCells(self, grid: list[list[str]], pattern: str) -> int:
        rows, columns = len(grid), len(grid[0])
        horizontal = "".join("".join(row) for row in grid)
        vertical = "".join(
            grid[row][column] for column in range(columns) for row in range(rows)
        )

        def covered(text: str) -> list[bool]:
            prefix = [0] * len(pattern)
            for index in range(1, len(pattern)):
                candidate = prefix[index - 1]
                while candidate and pattern[index] != pattern[candidate]:
                    candidate = prefix[candidate - 1]
                if pattern[index] == pattern[candidate]:
                    candidate += 1
                prefix[index] = candidate

            difference = [0] * (len(text) + 1)
            matched = 0
            for index, value in enumerate(text):
                while matched and value != pattern[matched]:
                    matched = prefix[matched - 1]
                if value == pattern[matched]:
                    matched += 1
                if matched == len(pattern):
                    start = index - len(pattern) + 1
                    difference[start] += 1
                    difference[index + 1] -= 1
                    matched = prefix[matched - 1]

            answer = [False] * len(text)
            active = 0
            for index in range(len(text)):
                active += difference[index]
                answer[index] = active > 0
            return answer

        horizontal_covered = covered(horizontal)
        vertical_covered = covered(vertical)
        answer = 0
        for row in range(rows):
            for column in range(columns):
                horizontal_index = row * columns + column
                vertical_index = column * rows + row
                answer += (
                    horizontal_covered[horizontal_index]
                    and vertical_covered[vertical_index]
                )
        return answer


if __name__ == "__main__":
    test_cases = [
        (
            (
                [
                    ["a", "a", "c", "c"],
                    ["b", "b", "b", "c"],
                    ["a", "a", "b", "a"],
                    ["c", "a", "a", "c"],
                    ["a", "a", "b", "a"],
                ],
                "abaca",
            ),
            1,
        ),
        (([["a"]], "a"), 1),
    ]
    for _, ((grid, pattern), expected) in enumerate(test_cases):
        assert Solution().countCells(grid, pattern) == expected

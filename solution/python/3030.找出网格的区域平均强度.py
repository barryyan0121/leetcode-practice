class Solution:
    def resultGrid(self, image: list[list[int]], threshold: int) -> list[list[int]]:
        rows, columns = len(image), len(image[0])
        totals = [[0] * columns for _ in range(rows)]
        counts = [[0] * columns for _ in range(rows)]
        for top in range(rows - 2):
            for left in range(columns - 2):
                valid = True
                for row in range(top, top + 3):
                    for column in range(left, left + 2):
                        if abs(image[row][column] - image[row][column + 1]) > threshold:
                            valid = False
                for row in range(top, top + 2):
                    for column in range(left, left + 3):
                        if abs(image[row][column] - image[row + 1][column]) > threshold:
                            valid = False
                if valid:
                    average = (
                        sum(
                            image[row][column]
                            for row in range(top, top + 3)
                            for column in range(left, left + 3)
                        )
                        // 9
                    )
                    for row in range(top, top + 3):
                        for column in range(left, left + 3):
                            totals[row][column] += average
                            counts[row][column] += 1
        return [
            [
                (
                    totals[row][column] // counts[row][column]
                    if counts[row][column]
                    else image[row][column]
                )
                for column in range(columns)
            ]
            for row in range(rows)
        ]


if __name__ == "__main__":
    test_cases = [
        (
            ([[5, 6, 7, 10], [8, 9, 10, 10], [11, 12, 13, 10]], 3),
            [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]],
        ),
        (
            ([[5, 6, 7], [8, 9, 10], [11, 12, 13]], 1),
            [[5, 6, 7], [8, 9, 10], [11, 12, 13]],
        ),
    ]
    for _, ((image, threshold), expected) in enumerate(test_cases):
        assert Solution().resultGrid(image, threshold) == expected

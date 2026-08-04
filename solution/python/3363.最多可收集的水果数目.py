class Solution:
    def maxCollectedFruits(self, fruits: list[list[int]]) -> int:
        size = len(fruits)
        diagonal = sum(fruits[index][index] for index in range(size))
        negative_infinity = -(10**18)

        top = [negative_infinity] * size
        top[-1] = fruits[0][-1]
        for row in range(1, size):
            next_top = [negative_infinity] * size
            for column in range(row, size):
                best = top[column]
                if column:
                    best = max(best, top[column - 1])
                if column + 1 < size:
                    best = max(best, top[column + 1])
                if best != negative_infinity:
                    next_top[column] = best + (
                        0 if row == column else fruits[row][column]
                    )
            top = next_top

        bottom = [negative_infinity] * size
        bottom[-1] = fruits[-1][0]
        for column in range(1, size):
            next_bottom = [negative_infinity] * size
            for row in range(column, size):
                best = bottom[row]
                if row:
                    best = max(best, bottom[row - 1])
                if row + 1 < size:
                    best = max(best, bottom[row + 1])
                if best != negative_infinity:
                    next_bottom[row] = best + (
                        0 if row == column else fruits[row][column]
                    )
            bottom = next_bottom

        return diagonal + top[-1] + bottom[-1]


if __name__ == "__main__":
    test_cases = [
        (([[1, 2, 3, 4], [5, 6, 8, 7], [9, 10, 11, 12], [13, 14, 15, 16]],), 100),
        (([[1, 1], [1, 1]],), 4),
    ]
    for _, ((fruits,), expected) in enumerate(test_cases):
        assert Solution().maxCollectedFruits(fruits) == expected

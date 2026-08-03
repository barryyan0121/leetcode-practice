from collections import Counter
from math import isqrt


class Solution:
    def mostFrequentPrime(self, mat: list[list[int]]) -> int:
        rows, columns = len(mat), len(mat[0])
        counts = Counter()
        directions = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if dr or dc]

        def is_prime(number: int) -> bool:
            if number < 2:
                return False
            for divisor in range(2, isqrt(number) + 1):
                if number % divisor == 0:
                    return False
            return True

        for row in range(rows):
            for column in range(columns):
                for dr, dc in directions:
                    number = mat[row][column]
                    next_row, next_column = row + dr, column + dc
                    while 0 <= next_row < rows and 0 <= next_column < columns:
                        number = number * 10 + mat[next_row][next_column]
                        if number > 10 and is_prime(number):
                            counts[number] += 1
                        next_row += dr
                        next_column += dc
        return max(counts, key=lambda number: (counts[number], number), default=-1)


if __name__ == "__main__":
    test_cases = [
        ([[1, 1], [9, 9], [1, 1]], 19),
        ([[7]], -1),
        ([[9, 7, 8], [4, 6, 5], [2, 8, 6]], 97),
    ]
    for _, (mat, expected) in enumerate(test_cases):
        assert Solution().mostFrequentPrime(mat) == expected

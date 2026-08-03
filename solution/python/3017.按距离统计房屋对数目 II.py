from itertools import accumulate


class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        if abs(x - y) <= 1:
            return list(range(2 * n - 2, -1, -2))

        def add(start: int, end: int, value: int) -> None:
            if start <= end:
                difference[start] += value
                difference[end + 1] -= value

        x, y = sorted((x, y))
        difference = [0] + [n - 1] + [-1] * n
        for start in range(1, (x + y) // 2):
            end = (x + y + 3) // 2 if start <= x else start + 1 + (y - x + 1) // 2
            add(end - start, n - start, -1)
            add(abs(x - start) + 1, abs(x - start) + n - y + 1, 1)
            add(abs(x - start) + 2, abs(x - start) + y - end + 1, 1)
        return [value * 2 for value in accumulate(difference[1:-1])]


if __name__ == "__main__":
    test_cases = [
        ((3, 1, 3), [6, 0, 0]),
        ((5, 2, 4), [10, 8, 2, 0, 0]),
        ((4, 1, 1), [6, 4, 2, 0]),
    ]
    for _, ((n, x, y), expected) in enumerate(test_cases):
        assert Solution().countOfPairs(n, x, y) == expected

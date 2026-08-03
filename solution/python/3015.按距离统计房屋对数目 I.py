class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        answer = [0] * n
        for start in range(1, n + 1):
            for end in range(start + 1, n + 1):
                distance = min(
                    end - start,
                    abs(start - x) + 1 + abs(end - y),
                    abs(start - y) + 1 + abs(end - x),
                )
                answer[distance - 1] += 2
        return answer


if __name__ == "__main__":
    test_cases = [
        ((3, 1, 3), [6, 0, 0]),
        ((5, 2, 4), [10, 8, 2, 0, 0]),
    ]
    for _, ((n, x, y), expected) in enumerate(test_cases):
        assert Solution().countOfPairs(n, x, y) == expected

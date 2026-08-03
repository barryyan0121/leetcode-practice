class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        values = [1] * n
        for _ in range(k):
            for index in range(1, n):
                values[index] = (values[index] + values[index - 1]) % 1_000_000_007
        return values[-1]


if __name__ == "__main__":
    test_cases = [((4, 5), 56), ((5, 3), 35)]
    for _, ((n, k), expected) in enumerate(test_cases):
        assert Solution().valueAfterKSeconds(n, k) == expected

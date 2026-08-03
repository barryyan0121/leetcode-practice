class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return ((n + 1) // 2) * (m // 2) + (n // 2) * ((m + 1) // 2)


if __name__ == "__main__":
    test_cases = [((3, 2), 3), ((1, 1), 0)]
    for _, ((n, m), expected) in enumerate(test_cases):
        assert Solution().flowerGame(n, m) == expected

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        cycle = 2 * (n - 1)
        position = k % cycle
        return position if position < n else cycle - position


if __name__ == "__main__":
    test_cases = [((3, 5), 1), ((5, 6), 2)]
    for _, ((n, k), expected) in enumerate(test_cases):
        assert Solution().numberOfChild(n, k) == expected

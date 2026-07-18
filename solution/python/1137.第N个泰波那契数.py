class Solution:
    def tribonacci(self, n: int) -> int:
        first, second, third = 0, 1, 1
        for _ in range(3, n + 1):
            first, second, third = second, third, first + second + third
        return (first, second, third)[n] if n < 3 else third


if __name__ == "__main__":
    test_cases = [(0, 0), (1, 1), (2, 1), (4, 4), (25, 1389537)]
    for _, (n, expected) in enumerate(test_cases):
        assert Solution().tribonacci(n) == expected

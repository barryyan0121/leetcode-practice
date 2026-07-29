class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5


if __name__ == "__main__":
    test_cases = [(1, 1.0), (2, 0.5)]
    for _, (n, expected) in enumerate(test_cases):
        assert Solution().nthPersonGetsNthSeat(n) == expected

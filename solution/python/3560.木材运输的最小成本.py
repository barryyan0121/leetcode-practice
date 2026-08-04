"""3560. 木材运输的最小成本"""


class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        return sum(k * (length - k) for length in (n, m) if length > k)


if __name__ == "__main__":
    test_cases = [
        ((6, 5, 5), 5),
        ((4, 4, 6), 0),
    ]
    for _, ((n, m, k), expected) in enumerate(test_cases):
        assert Solution().minCuttingCost(n, m, k) == expected

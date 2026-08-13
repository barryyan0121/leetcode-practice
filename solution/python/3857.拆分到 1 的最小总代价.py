"""3857. 拆分到 1 的最小总代价"""


class Solution:
    def minCost(self, n: int) -> int:
        return n * (n - 1) // 2


if __name__ == "__main__":
    test_cases = [((3,), 3), ((4,), 6)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minCost(*args) == expected

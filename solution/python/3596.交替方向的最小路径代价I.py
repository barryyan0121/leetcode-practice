"""3596. 交替方向的最小路径代价 I"""


class Solution:
    def minCost(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        if (m, n) in ((1, 2), (2, 1)):
            return 3
        return -1


if __name__ == "__main__":
    test_cases = [
        ((1, 1), 1),
        ((2, 1), 3),
        ((1, 2), 3),
        ((2, 2), -1),
    ]
    for _, ((m, n), expected) in enumerate(test_cases):
        assert Solution().minCost(m, n) == expected

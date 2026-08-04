"""3492. 船上可以装载的最大集装箱数量"""


class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return min(n * n, maxWeight // w)


if __name__ == "__main__":
    test_cases = [
        ((2, 3, 15), 4),
        ((3, 5, 20), 4),
    ]
    for _, ((n, w, max_weight), expected) in enumerate(test_cases):
        assert Solution().maxContainers(n, w, max_weight) == expected

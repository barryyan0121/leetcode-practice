"""2078. 两栋最远房子之间的最大距离"""


class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        return max(
            next(i for i in range(len(colors)) if colors[i] != colors[0]),
            next(i for i in range(len(colors) - 1, -1, -1) if colors[i] != colors[0]),
            len(colors)
            - 1
            - next(i for i in range(len(colors)) if colors[i] != colors[-1]),
        )


if __name__ == "__main__":
    test_cases = [(([1, 1, 1, 6, 1, 1, 1],), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxDistance(*args) == expected

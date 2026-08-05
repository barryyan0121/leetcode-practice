"""3925. 连接逆序数组"""


class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums + nums[::-1]


if __name__ == "__main__":
    test_cases = [(([1, 2, 3],), [1, 2, 3, 3, 2, 1]), (([1],), [1, 1])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().concatWithReverse(*args) == expected

"""2980. 检查按位或是否存在尾随零"""


class Solution:
    def hasTrailingZeros(self, nums: list[int]) -> bool:
        return sum(value % 2 == 0 for value in nums) >= 2


if __name__ == "__main__":
    test_cases = [(([1, 2, 3, 4],), True), (([1, 3, 5],), False)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().hasTrailingZeros(*args) == expected

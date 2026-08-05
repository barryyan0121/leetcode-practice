"""2148. 元素计数"""


class Solution:
    def countElements(self, nums: list[int]) -> int:
        low, high = min(nums), max(nums)
        return sum(low < value < high for value in nums)


if __name__ == "__main__":
    test_cases = [(([11, 7, 2, 15],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countElements(*args) == expected

"""2149. 按符号重排数组"""


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positives = [value for value in nums if value > 0]
        negatives = [value for value in nums if value < 0]
        return [value for pair in zip(positives, negatives) for value in pair]


if __name__ == "__main__":
    test_cases = [(([3, 1, -2, -5, 2, -4],), [3, -2, 1, -5, 2, -4])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().rearrangeArray(*args) == expected

"""2099. 找到和最大的长度为 K 的子序列"""


class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        selected = sorted(enumerate(nums), key=lambda item: item[1], reverse=True)[:k]
        return [value for index, value in sorted(selected)]


if __name__ == "__main__":
    test_cases = [(([2, 1, 3, 3], 2), [3, 3])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxSubsequence(*args) == expected

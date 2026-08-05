"""3936. 将 0 移到末尾的最少交换次数"""


class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        nonzero = sum(value != 0 for value in nums)
        return nonzero - sum(value != 0 for value in nums[:nonzero])


if __name__ == "__main__":
    test_cases = [([0, 1, 0, 3, 12], 2), ([0, 1, 0, 2], 1), ([1, 2, 0], 0)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().minimumSwaps(nums) == expected

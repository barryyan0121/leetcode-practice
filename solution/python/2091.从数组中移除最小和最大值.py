"""2091. 从数组中移除最小和最大值"""


class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        left = min(nums.index(min(nums)), nums.index(max(nums)))
        right = max(nums.index(min(nums)), nums.index(max(nums)))
        return min(right + 1, n - left, left + 1 + n - right)


if __name__ == "__main__":
    test_cases = [(([2, 10, 7, 5, 4, 1, 8, 6],), 5)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumDeletions(*args) == expected

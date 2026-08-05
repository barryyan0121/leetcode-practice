"""1984. 学生分数的最小差值"""


class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))


if __name__ == "__main__":
    test_cases = [(([90, 3, 1, 4, 2, 50, 70, 80, 100, 40], 5), 39)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumDifference(*args) == expected

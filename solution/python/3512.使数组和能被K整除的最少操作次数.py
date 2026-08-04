"""3512. 使数组和能被 K 整除的最少操作次数"""


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        return sum(nums) % k


if __name__ == "__main__":
    test_cases = [
        (([3, 9, 7], 5), 4),
        (([4, 1, 3], 4), 0),
        (([3, 2], 6), 5),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().minOperations(nums, k) == expected

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        if any(value < k for value in nums):
            return -1
        return len({value for value in nums if value > k})


if __name__ == "__main__":
    test_cases = [
        (([5, 2, 5, 4, 5], 2), 2),
        (([2, 1, 2], 2), -1),
        (([9, 7, 5, 3], 1), 4),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().minOperations(nums, k) == expected

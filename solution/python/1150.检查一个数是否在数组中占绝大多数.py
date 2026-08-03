from bisect import bisect_left


class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        index = bisect_left(nums, target)
        return (
            index + len(nums) // 2 < len(nums)
            and nums[index + len(nums) // 2] == target
        )


if __name__ == "__main__":
    test_cases = [
        ([2, 4, 5, 5, 5, 5, 5, 6, 6], 5, True),
        ([10, 100, 101, 101], 101, False),
        ([1], 1, True),
        ([1, 2, 2], 2, True),
        ([1, 1, 2], 1, True),
        ([1, 2, 3], 4, False),
    ]
    for _, (nums, target, expected) in enumerate(test_cases):
        assert Solution().isMajorityElement(nums, target) == expected

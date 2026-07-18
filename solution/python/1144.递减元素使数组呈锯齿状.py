class Solution:
    def movesToMakeZigzag(self, nums: list[int]) -> int:
        costs = [0, 0]
        for index, value in enumerate(nums):
            left = nums[index - 1] if index else float("inf")
            right = nums[index + 1] if index + 1 < len(nums) else float("inf")
            costs[index % 2] += max(0, value - min(left, right) + 1)
        return min(costs)


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], 2),
        ([9, 6, 1, 6, 2], 4),
        ([2, 1, 2], 0),
        ([1], 0),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().movesToMakeZigzag(nums) == expected

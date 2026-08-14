"""3396. 使数组元素互不相同所需的最少操作次数"""


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        for operations in range((len(nums) + 2) // 3 + 1):
            tail = nums[operations * 3 :]
            if len(tail) == len(set(tail)):
                return operations
        return 0


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 2, 3, 3, 5, 7], 2),
        ([4, 5, 6, 4, 4], 2),
        ([6, 7, 8, 9], 0),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().minimumOperations(nums) == expected

class Solution:
    def minimumArrayLength(self, nums: list[int]) -> int:
        minimum = min(nums)
        if any(value % minimum for value in nums):
            return 1
        return (nums.count(minimum) + 1) // 2


if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumArrayLength([1, 4, 3, 1]) == 1
    assert solution.minimumArrayLength([5, 5, 5, 10, 5]) == 2
    assert solution.minimumArrayLength([2, 3, 4]) == 1

"""2560. 打家劫舍 IV"""


class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            count = 0
            index = 0
            while index < len(nums):
                if nums[index] <= mid:
                    count += 1
                    index += 2
                else:
                    index += 1
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    test_cases = [(([2, 3, 5, 9], 2), 5)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minCapability(*args) == expected

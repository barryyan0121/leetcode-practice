class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = ans = 0
        for right, value in enumerate(nums):
            while value - nums[left] > 2 * k:
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    assert Solution().maximumBeauty([4, 6, 1, 2], 2) == 3

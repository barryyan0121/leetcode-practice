class Solution:
    def missingElement(self, nums: list[int], k: int) -> int:
        missing = lambda i: nums[i] - nums[0] - i
        if k > missing(len(nums) - 1):
            return nums[-1] + k - missing(len(nums) - 1)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if missing(mid) < k:
                left = mid + 1
            else:
                right = mid
        return nums[left - 1] + k - missing(left - 1)


if __name__ == "__main__":
    test_cases = [([4, 7, 9, 10], 3, 8), ([1], 1, 2)]
    for _, (nums, k, expected) in enumerate(test_cases):
        assert Solution().missingElement(nums, k) == expected

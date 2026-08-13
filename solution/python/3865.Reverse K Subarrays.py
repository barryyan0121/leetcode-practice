class Solution:
    def reverseSubarrays(self, nums: list[int], k: int) -> list[int]:
        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        length = len(nums) // k
        for left in range(0, len(nums), length):
            reverse(left, left + length - 1)
        return nums


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 4, 3, 5, 6], 3), [2, 1, 3, 4, 6, 5]),
        (([5, 4, 4, 2], 1), [2, 4, 4, 5]),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().reverseSubarrays(nums, k) == expected

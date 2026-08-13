class Solution:
    def validSubarrays(self, nums: list[int], k: int) -> int:
        result = 0
        left_peak = -1
        left_choices = 0
        for right_peak in range(1, len(nums) - 1):
            if not nums[right_peak - 1] < nums[right_peak] > nums[right_peak + 1]:
                continue
            right_choices = min(right_peak - left_peak, k + 1)
            result += left_choices * right_choices
            left_peak = right_peak
            left_choices = right_choices
        result += left_choices * min(len(nums) - left_peak, k + 1)
        return result


if __name__ == "__main__":
    test_cases = [
        (([1, 3, 2], 1), 4),
        (([7, 8, 9], 2), 0),
        (([4, 3, 5, 1], 2), 6),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().validSubarrays(nums, k) == expected

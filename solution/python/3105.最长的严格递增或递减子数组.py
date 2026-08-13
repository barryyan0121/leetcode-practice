"""3105. 最长的严格递增或递减子数组"""


class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        inc = dec = answer = 1
        for index in range(1, len(nums)):
            if nums[index] > nums[index - 1]:
                inc += 1
                dec = 1
            elif nums[index] < nums[index - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            answer = max(answer, inc, dec)
        return answer


if __name__ == "__main__":
    test_cases = [([1, 4, 3, 3, 2], 2), ([3, 3, 3, 3], 1), ([3, 2, 1], 3)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().longestMonotonicSubarray(nums) == expected

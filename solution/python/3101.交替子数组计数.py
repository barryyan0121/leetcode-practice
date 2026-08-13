"""3101. 交替子数组计数"""


class Solution:
    def countAlternatingSubarrays(self, nums: list[int]) -> int:
        answer = current = 1
        for index in range(1, len(nums)):
            current = current + 1 if nums[index] != nums[index - 1] else 1
            answer += current
        return answer


if __name__ == "__main__":
    test_cases = [([0, 1, 1, 1], 5), ([1, 0, 1, 0], 10)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().countAlternatingSubarrays(nums) == expected

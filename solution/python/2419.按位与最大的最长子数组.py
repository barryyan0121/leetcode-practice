"""2419. 按位与最大的最长子数组"""


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        maximum = max(nums)
        answer = current = 0
        for value in nums:
            current = current + 1 if value == maximum else 0
            answer = max(answer, current)
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 2, 3, 3, 2, 2],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().longestSubarray(*args) == expected

"""3095. 或值至少 K 的最短子数组 I"""


class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        answer = len(nums) + 1
        for left in range(len(nums)):
            value = 0
            for right in range(left, len(nums)):
                value |= nums[right]
                if value >= k:
                    answer = min(answer, right - left + 1)
                    break
        return answer if answer <= len(nums) else -1


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3], 2), 1),
        (([2, 1, 8], 10), 3),
        (([1, 2], 0), 1),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumSubarrayLength(*args) == expected

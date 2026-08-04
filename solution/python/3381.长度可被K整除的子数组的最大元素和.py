class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        minimum_prefix = [10**30] * k
        minimum_prefix[0] = 0
        prefix = 0
        answer = -(10**30)
        for index, value in enumerate(nums, 1):
            prefix += value
            remainder = index % k
            answer = max(answer, prefix - minimum_prefix[remainder])
            minimum_prefix[remainder] = min(minimum_prefix[remainder], prefix)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4, 5], 2), 14),
        (([-5, -2, -3], 2), -5),
        (([1, -2, 3, 4], 3), 5),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().maxSubarraySum(nums, k) == expected

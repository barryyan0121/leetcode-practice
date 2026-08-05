"""2104. 子数组范围和"""


class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            low = high = nums[i]
            for j in range(i + 1, len(nums)):
                low = min(low, nums[j])
                high = max(high, nums[j])
                answer += high - low
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 2, 3],), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().subArrayRanges(*args) == expected

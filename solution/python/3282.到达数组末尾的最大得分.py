class Solution:
    def findMaximumScore(self, nums: list[int]) -> int:
        best = 0
        answer = 0
        for value in nums[:-1]:
            best = max(best, value)
            answer += best
        return answer


if __name__ == "__main__":
    test_cases = [([1, 3, 1, 5], 7), ([4, 3, 1, 3, 2], 16)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().findMaximumScore(nums) == expected

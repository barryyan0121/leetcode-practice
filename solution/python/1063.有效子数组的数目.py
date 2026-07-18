class Solution:
    def validSubarrays(self, nums: list[int]) -> int:
        stack = []
        answer = 0
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                answer += i - stack.pop()
            stack.append(i)
        while stack:
            answer += len(nums) - stack.pop()
        return answer


if __name__ == "__main__":
    test_cases = [([1, 4, 2, 5, 3], 11), ([3, 2, 1], 3), ([2, 2, 2], 6)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().validSubarrays(nums) == expected

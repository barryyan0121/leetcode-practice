"""1950. 所有子数组最小值中的最大值"""


class Solution:
    def maxMinSubarray(self, nums: list[int]) -> int:
        stack = []
        answer = 0
        for i in range(len(nums) + 1):
            value = nums[i] if i < len(nums) else 0
            while stack and nums[stack[-1]] >= value:
                index = stack.pop()
                left = stack[-1] if stack else -1
                answer = max(answer, nums[index] * (i - left - 1))
            stack.append(i)
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 2, 3, 2],), 6)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxMinSubarray(*args) == expected

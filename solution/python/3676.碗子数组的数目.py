"""3676. 碗子数组的数目"""


class Solution:
    def bowlSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        left = [-1] * n
        stack = []
        for index, value in enumerate(nums):
            while stack and nums[stack[-1]] < value:
                stack.pop()
            if stack:
                left[index] = stack[-1]
            stack.append(index)
        right = [-1] * n
        stack = []
        for index in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[index]:
                stack.pop()
            if stack:
                right[index] = stack[-1]
            stack.append(index)
        return sum(a != -1 and b != -1 and b - a >= 2 for a, b in zip(left, right))


if __name__ == "__main__":
    test_cases = [(([2, 5, 3, 1, 4],), 2), (([5, 1, 2, 3, 4],), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().bowlSubarrays(*args) == expected

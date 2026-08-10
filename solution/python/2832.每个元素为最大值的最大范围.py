"""2832. 每个元素为最大值的最大范围"""


class Solution:
    def maximumLengthOfRanges(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = [-1] * n
        stack = []
        for index, value in enumerate(nums):
            while stack and nums[stack[-1]] < value:
                stack.pop()
            left[index] = stack[-1] if stack else -1
            stack.append(index)
        right = [n] * n
        stack = []
        for index in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[index]:
                stack.pop()
            right[index] = stack[-1] if stack else n
            stack.append(index)
        return [right[index] - left[index] - 1 for index in range(n)]


if __name__ == "__main__":
    assert Solution().maximumLengthOfRanges([1, 5, 4, 3, 2]) == [1, 5, 3, 2, 1]

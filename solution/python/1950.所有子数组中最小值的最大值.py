"""1950. 所有子数组中最小值的最大值"""


class Solution:
    def findMaximums(self, nums: list[int]) -> list[int]:
        size = len(nums)
        left = [-1] * size
        right = [size] * size
        stack = []
        for index, value in enumerate(nums):
            while stack and nums[stack[-1]] >= value:
                stack.pop()
            if stack:
                left[index] = stack[-1]
            stack.append(index)
        stack = []
        for index in range(size - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[index]:
                stack.pop()
            if stack:
                right[index] = stack[-1]
            stack.append(index)
        result = [0] * size
        for index, value in enumerate(nums):
            length = right[index] - left[index] - 1
            result[length - 1] = max(result[length - 1], value)
        for index in range(size - 2, -1, -1):
            result[index] = max(result[index], result[index + 1])
        return result


if __name__ == "__main__":
    assert Solution().findMaximums([0, 1, 2, 4]) == [4, 2, 1, 0]

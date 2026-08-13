class Solution:
    def findIndices(
        self, nums: list[int], indexDifference: int, valueDifference: int
    ) -> list[int]:
        min_index = max_index = 0
        for right in range(indexDifference, len(nums)):
            left = right - indexDifference
            if nums[left] < nums[min_index]:
                min_index = left
            if nums[left] > nums[max_index]:
                max_index = left
            if nums[right] - nums[min_index] >= valueDifference:
                return [min_index, right]
            if nums[max_index] - nums[right] >= valueDifference:
                return [max_index, right]
        return [-1, -1]


assert Solution().findIndices([5, 1, 4, 1], 2, 4) == [0, 3]

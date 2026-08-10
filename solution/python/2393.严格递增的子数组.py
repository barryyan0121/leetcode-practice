"""2393. 严格递增的子数组"""


class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        answer = length = 1
        for index in range(1, len(nums)):
            if nums[index] > nums[index - 1]:
                length += 1
            else:
                length = 1
            answer += length
        return answer

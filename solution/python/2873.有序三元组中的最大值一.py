"""2873. 有序三元组中的最大值 I"""


class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        suffix = [0] * len(nums)
        for index in range(len(nums) - 2, -1, -1):
            suffix[index] = max(suffix[index + 1], nums[index + 1])
        prefix = nums[0]
        answer = 0
        for index in range(1, len(nums) - 1):
            answer = max(answer, (prefix - nums[index]) * suffix[index])
            prefix = max(prefix, nums[index])
        return answer


if __name__ == "__main__":
    assert Solution().maximumTripletValue([12, 6, 1, 2, 7]) == 77

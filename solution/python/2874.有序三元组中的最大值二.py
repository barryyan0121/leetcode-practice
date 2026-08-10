"""2874. 有序三元组中的最大值 II"""


class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        maximum = nums[0]
        answer = 0
        best_difference = 0
        for value in nums[1:]:
            answer = max(answer, best_difference * value)
            best_difference = max(best_difference, maximum - value)
            maximum = max(maximum, value)
        return answer


if __name__ == "__main__":
    assert Solution().maximumTripletValue([1, 10, 3, 4, 19]) == 133

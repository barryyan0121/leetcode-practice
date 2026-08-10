"""2680. 最大或值"""


class Solution:
    def maximumOr(self, nums: list[int], k: int) -> int:
        suffix = [0] * (len(nums) + 1)
        for index in range(len(nums) - 1, -1, -1):
            suffix[index] = suffix[index + 1] | nums[index]
        prefix = 0
        answer = 0
        for index, value in enumerate(nums):
            answer = max(answer, prefix | (value << k) | suffix[index + 1])
            prefix |= value
        return answer


if __name__ == "__main__":
    assert Solution().maximumOr([12, 9], 1) == 30

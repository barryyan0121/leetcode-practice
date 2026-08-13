#
# @lc app=leetcode.cn id=3979 lang=python3
#
# [3979] 最大有效数对和
#


class Solution:
    # @lc code=start
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        best = 0
        answer = 0
        for index in range(k, len(nums)):
            best = max(best, nums[index - k])
            answer = max(answer, best + nums[index])
        return answer

    # @lc code=end


if __name__ == "__main__":
    test_cases = [
        (([1, 3, 5, 2, 8], 2), 13),
        (([5, 1, 9], 1), 14),
        (([10, 1], 1), 11),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxValidPairSum(*args) == expected

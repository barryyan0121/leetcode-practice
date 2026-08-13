"""3038. 相同分数的最大操作数目 I"""


class Solution:
    def maxOperations(self, nums: list[int]) -> int:
        score = nums[0] + nums[1]
        answer = 0
        for index in range(0, len(nums) - 1, 2):
            if nums[index] + nums[index + 1] != score:
                break
            answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [
        ([3, 2, 1, 4, 5], 2),
        ([1, 5, 3, 3, 4, 1, 3, 2, 2, 3], 2),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().maxOperations(nums) == expected

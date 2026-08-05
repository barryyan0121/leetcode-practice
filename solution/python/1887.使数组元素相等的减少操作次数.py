"""1887. 使数组元素相等的减少操作次数"""


class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        ordered = sorted(nums)
        answer = 0
        levels = 0
        for index in range(1, len(ordered)):
            if ordered[index] != ordered[index - 1]:
                levels += 1
            answer += levels
        return answer


if __name__ == "__main__":
    test_cases = [([5, 1, 3], 3), ([1, 1, 1], 0)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().reductionOperations(nums) == expected

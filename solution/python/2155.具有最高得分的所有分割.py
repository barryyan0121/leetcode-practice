"""2155. 具有最高得分的所有分割"""


class Solution:
    def maxScoreIndices(self, nums: list[int]) -> list[int]:
        right_ones = sum(nums)
        left_zeros = 0
        best = -1
        answer = []
        for index in range(len(nums) + 1):
            score = left_zeros + right_ones
            if score > best:
                best = score
                answer = [index]
            elif score == best:
                answer.append(index)
            if index < len(nums):
                if nums[index] == 0:
                    left_zeros += 1
                else:
                    right_ones -= 1
        return answer


if __name__ == "__main__":
    test_cases = [(([0, 0, 1, 0],), [2, 4])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxScoreIndices(*args) == expected

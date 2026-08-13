"""3847. 计算比赛分数差"""


class Solution:
    def scoreDifference(self, nums: list[int]) -> int:
        score = [0, 0]
        active = 0
        for index, value in enumerate(nums):
            if value % 2 == 1:
                active ^= 1
            if index % 6 == 5:
                active ^= 1
            score[active] += value
        return score[0] - score[1]


if __name__ == "__main__":
    test_cases = [(([1, 2, 3],), 0), (([2, 4, 2, 1, 2, 1],), 4), (([1],), -1)]
    for args, expected in test_cases:
        assert Solution().scoreDifference(*args) == expected

#
# @lc app=leetcode.cn id=1176 lang=python3
#
# [1176] 健身计划评估
#


# @lc code=start
class Solution:
    def dietPlanPerformance(self, calories, k, lower, upper):
        score = 0
        total = sum(calories[:k])
        for index in range(k, len(calories) + 1):
            if total < lower:
                score -= 1
            elif total > upper:
                score += 1
            if index < len(calories):
                total += calories[index] - calories[index - k]
        return score


# @lc code=end


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4, 5], 1, 3, 3), 0),
        (([3, 2], 2, 0, 1), 1),
    ]
    for index, (args, expected) in enumerate(test_cases):
        assert Solution().dietPlanPerformance(*args) == expected, index

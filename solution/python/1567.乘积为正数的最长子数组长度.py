# @lc app=leetcode.cn id=1567 lang=python3


class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        positive = negative = answer = 0
        for number in nums:
            if number == 0:
                positive = negative = 0
            elif number > 0:
                positive += 1
                negative = negative + 1 if negative else 0
            else:
                positive, negative = (negative + 1 if negative else 0), positive + 1
            answer = max(answer, positive)
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.getMaxLen, ([1, -2, -3, 4],), 4),
        (solution.getMaxLen, ([0, 1, -2, -3, -4],), 3),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1567 题 "乘积为正数的最长子数组长度" 所有测试用例通过')

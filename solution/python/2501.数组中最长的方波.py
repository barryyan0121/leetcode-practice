# @lc app=leetcode.cn id=2501 lang=python3


class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        values = set(nums)
        answer = -1
        for value in values:
            length = 1
            current = value
            while current * current in values:
                current *= current
                length += 1
            if length >= 2:
                answer = max(answer, length)
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.longestSquareStreak, ([4, 3, 6, 16, 8, 2],), 3),
        (solution.longestSquareStreak, ([2, 3, 5, 6, 7],), -1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2501 题 "数组中最长的方波" 所有测试用例通过')

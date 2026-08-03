# @lc app=leetcode.cn id=1550 lang=python3


class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        streak = 0
        for value in arr:
            streak = streak + 1 if value % 2 else 0
            if streak == 3:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.threeConsecutiveOdds, ([2, 6, 4, 1],), False),
        (solution.threeConsecutiveOdds, ([1, 2, 34, 3, 4, 5, 7, 23, 12],), True),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1550 题 "存在连续三个奇数的数组" 所有测试用例通过')

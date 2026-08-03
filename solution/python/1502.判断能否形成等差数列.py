# @lc app=leetcode.cn id=1502 lang=python3


class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        values = sorted(arr)
        difference = values[1] - values[0]
        return all(
            values[index] - values[index - 1] == difference
            for index in range(2, len(values))
        )


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.canMakeArithmeticProgression, ([3, 5, 1],), True)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1502 题 "判断能否形成等差数列" 所有测试用例通过')

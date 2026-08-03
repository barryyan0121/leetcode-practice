# @lc app=leetcode.cn id=1414 lang=python3


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibonacci = [1, 1]
        while fibonacci[-1] <= k:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        count = 0
        for number in reversed(fibonacci):
            if number <= k:
                k -= number
                count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findMinFibonacciNumbers, (7,), 2),
        (solution.findMinFibonacciNumbers, (10,), 2),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1414 题 "和为 K 的最少斐波那契数字数目" 所有测试用例通过')

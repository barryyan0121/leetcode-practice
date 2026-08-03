# @lc app=leetcode.cn id=1390 lang=python3
from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for number in nums:
            divisors = []
            divisor = 1
            while divisor * divisor <= number:
                if number % divisor == 0:
                    divisors.append(divisor)
                    if divisor * divisor != number:
                        divisors.append(number // divisor)
                if len(divisors) > 4:
                    break
                divisor += 1
            if len(divisors) == 4:
                total += sum(divisors)
        return total


if __name__ == "__main__":
    test_cases = [
        (Solution().sumFourDivisors, ([21, 4, 7],), 32),
        (Solution().sumFourDivisors, ([1, 2, 3, 4, 5],), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1390 题 "四因数" 所有测试用例通过')

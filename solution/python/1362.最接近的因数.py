# @lc app=leetcode.cn id=1362 lang=python3

from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def find(value: int) -> List[int]:
            for first in range(int(value**0.5), 0, -1):
                if value % first == 0:
                    return [first, value // first]
            return [1, value]

        first, second = find(num + 1), find(num + 2)
        return first if first[1] - first[0] < second[1] - second[0] else second


if __name__ == "__main__":
    test_cases = [
        (Solution().closestDivisors, (8,), [3, 3]),
        (Solution().closestDivisors, (123,), [5, 25]),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1362 题 "最接近的因数" 所有测试用例通过')

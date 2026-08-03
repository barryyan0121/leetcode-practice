# @lc app=leetcode.cn id=1300 lang=python3

from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        left, right = 0, max(arr)
        while left < right:
            value = (left + right) // 2
            if sum(min(number, value) for number in arr) < target:
                left = value + 1
            else:
                right = value
        candidates = [max(0, left - 1), left]
        return min(
            candidates,
            key=lambda value: (
                abs(sum(min(number, value) for number in arr) - target),
                value,
            ),
        )


if __name__ == "__main__":
    test_cases = [
        (Solution().findBestValue, ([4, 9, 3], 10), 3),
        (Solution().findBestValue, ([2, 3, 5], 10), 5),
        (Solution().findBestValue, ([60864, 25176, 27249, 21296, 20204], 56803), 11361),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1300 题 "转变数组后最接近目标值的数组和" 所有测试用例通过')

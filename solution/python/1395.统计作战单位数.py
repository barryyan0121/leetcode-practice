# @lc app=leetcode.cn id=1395 lang=python3
from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result = 0
        for middle in range(len(rating)):
            left_less = sum(rating[left] < rating[middle] for left in range(middle))
            right_less = sum(
                rating[right] < rating[middle]
                for right in range(middle + 1, len(rating))
            )
            left_greater = middle - left_less
            right_greater = len(rating) - middle - 1 - right_less
            result += left_less * right_greater + left_greater * right_less
        return result


if __name__ == "__main__":
    test_cases = [
        (Solution().numTeams, ([2, 5, 3, 4, 1],), 3),
        (Solution().numTeams, ([2, 1, 3],), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1395 题 "统计作战单位数" 所有测试用例通过')

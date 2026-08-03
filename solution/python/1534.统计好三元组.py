# @lc app=leetcode.cn id=1534 lang=python3


class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        return sum(
            abs(arr[first] - arr[second]) <= a
            and abs(arr[second] - arr[third]) <= b
            and abs(arr[first] - arr[third]) <= c
            for first in range(len(arr))
            for second in range(first + 1, len(arr))
            for third in range(second + 1, len(arr))
        )


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.countGoodTriplets, ([3, 0, 1, 1, 9, 7], 7, 2, 3), 4)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1534 题 "统计好三元组" 所有测试用例通过')

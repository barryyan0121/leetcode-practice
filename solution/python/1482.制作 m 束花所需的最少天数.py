# @lc app=leetcode.cn id=1482 lang=python3


class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def possible(day: int) -> bool:
            bouquets = flowers = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            middle = (left + right) // 2
            if possible(middle):
                right = middle
            else:
                left = middle + 1
        return left


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.minDays, ([1, 10, 3, 10, 2], 3, 1), 3)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1482 题 "制作 m 束花所需的最少天数" 所有测试用例通过')

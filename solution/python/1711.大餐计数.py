# @lc app=leetcode.cn id=1711 lang=python3


class Solution:
    def countPairs(self, deliciousness: list[int]) -> int:
        mod = 10**9 + 7
        counts = {}
        answer = 0
        for value in deliciousness:
            for power in range(22):
                answer += counts.get((1 << power) - value, 0)
            counts[value] = counts.get(value, 0) + 1
        return answer % mod


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.countPairs, ([1, 3, 5, 7, 9],), 4),
        (solution.countPairs, ([1, 1, 1, 3, 3, 3, 7],), 15),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1711 题 "大餐计数" 所有测试用例通过')

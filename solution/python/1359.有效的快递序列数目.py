# @lc app=leetcode.cn id=1359 lang=python3


class Solution:
    def countOrders(self, n: int) -> int:
        result = 1
        mod = 10**9 + 7
        for order in range(1, n + 1):
            result = result * order * (2 * order - 1) % mod
        return result


if __name__ == "__main__":
    test_cases = [
        (Solution().countOrders, (1,), 1),
        (Solution().countOrders, (2,), 6),
        (Solution().countOrders, (3,), 90),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1359 题 "有效的快递序列数目" 所有测试用例通过')

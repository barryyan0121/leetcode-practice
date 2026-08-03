# @lc app=leetcode.cn id=1524 lang=python3


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod = 10**9 + 7
        counts = [1, 0]
        parity = result = 0
        for value in arr:
            parity ^= value & 1
            result = (result + counts[parity ^ 1]) % mod
            counts[parity] += 1
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.numOfSubarrays, ([1, 3, 5],), 4)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1524 题 "和为奇数的子数组数目" 所有测试用例通过')

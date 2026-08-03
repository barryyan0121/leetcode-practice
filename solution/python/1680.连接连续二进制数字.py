# @lc app=leetcode.cn id=1680 lang=python3


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        answer = 0
        for value in range(1, n + 1):
            answer = (answer << value.bit_length() | value) % mod
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.concatenatedBinary, (1,), 1),
        (solution.concatenatedBinary, (3,), 27),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1680 题 "连接连续二进制数字" 所有测试用例通过')

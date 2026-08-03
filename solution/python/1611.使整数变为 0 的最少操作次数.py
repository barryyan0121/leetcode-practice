# @lc app=leetcode.cn id=1611 lang=python3


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        answer = 0
        while n:
            answer ^= n
            n >>= 1
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minimumOneBitOperations, (3,), 2),
        (solution.minimumOneBitOperations, (6,), 4),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1611 题 "使整数变为 0 的最少操作次数" 所有测试用例通过')

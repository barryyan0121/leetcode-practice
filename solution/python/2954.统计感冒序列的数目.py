# @lc app=leetcode.cn id=2954 lang=python3


class Solution:
    def numberOfSequence(self, n: int, sick: list[int]) -> int:
        modulus = 10**9 + 7
        healthy = n - len(sick)
        factorial = [1] * (healthy + 1)
        for value in range(1, healthy + 1):
            factorial[value] = factorial[value - 1] * value % modulus
        inverse_factorial = [1] * (healthy + 1)
        inverse_factorial[healthy] = pow(factorial[healthy], modulus - 2, modulus)
        for value in range(healthy, 0, -1):
            inverse_factorial[value - 1] = inverse_factorial[value] * value % modulus
        gaps = [sick[0]]
        for left, right in zip(sick, sick[1:]):
            gaps.append(right - left - 1)
        gaps.append(n - 1 - sick[-1])
        result = factorial[healthy]
        for gap in gaps:
            result = result * inverse_factorial[gap] % modulus
        for gap in gaps[1:-1]:
            if gap:
                result = result * pow(2, gap - 1, modulus) % modulus
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numberOfSequence, (5, [0, 4]), 4),
        (solution.numberOfSequence, (6, [0, 1]), 1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2954 题 "统计感冒序列的数目" 所有测试用例通过')

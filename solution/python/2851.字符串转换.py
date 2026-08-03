# @lc app=leetcode.cn id=2851 lang=python3


class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        modulus = 10**9 + 7
        length = len(s)
        same = 0
        other = 0
        for index in range(length):
            if (s + s)[index : index + length] == t:
                if index == 0:
                    same += 1
                else:
                    other += 1

        matrix = [[0, length - 1], [1, length - 2]]
        powered = self._matrix_power(matrix, k, modulus)
        ways_same = powered[0][0]
        ways_other = powered[1][0]
        return (same * ways_same + other * ways_other) % modulus

    @staticmethod
    def _matrix_power(
        matrix: list[list[int]], exponent: int, modulus: int
    ) -> list[list[int]]:
        result = [[1, 0], [0, 1]]
        while exponent:
            if exponent & 1:
                result = Solution._multiply(result, matrix, modulus)
            matrix = Solution._multiply(matrix, matrix, modulus)
            exponent >>= 1
        return result

    @staticmethod
    def _multiply(
        left: list[list[int]], right: list[list[int]], modulus: int
    ) -> list[list[int]]:
        return [
            [
                (left[row][0] * right[0][col] + left[row][1] * right[1][col]) % modulus
                for col in range(2)
            ]
            for row in range(2)
        ]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numberOfWays, ("abcd", "cdab", 2), 2),
        (solution.numberOfWays, ("abab", "abab", 1), 1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2851 题 "字符串转换" 所有测试用例通过')

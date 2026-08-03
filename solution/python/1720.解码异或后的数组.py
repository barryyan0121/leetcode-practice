# @lc app=leetcode.cn id=1720 lang=python3


class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        result = [first]
        for value in encoded:
            result.append(result[-1] ^ value)
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.decode, ([1, 2, 3], 1), [1, 0, 2, 1]),
        (solution.decode, ([6, 2, 7, 3], 4), [4, 2, 0, 7, 4]),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1720 题 "解码异或后的数组" 所有测试用例通过')

# @lc app=leetcode.cn id=2055 lang=python3


class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        length = len(s)
        prefix = [0] * (length + 1)
        left_candle = [-1] * length
        right_candle = [-1] * length
        nearest = -1
        for index, char in enumerate(s):
            if char == "|":
                nearest = index
            left_candle[index] = nearest
            prefix[index + 1] = prefix[index] + (char == "*")
        nearest = -1
        for index in range(length - 1, -1, -1):
            if s[index] == "|":
                nearest = index
            right_candle[index] = nearest
        result = []
        for start, end in queries:
            left = right_candle[start]
            right = left_candle[end]
            result.append(
                prefix[right] - prefix[left] if left != -1 and left <= right else 0
            )
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.platesBetweenCandles,
            (
                "**|**|***|",
                [[2, 5], [5, 9]],
            ),
            [2, 3],
        ),
        (solution.platesBetweenCandles, ("***|", [[0, 2]]), [0]),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2055 题 "蜡烛之间的盘子" 所有测试用例通过')

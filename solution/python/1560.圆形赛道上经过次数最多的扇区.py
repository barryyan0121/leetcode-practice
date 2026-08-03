# @lc app=leetcode.cn id=1560 lang=python3


class Solution:
    def mostVisited(self, n: int, rounds: list[int]) -> list[int]:
        start, end = rounds[0], rounds[-1]
        if start <= end:
            return list(range(start, end + 1))
        return list(range(1, end + 1)) + list(range(start, n + 1))


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.mostVisited, (4, [1, 3, 1, 2]), [1, 2]),
        (solution.mostVisited, (2, [2, 1, 2, 1, 2, 1, 2, 1]), [1, 2]),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1560 题 "圆形赛道上经过次数最多的扇区" 所有测试用例通过')

# @lc app=leetcode.cn id=1436 lang=python3


class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        starts = {start for start, _ in paths}
        return next(end for _, end in paths if end not in starts)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.destCity,
            ([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]],),
            "Sao Paulo",
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1436 题 "旅行终点站" 所有测试用例通过')

# @lc app=leetcode.cn id=2201 lang=python3


class Solution:
    def digArtifacts(
        self, n: int, artifacts: list[list[int]], dig: list[list[int]]
    ) -> int:
        dug = {tuple(cell) for cell in dig}
        return sum(
            all(
                (row, col) in dug
                for row in range(r1, r2 + 1)
                for col in range(c1, c2 + 1)
            )
            for r1, c1, r2, c2 in artifacts
        )


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.digArtifacts,
            (2, [[0, 0, 0, 0], [0, 1, 1, 1]], [[0, 0], [0, 1], [1, 1]]),
            2,
        ),
        (solution.digArtifacts, (1, [[0, 0, 0, 0]], []), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2201 题 "统计可以提取的工件" 所有测试用例通过')

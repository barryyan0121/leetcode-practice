# @lc app=leetcode.cn id=1510 lang=python3


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        winning = [False] * (n + 1)
        for total in range(1, n + 1):
            square = 1
            while square * square <= total:
                if not winning[total - square * square]:
                    winning[total] = True
                    break
                square += 1
        return winning[n]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.winnerSquareGame, (1,), True),
        (solution.winnerSquareGame, (2,), False),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1510 题 "石子游戏 IV" 所有测试用例通过')

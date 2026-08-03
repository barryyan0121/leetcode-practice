# @lc app=leetcode.cn id=1583 lang=python3


class Solution:
    def unhappyFriends(
        self, n: int, preferences: list[list[int]], pairs: list[list[int]]
    ) -> int:
        rank = [[0] * n for _ in range(n)]
        for person in range(n):
            for order, other in enumerate(preferences[person]):
                rank[person][other] = order
        partner = {}
        for a, b in pairs:
            partner[a], partner[b] = b, a
        return sum(
            any(
                rank[x][y] < rank[x][partner[x]] and rank[y][x] < rank[y][partner[y]]
                for y in preferences[x]
            )
            for x in range(n)
        )


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.unhappyFriends,
            (4, [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], [[0, 1], [2, 3]]),
            2,
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1583 题 "不开心的朋友" 所有测试用例通过')

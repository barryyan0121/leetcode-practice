"""2005. 斐波那契树的移除子树游戏"""


class Solution:
    def findGameWinner(self, n: int) -> bool:
        return n % 6 != 1


if __name__ == "__main__":
    test_cases = [((2,), True), ((7,), False)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findGameWinner(*args) == expected

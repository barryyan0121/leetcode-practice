"""2550. 猴子碰撞的方法数"""


class Solution:
    def monkeyMove(self, n: int) -> int:
        mod = 10**9 + 7
        return (pow(2, n, mod) - 2) % mod


if __name__ == "__main__":
    test_cases = [((3,), 6)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().monkeyMove(*args) == expected

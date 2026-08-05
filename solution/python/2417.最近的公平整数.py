"""2417. 最近的公平整数"""


class Solution:
    def closestFair(self, n: int) -> int:
        while True:
            text = str(n)
            if (
                len(text) % 2 == 0
                and sum(int(digit) % 2 == 0 for digit in text) == len(text) // 2
            ):
                return n
            n += 1


if __name__ == "__main__":
    test_cases = [((1,), 10)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().closestFair(*args) == expected

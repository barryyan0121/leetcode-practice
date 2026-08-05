"""1881. 插入后的最大值"""


class Solution:
    def maxValue(self, n: str, x: int) -> str:
        digit = str(x)
        if n[0] == "-":
            position = next(
                (index for index in range(1, len(n)) if n[index] > digit), len(n)
            )
        else:
            position = next(
                (index for index, value in enumerate(n) if value < digit), len(n)
            )
        return n[:position] + digit + n[position:]


if __name__ == "__main__":
    test_cases = [(("99", 9), "999"), (("-13", 2), "-123")]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxValue(*args) == expected

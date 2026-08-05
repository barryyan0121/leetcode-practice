"""1963. 使字符串平衡的最小交换次数"""


class Solution:
    def minSwaps(self, s: str) -> int:
        balance = minimum = 0
        for char in s:
            balance += 1 if char == "[" else -1
            minimum = min(minimum, balance)
        return (-minimum + 1) // 2


if __name__ == "__main__":
    test_cases = [(("][][",), 1), [(("]]][[[",), 2)][0]]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minSwaps(*args) == expected

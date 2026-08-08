class Solution:
    def encode(self, num: int) -> str:
        return bin(num + 1)[3:]


if __name__ == "__main__":
    test_cases = [(23, "1000"), (0, "")]
    for _, (num, expected) in enumerate(test_cases):
        assert Solution().encode(num) == expected

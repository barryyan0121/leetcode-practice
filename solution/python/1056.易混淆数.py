class Solution:
    def confusingNumber(self, n: int) -> bool:
        mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        try:
            return int("".join(mapping[char] for char in reversed(str(n)))) != n
        except KeyError:
            return False


if __name__ == "__main__":
    test_cases = [(6, True), (11, False), (25, False)]
    for _, (n, expected) in enumerate(test_cases):
        assert Solution().confusingNumber(n) == expected
